import time
from logger import LOGGER
from utils import current_timestamp, salvar_csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


def fetch_currency_from_web():
    options = Options()
    # Argumento para rodar em tela cheia
    options.add_argument("--start-maximized")

    service = Service()
    driver = webdriver.Chrome(service=service, options=options)

    # Dicionario com as URLs de cada cotação
    cotacoes = {
        "DOLAR AMERICANO/REAL": "https://economia.uol.com.br/cotacoes/cambio/dolar-comercial-estados-unidos/",
        "EURO/REAL": "https://economia.uol.com.br/cotacoes/cambio/euro-uniao-europeia/",
        "BITCOIN/REAL": "https://economia.uol.com.br/cotacoes/cambio/criptomoeda/bitcoin/",
        "YUAN/REAL": "https://economia.uol.com.br/cotacoes/cambio/yuan-china/",
        "IENE/REAL": "https://economia.uol.com.br/cotacoes/cambio/iene-japao/",
    }

    # Inicializa lista vazia
    resultados = []

    try:
        # Para cada cotação, acessa a URL e extrai o valor
        for cotacao_nome, url in cotacoes.items():
            try:
                LOGGER("INFO", f"Buscando {cotacao_nome}")
                driver.get(url)
                # Espera 3 segundos para a página carregar
                time.sleep(3)

                try:
                    # Espera até o campo de valor estar visível
                    price_tag = WebDriverWait(driver, 20).until(
                        EC.visibility_of_element_located(
                            (By.CSS_SELECTOR, "input.field.normal[name='currency2']")
                        )
                    )
                    # Obtém o valor da cotação usando get_attribute do Selenium
                    cotacao_valor = price_tag.get_attribute("value")
                    LOGGER("INFO", f"{cotacao_nome}: {cotacao_valor}")

                # Estoura uma exceção se o elemento não for encontrado
                except TimeoutException:
                    LOGGER("ERRO", f"Timeout ao buscar o valor para {cotacao_nome}")
                    continue

                # Verifica se o valor foi encontrado
                if not cotacao_valor or cotacao_valor.strip() == "":
                    LOGGER(
                        "INFO",
                        f"Elemento encontrado para mas sem valor: {cotacao_nome}",
                    )

                    # Pula para a próxima cotação caso não tenha valor
                    continue

                LOGGER("INFO", f"Valor encontrado para {cotacao_nome}: {cotacao_valor}")
                resultados.append(
                    {
                        "moeda": cotacao_nome,
                        "valor": cotacao_valor.replace(",", "."),
                        "data_hora": current_timestamp(),
                    }
                )

            # Estoura uma exceção para outros erros
            except Exception as e:
                LOGGER("ERRO", f"Erro ao processar {cotacao_nome}: {e}")
                continue

        # Retorna a lista de resultados
        return resultados

    # Estoura uma exceção geral
    except Exception as e:
        LOGGER("ERRO", f"Erro geral: {e}")
        return resultados

    finally:
        # Fecha o navegador
        driver.quit()


if __name__ == "__main__":
    results = fetch_currency_from_web()
    if results:
        # Salva os dados em CSV e configura a saída
        salvar_csv(results, "outputs/scraping_output.csv")
        LOGGER("INFO", f"Dados salvos com sucesso. Total: {len(results)} registros.")
    else:
        LOGGER("ERRO", "Nenhuma cotação foi encontrada.")
