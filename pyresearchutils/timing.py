import time
from pyresearchutils import logger

TIME_LIST = []


def tic(log=None):
    if log is not None:
        logger.info(f"Start timing: {log}")
    TIME_LIST.append(time.time())


def toc(log=None):
    start = TIME_LIST.pop(-1)
    delta_time = time.time() - start
    logger.info(f"End timing: {log} in {delta_time}")
    return delta_time
