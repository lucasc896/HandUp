import logging

LOG_FORMAT = '(%(levelname)s) [%(module)s] %(asctime)-15s: %(message)s'


def setup_logging(verbose=False):
    logging.basicConfig(format=LOG_FORMAT)
    if verbose:
        logging.getLogger().setLevel(logging.DEBUG)
