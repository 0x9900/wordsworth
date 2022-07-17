#!/usr/bin/env python3
#
import sys

from setuptools import setup, find_packages

import gen_cw

__doc__ = gen_cw.__doc__
__version__ = gen_cw.__version__

__author__ = "Fred C. (W6BSD)"
__license__ = 'BSD'

py_version = sys.version_info[:2]
if py_version < (3, 5):
  raise RuntimeError('gen_cw requires Python 3.5 or later')

def readme():
  """Read and return the content of the README.md file"""
  with open('README.md') as fdi:
    return fdi.read()

setup(
  name='wordsworth',
  version=__version__,
  description='Wordsworth Morse code exercises for fldigi',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='https://0x9900.com/learning-cw/',
  project_urls = {
    'Source': 'https://github.com/0x9900/wordsworth/',
    'Tracker': 'https://github.com/0x9900/wordsworth/issues',
  },
  license=__license__,
  author=__author__,
  author_email='w6bsd@bsdworld.org',
  # py_modules=['gen_cw'],
  entry_points={
    'console_scripts': ['wordsworth = gen_cw:main'],
  },
  packages=find_packages(),
  include_package_data=True,
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
