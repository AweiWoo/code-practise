#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author : wwu

from asyncio.log import logger
import logging
import logging.config

logging.config.fileConfig('logging.conf')

logger = logging.getLogger('simple')

logger.debug('debug message')
logger.info('info message')
logger.error('error message')
logger.warn('warn message')
logger.critical('critical message')