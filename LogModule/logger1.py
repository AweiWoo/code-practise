from email import header
#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author : wwu

import logging

def first():
    """
    WARNING:root:this is a info warning log.
    ERROR:root:this is a error log.      
    CRITICAL:root:this is a critical log.
    """

    logging.debug("this is a debug log.")
    logging.info("this is a info log.")
    logging.warning("this is first info warning log.")
    logging.error("this is first error log.")
    logging.critical("this first a critical log.")

#默认等级：从warning开始，前面debug和info不打印
#默认格式：日志级别:日志器名称:日志内容， "%(levelname)s:%(name)s:%(message)s"
#默认输出位置：sys.stderr


def second():
    LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
    DATE_FORMAT = "%m/%d/%y %H:%M:%S %p"

    logging.basicConfig(filename='my.log', level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT)
    
    logging.warning("this is second info warning log.")
    logging.error("this is second error log.")
    logging.critical("this is second critical log.")


if __name__ == "__main__":
    #两个方法同时运行，只有第一个剩下，同一个文件中，logging.basicConfig()只有一个起作用
    first()
    second()  #不会运行