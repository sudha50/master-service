import logging.handlers
import os
import sys
import logging



FORMAT = '%(asctime)s %(levelname)s %(message)s'

logging.basicConfig(format=FORMAT)

logger = logging.getLogger()
logger.setLevel(logging.INFO)

handler = logging.StreamHandler(sys.stdout)

for handler in logging.handlers:
    logger.removeHandler(handler)
logger.addHandler(handler)


DEBUG_MODE = os.environ.get("DEBUG_MODE", "false")

MUL_HOST = os.environ.get("MUL_HOST", "0.0.0.0")
MUL_PORT = os.environ.get("MUL_PORT", "8001")

SUM_HOST = os.environ.get("SUM_HOST", "0.0.0.0")
SUM_PORT = os.environ.get("SUM_PORT", "8002")
