import logging
import os
from config import LOG_FILE

if not os.path.exists("logs"):
    os.makedirs("logs")

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s | IP: %(message)s"
)

def log_event(ip, reason):
    logging.info(f"{ip} | {reason}")