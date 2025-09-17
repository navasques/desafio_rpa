import requests
from logger import setup_logger
from utils import current_timestamp, salvar_csv

logger = setup_logger("api_script")


def fetch_data_api():
    # URL da API, passando as moedas para cotação
    url = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL,CNY-BRL,JPY-BRL"

    try:
        response = requests.get(url, timeout=10)
        # Estoura uma exceção para erros HTTP / 4xx e 5xx
        response.raise_for_status()

        # Transforma a response em um JSON
        data = response.json()

        resultado = [
            {
                "moeda": "DOLAR AMERICANO/REAL",
                "valor": data["USDBRL"]["bid"],
                "data_hora": current_timestamp(),
            },
            {
                "moeda": "EURO/REAL",
                "valor": data["EURBRL"]["bid"],
                "data_hora": current_timestamp(),
            },
            {
                "moeda": "BITCOIN/REAL",
                "valor": data["BTCBRL"]["bid"],
                "data_hora": current_timestamp(),
            },
            {
                "moeda": "YUAN/REAL",
                "valor": data["CNYBRL"]["bid"],
                "data_hora": current_timestamp(),
            },
            {
                "moeda": "IENE/REAL",
                "valor": data["JPYBRL"]["bid"],
                "data_hora": current_timestamp(),
            },
        ]

        logger.info("Dados da API obtidos com sucesso.")
        return resultado

    # Estoura uma exceção para erros de conexão
    except requests.exceptions.RequestException as e:
        logger.error(f"Erro ao acessar a API: {e}")
        return []


if __name__ == "__main__":
    results = fetch_data_api()
    if results:
        # Salva os dados em CSV e configura a saída
        salvar_csv(results, "outputs/api_output.csv")
    else:
        logger.error("Nenhuma cotação foi encontrada.")
