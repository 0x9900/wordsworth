## Gen Wordsworth CW

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

You can install this program from the source located on my [github]
account. If you already have your Python environment set up, the
easiest way is by using `pip` with the following command:

    $ pip install gen-cw

If you set the environment variable `CALL_SIGN` with your call sign,
gen_cw will use it in the sequences of words generated. Set that
variable permanently to your `.bashrc` or `.zshrc` file depending on
the type of shell you are using.

   $ export CALL_SIGN=W6BSD

## Usage

If you are running this program on macOS, it will automatically copy
the sequence of words into your clipboard buffer. You simply need to
paste it into [fldigi][4].

### Example:

    $ gen_cw --repeat 4 --spaces 10 --dataset abbrevs



It is possible to run this program as an [fldigi][4] macro. Every time
you click on the macro. The CW exercise will automatically appear in
your fldigi transmit window.

### Example of fldigi macro:

    <TX>
    <EXEC>/usr/local/bin/gen_cw --repeat 4 --spaces 5</EXEC>
    <RX>


[1]: misc/QST-Wordsworth.pdf
[2]: https://vimeo.com/523481792
[3]: https://github.com/0x9900/wordsworth
[4]: http://www.w1hkj.com
