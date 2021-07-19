## Gen Wordsworth

George Allison K1IG described a methodology "head copy" morse
code. High-speed operators who copy in their heads at speed greater
than 40 WPM have learned to process CW by hearing entire words.

The Wordsworth method is a variant of the Farnsworth method which
sends individual letters at a high speed. The Wordsworth’s method send
words at your target speed with long spacing between each words. You
reduce the number of spaces as your proficiency increases.

For more information you can read George's article, published on the
[QST magazine][1] on his method.

You can also watch the George's presentation at [QSO Today][2]

## Usage

If you are running this program on MacOS it will automatically copy
sequence of words into your clipboard buffer. You just need to paste
it into fldigi.

### Example:

    $ gen_cw --repeat 4 --spaces 10 --dataset abbrevs



It is possible to run this program as an fldigi macro. Every time you
click on the macro the cw exercise will automatically appear into your
fldigi transmit window.

### Example of macro:

    <TX>
    <EXEC>/usr/local/bin/gen_cw --repeat 4 --spaces 5</EXEC>
    <RX>


[1]: misc/QST-Wordsworth.pdf
[2]: https://vimeo.com/523481792
