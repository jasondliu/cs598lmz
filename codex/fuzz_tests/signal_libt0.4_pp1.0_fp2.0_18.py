import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Create an empty model
model = QgsModel()

# Create the modeler algorithm
modeler_algorithm = QgsProcessingModelAlgorithm()

# Add an input parameter
param = QgsProcessingParameterString(
    'INPUT',
    'Input layer',
    defaultValue=None
)
param.setMetadata({
    'widget_wrapper': {
        'class': 'processing.gui.wrappers_postgis.StringListWidgetWrapper'
    }
})
modeler_algorithm.addParameter(param)

# Add an output parameter
param = QgsProcessingParameterString(
    'OUTPUT',
    'Output layer',
    defaultValue=None
)
param.setMetadata({
    'widget_wrapper': {
        'class': 'processing.gui.wrappers_postgis.StringListWidgetWrapper'
    }
})
modeler_algorithm.addParameter(param)

# Add an algorithm to the model
alg = Qgs
