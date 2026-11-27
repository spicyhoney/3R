"""Example module for the demo package"""

from .logger_config import logger


def hello_world(message):
    """Example function to say Hello world with a message"""
    logger.debug("This is DEBUG level log message")
    logger.info("This is INFO level log message")
    logger.warning("This is WARN level log message")
    logger.error("This is ERROR level log message")
    return f"Hello world!: {message}"


def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert a temperature in degrees Celsius to degrees Fahrenheit."""
    return celsius * 1.8 + 32
