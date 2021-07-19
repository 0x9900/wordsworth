#!/usr/bin/env python
#
# (C) 2021 Fred C. (W6BSD)
# https://github.com/0x9900/gen_wordsworth
#

"""%(prog)s [options]

Generate a sequence of words choosen from different dataset, that you
can copy into fldigi to help you learn morse code.
The dataset can be one of serveral from the following list:
  - abbrevs
  - alpha
  - common_names
  - common_words
  - connectives
  - numbers
  - pro_codes
  - punctuation

Example:

    $ gen_cw --repeat 4 --spaces 10 --dataset abbrevs

If you are running this program on MacOS it will automatically copy
sequence of words into your clipboard buffer. You just need to paste
it into fldigi.

It is possible to run this program as an fldigi macro. Every time you
click on the macro the cw exercise will automatically appear into your
fldigi transmit window.

Example:
    <TX>
    <EXEC>/usr/local/bin/gen_cw --repeat 4 --spaces 5</EXEC>
    <RX>

"""

import argparse
import string
import sys

from random import shuffle
from subprocess import Popen, PIPE

SPACES = 10
REPEAT = 4
NB_WORDS = 40

DATASET = {
  "ALPHA": list(string.ascii_uppercase),
  "NUMBERS": list(string.digits),
  "CONNECTIVES": None,
  "COMMON_NAMES": [
    'AL', 'ALAN', 'ALEX', 'ANDY', 'ART', 'BERT', 'BILL',
    'BOB', 'CARL', 'CHAS', 'CHRIS', 'DAN', 'DAVE', 'DICK',
    'DON', 'DOUG', 'ED', 'FRED', 'GARY', 'GENE', 'GEORGE',
    'GREG', 'GUS', 'JACK', 'JC', 'JEFF', 'JERRY', 'JESSIE',
    'JIM', 'JOE', 'JOHN', 'JON', 'JUAN', 'KEN', 'LARRY',
    'MIKE', 'OLEG', 'PAT', 'PAUL', 'PETE', 'PHIL', 'RICH',
    'RICK', 'RON', 'SCOTT', 'SERGE', 'STEVE', 'TED', 'TIM',
    'TOM', 'TONY', 'VLAD'
  ],
  "PUNCTUATION": [
    '$', "'", "(", ")", ",", "-", ".", "/", ":", ";", "?", "@", "!"
  ],
  "PRO_CODES": [  # Fldigi pro-codes
    "~", "%", "&", "+", "=", "{", "}", "<", ">", "[", "]"
  ],
  "ABBREVS": [
    "QRL?", "QRM", "QRN", "QRS", "QRT", "QRZ", "QSL", "QSO",
    "QSY", "QTH", "QRX", "ABT", "AGE", "ANT", "BEAM", "BK",
    "QRP", "AGN", "C", "CL", "CPY", "CQ", "CUL", "DE",
    "DX", "ES", "EL", "FB", "HI", "HW?", "HR", "K", "=", "<",
    "%", ">", "LID", "LOOP", "NAME", "OM", "OP", "PKT", "PSE",
    "R", "RPT", "RST", "RIG", "TEMP", "TEST", "TU", "TKS",
    "TNX", "VERT", "WATT", "WX", "YAGI", "YRS", "73", "88",
    "?", "/", "VY", "YL", "XYL", "MY", "UR", "IS", "QSB",
    "QRQ", "HVE", "HPE", "BEST", "SSB", "PHONE"
  ],
  "COMMON_WORDS": [
    'I', 'WITH', 'YOU', 'THEY', 'ITS', 'THEN', 'ME', 'SEE',
    'THIS', 'WE', 'AND', 'OTHER', 'US', 'BECAUSE', 'BE',
    'THESE', 'DAY', 'SHE', 'SOME', 'FROM', 'COULD', 'IT',
    'ONLY', 'HIS', 'TIME', 'TWO', 'LOOK', 'ONE', 'SO', 'YEAR',
    'BUT', 'KNOW', 'EVEN', 'AN', 'IN', 'BACK', 'ALSO', 'ANY',
    'AFTER', 'HIM', 'A', 'OVER', 'WOULD', 'IF', 'HER', 'USE',
    'INTO', 'OUT', 'BY', 'WHICH', 'NOW', 'MAKE', 'THAT',
    'WILL', 'WELL', 'WORK', 'HE', 'AS', 'ON', 'COME', 'TO',
    'GIVE', 'NOT', 'MY', 'THEIR', 'HOW', 'TAKE', 'CAN', 'WAY',
    'NEW', 'FOR', 'OR', 'WANT', 'PERSON', 'WHEN', 'GO', 'THEM',
    'SAY', 'FIRST', 'NO', 'AT', 'DO', 'THERE', 'WHAT', 'JUST',
    'LIKE', 'OUR', 'THE', 'YOUR', 'HAVE', 'THAN', 'MOST',
    'THINK', 'GOOD', 'GET', 'ABOUT', 'WHO', 'UP', 'OF', 'ALL'
  ],
}


def read_dict(dict_name):
  """Read words from a file (used to read os dictionaries)"""
  words = []
  try:
    with open(dict_name, 'r') as fdi:
      words = {w.strip().upper() for w in fdi}
      words = [w for w in words if len(w) <= 5]
  except IOError as err:
    print(err, file=sys.stderr)

  return words


def pbcopy(buffer):
  """If MacOS sent the CW exercise to the clipboard"""
  if sys.platform != "darwin":
    return
  with Popen('pbcopy', env={'LANG': 'en_US.UTF-8'}, stdin=PIPE) as process:
    process.communicate(buffer.encode('utf-8'))
  print('*** The CW excercise has been copied into your clipboard ***',
        file=sys.stderr, end="\n\n")


def type_dataset(parg):
  """check if the dataset argument is valid. lazy download the
  connectives from the OS dictionary when needed
  """
  parg = parg.upper()
  if parg not in DATASET:
    raise argparse.ArgumentTypeError('Argument error')

  if parg == 'CONNECTIVES':
    DATASET['CONNECTIVES'] = read_dict('/usr/share/dict/connectives')

  return parg

## ------------

def main():
  """This is where we make the sausage"""
  call_sign = os.getenv('FLDIGI_MY_CALL', 'W1AW')
  parser = argparse.ArgumentParser(usage=__doc__)
  parser.add_argument("-s", "--spaces", type=int, default=SPACES,
                      help="Spacing between each words [default: %(default)s]")
  parser.add_argument("-n", "--nb-words", type=int, default=NB_WORDS,
                      help="Number of words to select")
  parser.add_argument("-r", "--repeat", type=int, default=REPEAT,
                      help="repeatitions [default: %(default)s]")
  parser.add_argument("-d", "--dataset", nargs="+", type=type_dataset,
                      default="abbrevs", help="See --help for the list of datasets [default: %(default)s]")
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