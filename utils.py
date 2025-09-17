from logger import setup_logger
from datetime import datetime
import pandas as pd

logger = setup_logger("utils")


def salvar_csv(data, filename):
    try:
        df = pd.DataFrame(data)
        df.to_csv(filename, index=False, encoding="utf-8")
        logger.info(f"Dados salvos em {filename}")
    except Exception as e:
        logger.error(f"Erro ao salvar CSV: {e}")


def current_timestamp():
    return datetime.now().strftime("%d-%m-%Y %H:%M:%S")
