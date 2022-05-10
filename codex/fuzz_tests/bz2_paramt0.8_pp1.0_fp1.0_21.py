from bz2 import BZ2Decompressor
BZ2Decompressor.decompress = BZ2Decompressor.decompress_nonblock
from tarfile import TarFile
TarFile.extractall = TarFile.extractall_nonblock


class CPU(object):
    def freeze(self):
        return False

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


def get_extractor_configuration(config):
    return config.get('extractor', 'extractor')


def get_extractor_config(config):
    extractor_type = get_extractor_configuration(config)
    if extractor_type == 'yolo':
        return YoloExtractorConfig(config)
    raise Exception('Unsupported extractor: ' + extractor_type)


def get_extractor(config):
    extractor_type = get_extractor_configuration(config)
    if extractor_type == 'yolo':
        return YoloExtractor(get_extractor_config(config))
    raise Exception('Unsupported
