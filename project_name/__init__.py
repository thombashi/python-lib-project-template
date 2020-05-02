from .__version__ import __author__, __copyright__, __email__, __license__, __version__
from .logger import logger


def do_something(value: str) -> str:
    logger.debug("logging")

    return value


def failed_func(value: str) -> None:
    raise ValueError("always failed")
