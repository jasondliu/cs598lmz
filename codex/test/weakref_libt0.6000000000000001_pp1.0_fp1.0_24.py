import weakref

import numpy

from . import AudioBuffer
from . import AudioStream

def _py_audio_open(f, mode, format, channels, rate, frames_per_buffer,
                   stream_callback, start, input, output, stream_callback_args,
                   **kwargs):
    """
    Open a stream for playback or recording.

    Returns a PortAudio Stream Wrapper.
    """
    if f is not None:
        raise ValueError("files are not supported")
    if input and output:
        raise ValueError("cannot open a device for simultanous "
                         "input and output")
    if input:
        direction = pa.Pa_StreamCallbackFlags.input
    else:
        direction = pa.Pa_StreamCallbackFlags.output

    if stream_callback is None:
        if not _py_audio_is_format_pcm(format):
            raise ValueError("only PCM formats are supported "
                             "without a stream callback")
        samples = numpy.zeros(rate, dtype=format)
