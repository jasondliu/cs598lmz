import mmap
import tempfile
import unittest

import pytest

from kafka import (
    KafkaClient,
    SimpleProducer,
    SimpleConsumer,
    create_message,
    create_gzip_message,
    create_snappy_message,
    create_lz4_message
)
from kafka.common import (
    OffsetRequest, OffsetCommitRequest, OffsetFetchRequest,
    OffsetOutOfRangeError, UnknownTopicOrPartitionError, NotLeaderForPartitionError,
    FailedPayloadsError,
    FailedPayload, ChecksumError, ConnectionError, BufferUnderflowError,
    InvalidMessageError, UnknownCodecError
)
from kafka.consumer import SimpleConsumer as NewSimpleConsumer
from kafka.structs import OffsetAndMessage, TopicAndPartition
