# -*- coding:utf-8 -*-
import logging
logger0 = logging.getLogger("a")
logger1 = logging.getLogger("b")
from reportlogging import MultiLogger

logger = MultiLogger([logger0, logger1])

logging.basicConfig(level=logging.DEBUG)

logger.debug("hai")
logger.info("hai")

try:
    1 / 0
except:
    logger.warning("hai", exc_info=True)
