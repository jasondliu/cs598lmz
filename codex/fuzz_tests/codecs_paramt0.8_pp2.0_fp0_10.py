import codecs
codecs.register_error('essentia_replace', essentia_replace)

def extract_features(filename):
    audio = essentia.standard.MonoLoader(filename=filename)()
    #audio = essentia.standard.EqloudLoader(filename=filename)()
    audio = essentia.standard.Resample(inputSampleRate=44100, outputSampleRate=16000, quality=1)(audio)
    # audio = essentia.standard.Resample(inputSampleRate=44100, outputSampleRate=22050, quality=1)(audio)
    # audio = essentia.standard.Resample(inputSampleRate=22050, outputSampleRate=11025, quality=1)(audio)
    # audio = essentia.standard.Resample(inputSampleRate=11025, outputSampleRate=16000, quality=1)(audio)
    # audio = essentia.standard.EqualLoudness()(audio)
    lowlevel = essentia.standard.LowLevelSpectralExtractor(frameSize=1024, hopSize=512, sampleRate=16000)(audio)
    loud
