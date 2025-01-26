from signLanguage.logger import logging
from signLanguage.exception import SignLangException
import sys

# logging.info("Logger initialized")

try:
    x=10/0
except Exception as e:
    raise SignLangException(e, sys) from e