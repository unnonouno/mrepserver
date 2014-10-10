#!/usr/bin/env python

import os
from setuptools import setup

requires = [
    'mrep',
    'tornado',
    ]

def read(name):
    return open(os.path.join(os.path.dirname(__file__), name)).read()

setup(
    name='mrepserver',
    version='0.1.0',
    description='MREP server: morpheme regular expression printer',
    long_description=read('README.rst'),
    author='Yuya Unno',
    author_email='unnonouno@gmail.com',
    url='https://github.com/unnonouno/mrepserver',
    packages=['mrepserver',
              ],
    scripts=[
        'scripts/mrepserver',
    ],
    install_requires=requires,
    license='MIT',
    classifiers = [
        'Operating System :: OS Independent',
        'Environment :: Web Environment',
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',
        'Topic :: Utilities',
    ],
    )

