import weakref

from ufo2ft.featureCompiler import compileFeaturesToString
from ufo2ft.featureWriters.writerBase import WriterBase
from ufo2ft.fontInfoData import getAttrWithFallback
from ufo2ft.util import (
    makeOutputFileName,
    getPathForAttrWithFallback,
    getAttrWithFallback,
    addExtension,
)


class FeatureFileWriter(WriterBase):
    """Writes a feature file with the contents of the UFO's features.fea."""

    name = "featureFileWriter"

    _defaultParams = {
        "layerName": None,
        "featureFilePath": None,
        "featureFileName": None,
        "featureFile": None,
        "featureFileFormat": "fea",
    }

    def __init__(self, params, glyphSet, font):
        super().__init__(params, glyphSet, font)
        self._featureFilePath = None
        self._featureFile = None

    def _getFeatureFilePath(self):
        if self._feature
