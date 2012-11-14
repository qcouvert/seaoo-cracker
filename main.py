#!/usr/bin/env python
# -*- coding: utf-8 -*-


import time
import pymongo


def do_work():
    pass


def main():
    while True:
        try:
            do_work()
            time.sleep(10 * 60)
        except KeyboardInterrupt, err:
            raise err
        except Exception, err:
            print 'ERROR: ' + str(err)


if __name__ == '__main__':
    main()
