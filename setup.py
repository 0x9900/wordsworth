#!/usr/bin/env python3
#
import sys

from setuptools import setup, find_packages

import gen_cw

__doc__ = gen_cw.__doc__

__author__ = "Fred C. (W6BSD)"
__version__ = '0.1.4'
__license__ = 'BSD'

py_version = sys.version_info[:2]
if py_version < (3, 5):
  raise RuntimeError('gen_cw requires Python 3.5 or later')

def readme():
  with open('README.md') as fd:
    return fd.read()

setup(
  name='gen_cw',
  version=__version__,
  description='Wordsworth Morse code exercises for fldigi',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='https://github.com/0x9900/wordsworth/',
  license=__license__,
  author=__author__,
  author_email='w6bsd@bsdworld.org',
  py_modules=['gen_cw'],
  entry_points = {
    'console_scripts': ['gen_cw = gen_cw:main'],
  },
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.5',
    'Topic :: Communications :: Ham Radio',
  ],
)
