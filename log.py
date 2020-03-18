import logging

# DEBUG: Detailed information, typically of interest only when diagnosing problems.

# INFO: Confirmation that things are working as expected.

# WARNING: An indication that something unexpected, or indicative of some problem in the near future (e.g. 'disk space low'). The software is still working as expected.

# ERROR: Due to a more serious problem, the software has not been able to perform some function.

# CRITICAL: A serious error, indicating that the program itself may be unable to continue running.

""" set configuration """
# logging.basicConfig(filename='logpy.log', level=logging.INFO, format='%(levelname)s:%(message)s')


""" example of log info """
# logging.info("Log report #1")

""" setting logger """
logger = logging.getLogger(__name__) # logger creation
logger.setLevel(logging.INFO)   # setting the level

formatter = logging.Formatter('%(levelname)s:%(message)s') # create a formatter

file_handler = logging.FileHandler('logpy.log') # creating file handler
file_handler.setFormatter(formatter)     # setting the formatter

logger.addHandler(file_handler) # adding the file handler to the logger

# Now we have a configured logger that works with the specified configurations just like the root logger above 
# logger.info('something')