#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author : wwu

import logging

def third():
    """
    结果：
    04/16/22 17:55:39 PM - WARNING - Tom[192.168.1.2] - this is third log.
    NoneType: None    #exe_info控制：
    Stack (most recent call last):   #stack_info控制
    File "d:\Code\code-practise\LogModule\logger3.py", line 27, in <module>
        third()
    File "d:\Code\code-practise\LogModule\logger3.py", line 25, in third
        logging.warning("this is third log.", exc_info=True, stack_info=True, extra={'user': 'Tom', 'ip':'192.168.1.2'})
    """
    LOG_FORMAT = "%(asctime)s - %(levelname)s - %(user)s[%(ip)s] - %(message)s"
    DATE_FORMAT = "%m/%d/%y %H:%M:%S %p"

    logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT)
    logging.warning("this is third log.", exc_info=True, stack_info=True, extra={'user': 'Tom', 'ip':'192.168.1.2'})

third()