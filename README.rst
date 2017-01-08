===============================
instaread
===============================

.. image:: https://badge.fury.io/py/instaread.png
    :target: http://badge.fury.io/py/instaread

.. image:: https://travis-ci.org/anhdat/instaread.png?branch=master
        :target: https://travis-ci.org/anhdat/instaread


Fast and minimal CLI application to read Instapaper from terminal

Usage
--------

  instaread [--archive][--force]           Read the last unread item. Use with '--archive' to show your commitment.
  instaread putback                        Unarchive last archived item. Use after '--archive' to take back you overconfidence.
  instaread folders                        List all folders
  instaread unreads                        List all unread items
  instaread archiveds                      List all archived items
  instaread -h | --help
  instaread --version

Options:
  -h --help     Show this screen.
                Open last unread
  --archive     Open last unread and archive it
  --force       Force refresh token and secret
  --version     Show version.

Installation
------------

`pip3 install instaread`


Requirements
------------

- Python >= 3.3

License
-------

MIT licensed. See the bundled `LICENSE <https://github.com/anhdat/instaread/blob/master/LICENSE>`_ file for more details.
