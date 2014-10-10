==================================================
 MREP server: Morpheme Regular Expression Printer
==================================================

MREP is a regular expression matcher for morpheme sequences.
This program is a simple web server to use MREP from a browser.


Requirement
===========

- Python 2.7
- mrep
- tornado


Install
=======

::

   $ pip install mrepserver


If you want to install it from its source, use `setup.py`.

::

   $ python setup.py install


Usage
=====

::

   usage: mrepserver [-h] [-p PORT] FILE

MREP server: morpheme regular expression printer

positional arguments:
  :`FILE`:                  data file

optional arguments:
  -h, --help            show this help message and exit
  -p PORT, --port PORT  port number


License
-------

This program is distributed under the MIT license.


Copyright
---------

\(c) 2014, Yuya Unno.
