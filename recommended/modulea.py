#coding=utf-8


from py_logger import LoggerHelper


g_logger_helper = LoggerHelper()
g_logger = g_logger_helper.get_logger()
g_logger_helper.enable_memory_log()



def func_nothing(*args,**kwargs):
    pass