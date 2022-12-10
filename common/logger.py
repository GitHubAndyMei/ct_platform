# -*- coding: utf-8 -*-
"""
log module
"""

import logging
from config.config import LOG_PATH, PROJECT_NAME

logger = logging.getLogger("logger")
logger.setLevel(logging.INFO)

handler = logging.FileHandler(f"{LOG_PATH}/${PROJECT_NAME}.log")
handler.setFormatter(logging.Formatter("%(asctime)s|%(levelname)s|%(filename)s %(funcName)s %(lineno)s|%(message)s"))

logger.addHandler(handler)