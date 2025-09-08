import requests
from logger import LOGGER
from utils import current_timestamp, salvar_csv


def fetch_data_api():
    url = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL,CNY-BRL,JPY-BRL"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
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

        LOGGER("INFO", "Dados da API obtidos com sucesso.")
        return resultado

    except requests.exceptions.RequestException as e:
        LOGGER("ERRO", f"Erro ao acessar a API: {e}")
        return []


if __name__ == "__main__":
    results = fetch_data_api()
    if results:
        salvar_csv(results, "outputs/api_output.csv")
