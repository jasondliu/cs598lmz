import gc, weakref, sys, os
        #     if sys.version_info[0] >= 3:
        #         _int = int
        #     else:
        #         _int = (int, long)
        #     self.assertIsInstance(len(gc.get_referrers(self)), _int)
        #     del self
        #     gc.collect()
        #     self.assertFalse(gc.get_referrers(self))

    def test_set_parent(self):
        from mupdf import ffi, MuPDF
        doc = MuPDF('tests/pdfs/mupdf.pdf')
        page = doc[1]
        self.assertEqual(page.parent, doc)

        # Make sure that we don't have a circular reference.
        # It is important that page.__del__() is called which is
        # why we make sure to delete the page object.
        with self.assertRaises(AttributeError):
            del page
            gc.collect()
            del doc
            gc.collect()


class TestPage(unittest
