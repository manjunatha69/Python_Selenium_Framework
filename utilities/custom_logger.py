import logging
import inspect


def customlogger(logLevel=logging.DEBUG):
       logger=logging.getLogger(inspect.stack()[1][3])

       logger.setLevel(logLevel)

       filehandler=logging.FileHandler("automation.log")
       filehandler.setLevel(logLevel)

       formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

       filehandler.setFormatter(formatter)

       logger.addHandler(filehandler)

       return logger



