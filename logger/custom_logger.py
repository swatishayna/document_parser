import logging
import os
from datetime import datetime


class CustomLogger:
    def __init__(self, logs_dir = "logs"):
        self.logs_dir = os.path.join(os.getcwd(), logs_dir)
        os.makedirs(self.logs_dir, exist_ok=True)
        
        log_file = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
        log_file_path = os.path.join(logs_dir, log_file)

        logging.basicConfig(
            filename=log_file_path,
            format="[ %(asctime)s ] %(levelname)s %(name)s (line:%(lineno)d) - %(message)s",
            level=logging.INFO,
        )
        
    def get_logger(Self, name = __file__):
        return logging.getLogger(os.path.basename(name))
    
    
    
if __name__ == "main":
    logger = CustomLogger()
    logger = logger.get_logger(__file__)
    logger.info("Custom Logger Initialised")
    