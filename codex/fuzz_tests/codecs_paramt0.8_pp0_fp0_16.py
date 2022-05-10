import codecs
codecs.register_error('StrictOctalEscape', codecs.StrictOctalEscape)

def convert_text_to_matrix(text, size, emsize=14, encoding='utf-8'):
    """
    Convert a text to a matrix of characters.

    Parameters
    ----------
    text : str
        Text to be converted to matrix.
    size : tuple of two int
        Size of the output matrix.
    emsize : int
        Size of character in pixels.
    encoding : str
        Text encoding.

    Returns
    -------
    matrix : array
        Array of characters
    """
    font = ImageFont.truetype('/usr/share/fonts/truetype/droid/DroidSans.ttf',
                              size=emsize)
    w, h = size
    text = text.decode(encoding).encode('unicode-escape').decode('string-escape')
    text = text[:w * h]
    matrix = []
    i = 0
    for _ in range(h):
        line = []
        for
