"""
Queue uses the queue-listener manager to listen from events from a redis
queue. Data is sent by extractor
"""

import os
from impulsare_config import Reader as ConfigReader
from impulsare_distributer import QueueManager
from impulsare_logger import Logger
from impulsare_writer import write_data


def rule_raw_data(data: dict, job: str):
    config_file = os.getenv('CONFIG_FILE')
    if config_file is None:
        config_file = '/etc/impulsare/config.yml'

    config = _read_config(config_file)
    logger = Logger('ruler', config_file)

    logger.log.debug('Ruler called')
    logger.log.debug('Config: ' + config_file)
    logger.log.debug('Config Content: ' + str(config))
    logger.log.debug('Job: ' + job)
    print('Data: ', data)

    # Do the transformation


    # Jobs done
    queue = QueueManager(config_file, 'ruler')
    queue.add(write_data, data, job=job)
    logger.log.debug('Sending to write_data')
    logger.log.debug('Leaving Ruler')


def _read_config(config_file: str):
    base_path = os.path.abspath(os.path.dirname(__file__))

    return ConfigReader().parse(
        config_file,
        base_path + '/static/specs.yml',
        base_path + '/static/default.yml')
