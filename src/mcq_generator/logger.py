import logging
import os
from datetime import datetime

LOG_FILE=f"logs/{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}.log"

LOG_FILE_PATH = os.path.join(os.getcwd(), LOG_FILE)

logger=logging.basicConfig(
    level=logging.INFO,
    filename=LOG_FILE_PATH,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)