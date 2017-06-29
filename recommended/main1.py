#coding=utf-8


import os
import sys
import unittest


from modulea import func_nothing # !!! This will create the file modulea's global variable, so len(g_logger.handler)=2

from py_logger import LoggerHelper

g_logger_helper = LoggerHelper()
g_logger = g_logger_helper.get_logger()
g_logger_helper.enable_memory_log()


class MyTestCase(unittest.TestCase):
    def test(self):
        g_logger.info(u'from main') # print once


        self.assertEqual(len(g_logger.handlers), 2)
        l = g_logger_helper.get_formated_messages() # error, no memory log
        l = list(l)
        self.assertEqual(len(l), 1)

        l = map(lambda v : u'2 '+v, l)

        print(u'in memory:\n')
        print(os.linesep.join(l))
        sys.stdout.flush()


if __name__ == '__main__':
    unittest.main()