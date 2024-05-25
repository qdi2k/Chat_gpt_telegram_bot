import logging


def log(message):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('#%(levelname)-8s [%(asctime)s]'
                                  ' - %(filename)s: %(lineno)d - '
                                  '%(name)s - %(message)s')
    file_handler = logging.FileHandler('logger.log', encoding='utf-8')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.info(message)
