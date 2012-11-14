#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import time
import pymongo


def do_work():
    pass


def main():
    DATA_DB = os.environ['DATA_DB']
    connection = pymongo.Connection(DATA_DB)
    db = connection.seaoo
    notices = db.notices
    print notices.count()
    #while True:
    #    try:
    #        do_work()
    #        time.sleep(10 * 60)
    #    except KeyboardInterrupt, err:
    #        raise err
    #    except Exception, err:
    #        print 'ERROR: ' + str(err)


if __name__ == '__main__':
    main()
