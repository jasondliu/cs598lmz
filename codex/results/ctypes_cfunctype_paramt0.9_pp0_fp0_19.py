import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int)


class PrintLatexListener(LatexListener):
    def __init__(self, codeOutput):
        from .translator import LatexTranslator
        self._latexTranslator = LatexTranslator()
        self._codeOutput = codeOutput

    def enterLatex(self, latexContext):
        self._codeOutput(self._latexTranslator.translate(latexContext))

    def exitLatex(self, ctx):
        pass
