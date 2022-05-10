fn = lambda: None
# Test fn.__code__
_test_fn.__code__
#
# This will load all of the classes, in any of the modules, contained in all of the packages
# listed above (and their sub-packages)
# This is the same as saying:
## from lsst.pipe.tasks.characterizeImage import CharacterizeImageTask
## from lsst.pipe.tasks.detection import DetectCoaddSourcesTask, DetectCoaddSourcesConfig, \
##     MergeDetectionsTask, MergeDetectionsConfig
## from lsst.meas.astrom import ApplyExternalSkyWcsTask, ApplyExternalSkyWcsConfig
#
config.processCcd.load(__name__)

config.charImage.doApCorr=False
config.charImage.repair.doCosmicRay=True
config.charImage.repair.cosmicray.nCrPixelMax=100000
config.charImage.repair.cosmicray.cond3_fac2=0.4
config.charImage.repair.cosmicray.cond3_fac1=0.3
config.charImage.repair.cosmicray.cond3
