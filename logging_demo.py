import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Started")
logging.warning("disk problem")
logging.error("Code not working syntax error")