import logging
import sys
from datetime import datetime


def setup_logger(nome_automacao):
    logger = logging.getLogger(nome_automacao)
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    log_file = f"logs/{nome_automacao}_{datetime.now().strftime('%Y%m%d')}.log"
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    return logger
