=====================================
 MIURA server: Morpheme I U Regexp A
=====================================

MIURA is a regular expression matcher for morpheme sequences.
This program is a simple web server to use MIURA from a browser.


Requirement
===========

- Python 2.7
- miura
- tornado


Install
=======

::

   $ pip install miuraserver


If you want to install it from its source, use `setup.py`.

::

   $ python setup.py install


Usage
=====

::

   usage: miuraserver [-h] [-p PORT] FILE

MIURA: morpheme i u regexp a

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
