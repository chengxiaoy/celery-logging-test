import logging
import os

logger = logging.getLogger(__name__)


def print_log():
    print(f"currnt logger {logger} disabled {logger.disabled} current process id is {os.getpid()}")

    logger.debug(f"{os.getpid()}=========debug log===========")
    logger.info(f"{os.getpid()}=========info log===========")
    logger.warning(f"{os.getpid()}=========WARNING log===========")
