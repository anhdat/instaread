#!/usr/bin/env python
'''instaread

Usage:
  instaread [--archive]
  instaread folders
  instaread -h | --help
  instaread --version

Options:
  -h --help     Show this screen.
                Open last unread
  --archive     Open last unread and archive it
  --version     Show version.
'''
from docopt import docopt
import sys
from .instaread import AppException
from .instaread import login
from .instaread import sync
from .instaread import read_last_synced_bookmark
from .instaread import copy_read_assets
from .instaread import folders

__version__ = "0.1.1"
__author__ = "Dat Truong"
__license__ = "MIT"


def main():
    '''Main entry point for the instaread CLI.'''
    args = docopt(__doc__, version=__version__)
    should_archive = args['--archive']
    login()

    if args['folders']:
        folders()
        return

    copy_read_assets()
    sync()
    read_last_synced_bookmark(should_archive=should_archive)


if __name__ == '__main__':
    try:
        main()
    except AppException as err:
        print("{}: {}".format(type(err).__name__, err))
        sys.exit()
