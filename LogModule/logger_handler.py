#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author : wwu

from cgitb import handler
import logging
import logging.handlers
import datetime


def log_handler():

    #定义一个日志器
    logger = logging.getLogger('mytestlogger')
    logger.setLevel(logging.DEBUG) #默认级别

    #定义一个处理器，用于处理日志的一种方式：按时间分割
    handler1 =  logging.handlers.TimedRotatingFileHandler('all.log', when='midnight', interval=1, backupCount=7, atTime=datetime.time(0,0,0,0))
    #定义此处理器的格式
    handler1.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

    #定义第二个处理器
    handler2 = logging.FileHandler('error.log')
    handler2.setLevel(logging.ERROR)
    handler2.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"))

    #将处理器都添加到定义的日志器
    logger.addHandler(handler1)
    logger.addHandler(handler2)
    
    return logger


if __name__ == "__main__":
    myloger = log_handler()
    myloger.debug("debug message")
    myloger.info("info message")
    myloger.warning("warning message")
    myloger.error("error message")
    myloger.critical("critical message")