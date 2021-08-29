import logging

# logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-9s) %(message)s',)
# logging.basicConfig(level=logging.INFO)
# logging.basicConfig(filename='example.log',level=logging.DEBUG)
# logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logging.basicConfig(filename='example.log', format='%(asctime)s %(levelname)s:%(message)s', level=logging.DEBUG, datefmt='%m/%d/%Y %I:%M:%S %p')

logging.warning('[warning] Watch out!')  # will print a message to the console
logging.info('[info] I told you so')  # will not print anything if the level is WARNING
logging.debug('[debug] Starting')
logging.error('[error] Error')
logging.critical('[critical] critical')

logging.warning('%s before you %s', 'Look', 'leap!')


