import argparse
import sys

from loguru import logger

_LEVEL_ABBR = {
    "TRACE": "T", "DEBUG": "D", "INFO": "I", "SUCCESS": "S",
    "WARNING": "W", "ERROR": "E", "CRITICAL": "C",
}


def _fmt(record):
    abbr = _LEVEL_ABBR.get(record["level"].name, record["level"].name[0])
    return (
        "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
        f"<level>{abbr}</level> | "
        "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> | "
        "<level>{message}</level>\n{exception}"
    )


def configure_logging():
    """Configure loguru for console and file logging.

    Removes the default handler and sets up:
    - stderr handler at LOG_LEVEL (default: INFO, configurable via env var)
    - File handler at DEBUG level writing to LOG_FILE (default: app.log)
    """
    import os

    log_level = os.environ.get("LOG_LEVEL", "INFO")
    log_file = os.environ.get("LOG_FILE", "app.log")
    logger.remove()
    logger.add(sys.stderr, level=log_level, format=_fmt)
    logger.add(log_file, level="DEBUG", rotation="50 KB", retention=1, format=_fmt)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="second_brain",
        description="Second Brain CLI",
    )
    return parser


@logger.catch
def main():
    parser = build_parser()
    parser.parse_args()
    configure_logging()
    logger.info("Hello from second_brain!")
