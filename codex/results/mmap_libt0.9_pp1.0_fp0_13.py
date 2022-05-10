import mmap
import os.path

from pydocx.styles import get_styles
from pydocx.util import Docx2Html


def fix_paragraphs(text):
    return text.replace('<p><p>', '<p>')


def get_content(docx_file):
    """
    Returns the HTML content from a docx file
    """
    try:
        content = Docx2Html(docx_file).get_html()
    except Exception:
        # There are a couple of cases that pydocx doesn't handle.
        #
        # For example:
        #
        # * Images that have no associated file
        #
        #     <pack:part pack:name="/word/media/image1.jpeg"
        #                pack:contentType="image/jpeg"/
        #
        # * Footnotes with malformed xml
        #
        #     word/footnotes.xml...<w:footnote w:id="-1"
        #        ...
        #     word/footnotes.xml...</w:
