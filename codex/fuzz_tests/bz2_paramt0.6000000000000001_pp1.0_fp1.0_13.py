from bz2 import BZ2Decompressor
BZ2Decompressor.decompress = decompress

from .source import Source
from .utils import get_module_attr

class Pipeline(object):
    def __init__(self, config):
        self.config = config
        self.sources = []
        self.sinks = []

    def start(self):
        for source in self.sources:
            source.start()

    def stop(self):
        for source in self.sources:
            source.stop()
        for sink in self.sinks:
            sink.stop()

    def add_sources(self):
        sources = self.config.get('sources', [])
        for source_config in sources:
            source = self._create_source(source_config)
            self.sources.append(source)

    def add_sinks(self):
        sinks = self.config.get('sinks', [])
        for sink_config in sinks:
            sink = self._create_sink(sink_config)
            self.sinks.append(sink)

    def _create_source(
