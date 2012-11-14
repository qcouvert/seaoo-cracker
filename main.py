#!/usr/bin/env python
# -*- coding: utf-8 -*-


from optparse import OptionParser

import os
import time
import pymongo
import logging


__version__ = '0.0.1'

logger = logging.getLogger("seaoo-cracker")


def parse_opt():
    """Parse the program options."""
    parser = OptionParser()
    parser.add_option('-f', '--forever',
                      dest='forever',
                      help='Run the script forever.',
                      action='store_true',
                      default=False)
    parser.add_option('-i', '--interval',
                      dest='interval',
                      help='Interval to check the pdf database.',
                      metavar='INTERVAL',
                      action='store',
                      type='int',
                      default='600')
    return parser.parse_args()


def do_work():
    DATA_DB = os.environ['DATA_DB']
    connection = pymongo.Connection(DATA_DB)
    db = connection.seaoo
    notices = db.notices
    print notices.count()


def start(forever=False, interval=10*60):
    """Start the script forever or not."""
    if not forever:
        do_work()
        return

    while True:
        try:
            do_work()
            time.sleep(interval)
        except KeyboardInterrupt, err:
            raise err
        except Exception, err:
            logger.debug('ERROR: ' + str(err))


def main():
    """Get the options and actually start the script"""
    options, args = parse_opt()
    start(options.forever, options.interval)


if __name__ == '__main__':
    main()
