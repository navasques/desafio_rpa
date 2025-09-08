import logging
from datetime import datetime

# Configurando o logger
logger = logging.getLogger("MeuLogger")
logger.setLevel(logging.DEBUG)

# Formato
formatter = logging.Formatter(
    "%(asctime)s %(levelname)s : %(message)s", datefmt="%d-%m-%Y %H:%M:%S"
)

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

# Contador
ERROS_ENCONTRADOS = 0


def LOGGER(log_level, msg):
    global ERROS_ENCONTRADOS

    level = log_level.upper()
    if level == "ERRO":
        ERROS_ENCONTRADOS += 1
        logger.error(msg)
    elif level == "INFO":
        logger.info(msg)
    else:
        logger.debug(msg)
