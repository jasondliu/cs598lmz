import gc, weakref
#from .pymir.audio.signal import Signal

class AudioSegment():
    def __init__(self, signal, start_time, end_time, label=None, parent=None, id=None, **kwargs):
        """
        An object representing a segment of an audio file.

        Parameters
        ----------
        signal : :class:`Signal`
            The :class:`Signal` containing the audio data
        start_time : float
            The start time of the segment (in seconds)
        end_time : float
            The end time of the segment (in seconds)
        label : string, optional
            A label to apply to the segment.
        parent : :class:`AudioSegment`, optional
            A pointer to the parent of this segment.  If this is ``None``, it
            means that this is the root segment of a :class:`AudioSegmentList`.
        """

        self.signal = signal
        self.start_time = start_time
        self.end_time = end_time
        self.label = label
