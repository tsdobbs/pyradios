import logging
from logging import NullHandler
from pyradios.radios import RadioBrowser

__version__ = "0.0.22"

__all__ = ["RadioBrowser"]

logging.getLogger(__name__).addHandler(NullHandler())
