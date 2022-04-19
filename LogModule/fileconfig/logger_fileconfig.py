#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author : wwu

#使用fileConfig配置文件来定义日志格式

from asyncio.log import logger
import logging
import logging.config

logging.config.fileConfig('logging.conf')
logger = logging.getLogger('simple')

logger.debug('debug message')
logger.info('info message')
logger.error('error message')
logger.warning('warn message')
logger.critical('critical message')