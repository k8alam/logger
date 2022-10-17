import logging
import os
filename=os.path.basename(__file__)
logging.basicConfig(level=10,filename='mylog.txt',format='%(asctime)s:%(name)s:%(levelname)s:%(message)s',
                    datefmt='%d/%m/%Y %I:%M:%S %p',filemode='a')
logger = logging.getLogger(filename)
logger.critical('critical message')
logger.error('error message')
logger.warning('warning message')