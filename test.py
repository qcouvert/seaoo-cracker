#! /usr/bin/python

from seao.Seao import Seao
from seao.errors import NotLoggedError

import os


USER = ''
PASW = ''
PDFID = 'a18c621b-9bce-49ee-8eeb-d43c924bc3df'


def main():
    global USER, PASW, PDFID
    seao = Seao(USER, PASW)
    pdf = seao.get_file(PDFID)
    with open('tmp.pdf', 'w+') as f:
        f.write(pdf)
    seao.logout()


if __name__ == '__main__':
    main()
