import logging
from datetime import datetime

# Configurando o logger
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s : %(message)s",
    datefmt="%d-%m-%Y %H:%M:%S",
)

logger = logging.getLogger("MeuLogger")

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
