#!/usr/bin/env python
#
# (C) 2021 Fred C. (W6BSD)
# https://github.com/0x9900/gen_wordsworth
#

"""%(prog)s [options]

Generate a sequence of words chosen from a different dataset that you
can copy into fldigi to help you learn morse code.
The dataset can be one of serveral from the following list:
  - "abbrevs"      abbreviations used in CW
  - "alpha"        alphabet [A-Z]
  - "combination"  most Frequent letters combinations
  - "connectives"  connective words
  - "names"        common first names
  - "numbers"      numbers from 0 - 99
  - "pro_codes"    ham radio pro-codes <AR>, <AS>, <BT>, <SK>, etc
  - "punctuation"  all the punctuation used in Morse
  - "words"        most common words

Example:

    $ wordsworth --repeat 4 --spaces 10 --dataset abbrevs

If you are running this program on macOS, it will automatically copy
the sequence of words into your clipboard buffer. You can paste it into fldigi.

It is possible to run this program as a fldigi macro. Every time you
Click on the macro the CW exercise will automatically appear into your
fldigi transmit window.
"""

__version__ = '0.1.5'

import argparse
import os
import string
import sys

from random import shuffle
from subprocess import Popen, PIPE

try:
  import importlib.resources as importlib_resources
except ImportError:
  # Fall-back importlib_resources for python < 3.7
  import importlib_resources

# The program wordsworth uses the call sign defined in fldigi. When
# running wordsworth in a console, the environment variable "CALL_SIGN"
# will be used. If none of these are defined, this is the call sign
# that will be used.
DEFAULT_CALL = "W1AW"
SPACES = 10
REPEAT = 4
NB_WORDS = 40

DATASET = {
  "ALPHA": list(string.ascii_uppercase),
  "NUMBERS": [str(n) for n in range(0,100)],
  "PUNCTUATION": [
    "$", "'", "(", ")", ",", "-", ".", "/", ":", ";", "?", "@", "!"
  ],
  "PRO_CODES": [                # Fldigi pro-codes
    "~", "%", "&", "+", "=", "{", "}", "<", ">", "[", "]"
  ],
}


def read_dict(dict_name):
  """Read words from files in the 'dicts' directory"""
  words = set()
  filename = dict_name + '.dict'
  wordlist = importlib_resources.read_text(__name__, filename)
  for word in wordlist.splitlines():
    word = word.strip()
    if word.startswith('#'): # remove comments
      continue
    words.add(word)
  return list(words)


def pbcopy(buffer):
  """If MacOS sent the CW exercise to the clipboard"""
  if not sys.stdout.isatty() or sys.platform != "darwin":
    return
  with Popen('pbcopy', env={'LANG': 'en_US.UTF-8'}, stdin=PIPE) as process:
    process.communicate(buffer.encode('utf-8'))
  print('*** The CW excercise has been copied into your clipboard ***', file=sys.stderr)


def type_dataset(parg):
  """check if the dataset argument is valid. lazy download the
  connectives from the OS dictionary when needed
  """
  key = parg.upper()
  if key in DATASET:
    return key

  try:
    DATASET[key] = read_dict(parg)
  except IOError:
    raise argparse.ArgumentTypeError('Dictionary error: {}'.format(parg)) from None

  return key

## ------------

def main():
  """This is where we make the sausage"""
  call_sign = os.getenv('FLDIGI_MY_CALL', os.getenv('CALL_SIGN', DEFAULT_CALL))
  parser = argparse.ArgumentParser(usage=__doc__)
  parser.add_argument("-s", "--spaces", type=int, default=SPACES,
                      help="Spacing between each words [default: %(default)s]")
  parser.add_argument("-n", "--nb-words", type=int, default=NB_WORDS,
                      help="Number of word to select [default: %(default)s]")
  parser.add_argument("-r", "--repeat", type=int, default=REPEAT,
                      help="repeatitions [default: %(default)s]")
  parser.add_argument("-d", "--dataset", nargs="+", type=type_dataset, default="abbrevs",
                      help="See --help for the list of datasets [default: %(default)s]")
  parser.add_argument("--version", action="version", version='%(prog)s {}'.format(__version__))
  opts = parser.parse_args()
  spacing = ' ' * opts.spaces

  if isinstance(opts.dataset, str):
    opts.dataset = [opts.dataset.upper()]

  dataset = (DATASET[d] for d in opts.dataset)
  dataset = list(set(d for sublist in dataset for d in sublist)) # remove duplicates
  shuffle(dataset)

  dataset = dataset * int(1 + opts.nb_words / len(dataset))

  words = ["VVV"]
  for abbrev in dataset[:opts.nb_words]:
    words.extend([abbrev] * opts.repeat)
  words.extend(["DE", call_sign, "K"])

  buffer = spacing.join(words)
  pbcopy(buffer)
  print(buffer, end="\n\n")

if __name__ == "__main__":
  main()
