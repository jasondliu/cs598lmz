import lzma
lzma.CHECK_NONE # Silence pylint false positive

import pytest

from screener import config, decoder

def lzma_decoder_patch(working_dir, p, a=False):
    working_dir.join("dont-parse-me.zst").write("qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq")
    return decoder.LZMA(working_dir, p, a)

def test_lzma_decoder_can_read(working_dir):
    """Test that LZMA can read files."""
    with pytest.raises(lzma.LZMAError):
        p = config.Config("", -1, "", "")
        with decoder.LZMA(working_dir, p) as reader:
            reader.read("does-not-exist.zst")
    with pytest.raises(OSError):
       
