from logger import LOGGER
from datetime import datetime
import pandas as pd


def salvar_csv(data, filename):
    try:
        df = pd.DataFrame(data)
        df.to_csv(filename, index=False, encoding="utf-8")
        LOGGER("INFO", f"Dados salvos em {filename}")
    except Exception as e:
        LOGGER("ERRO", f"Erro ao salvar CSV: {e}")


def current_timestamp():
    return datetime.now().strftime("%d-%m-%Y %H:%M:%S")
