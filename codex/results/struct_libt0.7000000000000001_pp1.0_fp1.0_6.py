import _struct

from . import constants
from . import utils
from . import exceptions

from . import (
    audio,
    video,
    subtitle,
    attachment,
    chapter,
    cue,
    tag,
    webvtt,
    stats,
)


class Track:
    def __init__(
        self,
        track_type,
        codec,
        id,
        codec_params,
        default,
        forced,
        language,
        name,
        properties,
        tags,
        default_track,
        lacing,
        min_cache,
        max_cache,
        timecode_scale,
        max_block_additional_id,
        base_data_offset,
        content_encodings,
        encodings,
        decoders,
        codec_delay,
        seek_pre_roll,
        track_overlay,
        codec_private,
        codec_state,
    ):
        self.codec = codec
        self.codec_delay = codec_delay
        self.codec_
