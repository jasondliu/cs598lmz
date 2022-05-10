import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Add a custom menu to the image viewer
from lazyflow.operators.generic import OpSubRegion
from lazyflow.operators import OpPixelOperator, OpCompressedCache

from ilastik.applets.dataSelection import DataSelectionApplet
from ilastik.applets.layerViewer.layerViewerGui import LayerViewerGui
from ilastik.applets.layerViewer.layerViewerApplet import LayerViewerApplet
from ilastik.applets.pixelClassification.opPixelClassification import OpPixelClassification
from ilastik.applets.pixelClassification.pixelClassificationGui import PixelClassificationGui
from ilastik.applets.pixelClassification.pixelClassificationApplet import PixelClassificationApplet
from ilastik.applets.thresholdTwoLevels.opThresholdTwoLevels import OpThresholdTwoLevels
from ilastik.applets.thresholdTwoLevels.thresholdTwoLevelsGui import ThresholdTwoLevelsGui
