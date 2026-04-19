"""
Logger file Package
"""

import logging
import sys
from pathlib import Path
from typing import Optional

_LOG_FORMAT = (
    "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"
)
_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


def _build_formatter() -> logging.Formatter:
    """
    Build and return the standard formatter used by all package loggers.
    """
    return logging.Formatter(fmt=_LOG_FORMAT, datefmt=_DATE_FORMAT)

def _build_console_handler(
        formatter: logging.Formatter,
) -> logging.StreamHandler:
    """
    Retrun a stream handler writting to stdout
    """
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(formatter)
    return handler


def _build_file_handler(
        log_file: str,
        formatter: logging.Formatter,
) -> logging.FileHandler:
    """
    Return a file handler writting to ``log_file``
    """
    path = Path(log_file)
    path.parent.mkdir(parents=True, exist_ok=True)

    handler = logging.FileHandler(path, encoding="utf-8")
    handler.setFormatter(formatter)
    return handler




def get_logger(
        name: str,
        level: int = logging.INFO,
        log_file: Optional[str] = None,
) -> logging.Logger:
    """
    This is the single entry point for logging across the entire package.
    Every module calls this function with its own ``__name__`` so log
    records show exactly which file produced them.
    """
    logger = logging.getLogger(name)

    # checking if logger already has hanlders
    if logger.handlers:
        return logger

    logger.setLevel(level)

    logger.propagate = False

    formatter = _build_formatter()

    # console handler
    console_handler = _build_console_handler(formatter)
    logger.addHandler(console_handler)

    # File handler when path is requested
    if log_file is not None:
        file_handler = _build_file_handler(log_file, formatter)
        logger.addHandler(file_handler)

    return logger