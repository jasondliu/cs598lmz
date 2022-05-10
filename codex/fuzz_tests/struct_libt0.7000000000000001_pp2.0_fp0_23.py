import _struct
import wave

import sounddevice as sd


def int16_to_float32(samples, times=None, samplerate=None, subtype='PCM_16'):
    """Convert an array with 16-bit integers to floating point numbers.

    This is an inverse of `soundfile.blocks.float32_to_int16()`.
    """
    if len(samples.shape) != 1:
        raise ValueError('Only 1-D arrays supported.')
    if samples.dtype != 'int16':
        raise ValueError('Only 16-bit integer arrays supported.')
    if subtype not in ('PCM_16', 'PCM_24', 'PCM_32', 'PCM_U8'):
        raise ValueError('Only signed integer types supported.')
    if subtype != 'PCM_16':
        raise RuntimeError('Only PCM_16 supported, not %s.' % subtype)
    f = _struct.Struct('<%dh' % len(samples)).unpack
    samples = [sample / 32768 for sample in f(samples
