from .__version__ import __author__, __copyright__, __email__, __license__, __version__
from .logger import logger  # type: ignore


__all__ = (
    "__author__",
    "__copyright__",
    "__email__",
    "__license__",
    "__version__",
    "do_something",
    "failed_func",
    "logger",
)


def do_something(value: str) -> str:
    """[summary]

    Args:
        value (str): [description]

    Returns:
        str: [description]
    """

    logger.debug("logging")

    return value


def failed_func(value: str) -> None:
    """[summary]

    Args:
        value (str): [description]

    Raises:
        ValueError: [description]
    """

    raise ValueError("always failed")
