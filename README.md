## Wordsworth CW

George Allison K1IG described a methodology "head copy" morse
code. High-speed operators who copy in their heads at a speed greater
than 40 WPM have learned to process CW by hearing entire words.

The Wordsworth method is a variant of the Farnsworth method, which
sends individual letters at high speed. Wordsworth's method sends
words at your target speed with long spacing between each word. You
reduce the number of spaces as your proficiency increases.

For more information, you can read George's article, published on the
[QST magazine][1] on his method.

You can also watch George's presentation at [QSO Today][2]

## Installation

You can install this program from the source located on my [github][3]
account. If you already have your Python environment set up, the
easiest way is by using [pip][4] with the following command:

    $ pip install wordsworth

If you set the environment variable `CALL_SIGN` with your call sign,
wordworth will use it in the sequences of words generated. Set that
variable permanently to your `.bashrc` or `.zshrc` file depending on
the type of shell you are using.

    $ export CALL_SIGN=W6BSD

## Usage

If you are running this program on macOS, it will automatically copy
the sequence of words into your clipboard buffer. You simply need to
paste it into [fldigi][5].

### Example:

    $ wordworth --repeat 4 --spaces 10 --dataset abbrevs



It is possible to run this program as an [fldigi][5] macro. Every time
you click on the macro. The CW exercise will automatically appear in
your fldigi transmit window.

### Example of fldigi macro:

    <TX>
    <EXEC>/usr/local/bin/wordworth --repeat 4 --spaces 5</EXEC>
    <RX>

## Datasets

The datasets are:

 - "abbrevs"      abbreviations used in CW
 - "alpha"        alphabet [A-Z]
 - "combination"  most Frequent letters combinations
 - "connectives"  connective words
 - "names"        common first names
 - "numbers"      numbers from 0 - 99
 - "pro_codes"    ham radio pro-codes <AR>, <AS>, <BT>, <SK>, etc
 - "punctuation"  all the punctuation used in Morse
 - "words"        most common words


To use a specific dataset use the argument `--dataset` followed by the
names of the dataset you want to learn.

### Example

    $ wordworth --nb-words 50 --repeat 3 --dataset alpha numbers abbrevs

In this example the program will chose 50 words from the 3 datasets
alpha, numbers, abbrevs. Each word will be repeated 3 times.


[1]: misc/QST-Wordsworth.pdf
[2]: https://vimeo.com/523481792
[3]: https://github.com/0x9900/wordsworth
[4]: https://pypi.org/project/wordsworth/
[5]: http://www.w1hkj.com
