#!/usr/bin/env python

from distutils.core import setup  

setup(name='qiniucmd',  
    version = '1.0',  
    packages = [
    'qiniu',
    'qiniu.services',
    'qiniu.services.storage',
    'qiniu.services.processing',
    ],
    scripts = ['qiniucmd'],
    description = 'Command line tool for managing Qiniu Resource Storage',
    long_description = 'qiniucmd is a command line tool for uploading,retrieving and managing data in QiNiu Resource Storage.',  
    author = 'Colynn Liu',
    author_email = 'colynnliu@foxmail.com',  
    url = 'http://github.com/colynn',  
    py_modules = ['qiniucmd'],  
   )
