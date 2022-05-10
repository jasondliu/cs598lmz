import gc, weakref
        self.__dict__['_reaktor'] = reaktor
        self.__dict__['_w_reaktor'] = weakref.ref(reaktor)
        reaktor.__dict__['_outdevices'] = self
        reaktor._outdevices.append(self)
        self.name = reaktor._outdevices.index(self)
        self.synthmaster = SynthMaster('synthmaster')
        self._synthdev = SynthDevice('synthdev')
        self.synthmaster.AddOutputDevice(self._synthdev, self.name)
        self._sampledev = SampleDevice('sampledev')
        self.synthmaster.AddOutputDevice(self._sampledev, self.name)
        self.synthmaster.route = lambda x, y: None
        self.LoopSampler = LoopSampler(self)
        self.SynthOsc = SynthOsc(self)

    def __setattr__(self, atribute, value):
        if atribute in self._reaktor.__dict__
