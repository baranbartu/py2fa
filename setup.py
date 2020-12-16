#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

VERSION = '0.0.1'

setup(
    name='py2fa',
    version=VERSION,
    description='Command Line OTP Manager',
    long_description=README,
    url='https://github.com/baranbartu/py2fa',
    download_url='https://github.com/baranbartu/py2fa/tarball/%s' % VERSION,
    author='Baran Bartu Demirci',
    author_email='bbartu.demirci@gmail.com',
    license='MIT',
    keywords='otp 2fa authenticator',
    packages=find_packages(),
    entry_points={
        'console_scripts': ['py2fa = py2fa.cli:main']
    },
    install_requires=[
        'pyotp==2.4.1',
        'keyring==21.5.0',
        'pyperclip==1.8.1',
    ]
)
