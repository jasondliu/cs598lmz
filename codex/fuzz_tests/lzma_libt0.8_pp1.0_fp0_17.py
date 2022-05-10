import lzma
lzma._decompressobj = lzma.LZMADecompressor
del lzma

from ._helpers import get_qcschema_formats
from ._helpers import (
    validate_against_jsonschema,
    validate_against_qcschema,
    validate_json_file,
    validate_json_string,
    validate_qc_file,
    validate_qc_string,
    ValidatorBase,
    JSONFormat,
    JSON
)
from ._exceptions import JSONSchemaValidationError, JSONSchemaValueError, JSONSchemaError
from ._exceptions import QCSchemaValidationError, QCSchemaValueError, QCSchemaError
from ._exceptions import ValidatorError


def validate(project, config):
    """
    Validate a project using the configuration provided in config.
    """
    if 'qc_schema' in config:
        validate_against_qcschema(
            config['qc_schema'],
            project
        )
    if 'json_schemas'
