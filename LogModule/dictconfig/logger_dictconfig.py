#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author : wwu

import logging
import logging.config
import yaml


with open('./logging.yaml', 'r') as f_conf:
    dict_conf = yaml.load(f_conf, Loader=yaml.CLoader)
logging.config.dictConfig(dict_conf)


logger1 = logging.getLogger('simpleExample')

logger1.debug('ogger1 debug message')
logger1.info('logger1 info message')
logger1.warning('logger1 warning message')
logger1.error('logger1 error message')
logger1.critical('logger1 critical message')
