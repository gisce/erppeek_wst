#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='ERPPeek-WST',
    version='0.2.4',
    license='BSD',
    description='Erppeek extension for using web services transactions with ws_transactions module',
    long_description='',
    url='http://github.com/gisce/erppeek_wst',
    author='GISCE-TI, S.L.',
    author_email='devel@gisce.net',
    install_requires=['erppeek>=1.7', 'six'],
    py_modules=['erppeek_wst'],
    platforms='any',
    keywords="openerp xml-rpc xmlrpc",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
