from lzma import LZMADecompressor
LZMADecompressor().decompress(...)
</code>
But this is not what I need.
I need to use LZMA SDK (LZMA SDK 9.22 beta).
I tried to use this code:
<code>#include &lt;stdio.h&gt;
#include "lzma.h"

int main(int argc, char *argv[])
{
    FILE *in_file, *out_file;
    lzma_stream strm = LZMA_STREAM_INIT;
    lzma_action action = LZMA_RUN;

    if (argc != 3) {
        printf("Usage: %s &lt;infile&gt; &lt;outfile&gt;\n", argv[0]);
        return 1;
    }

    in_file = fopen(argv[1], "rb");
    out_file = fopen(argv[2], "wb");

    lzma_ret ret = lzma_stream_decoder(&amp;strm, UINT64_MAX, LZMA_CON
