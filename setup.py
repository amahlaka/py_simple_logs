#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from setuptools import setup, find_packages
import sys
import warnings

dynamic_requires = []

version = 0.1

setup(
    name='Simple_logs',
    version=0.1,
    author='Arttu Mahlakaarto',
    author_email='Arttu.mahlakaarto@gmail.com',
    url='http://github.com/amahlaka/',
    packages=find_packages(),
    download_url='https://github.com/amahlaka//tarball/0.1',
    scripts=[],
    description='Wrapper that simplifies logging',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    include_package_data=True,
    zip_safe=False,
)