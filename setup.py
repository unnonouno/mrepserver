#!/usr/bin/env python

from setuptools import setup

requires = [
    'miura',
    'tornado',
    ]

setup(
    name='miuraserver',
    version='0.1.0',
    description='MIURA server: pattern matcher for morpheme sequences',
    author='Yuya Unno',
    author_email='unnonouno@gmail.com',
    packages=['miuraserver',
              ],
    scripts=[
        'scripts/miuraserver',
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

