import socket
import struct
import sys
import time

import boto3
import botocore
import click
import requests

from . import __version__, DEFAULT_TIMEOUT, DEFAULT_URL, DEFAULT_REGION
from .exceptions import (
    InvalidRegionError,
    NoInstanceError,
    TimeoutError,
    InvalidCredentialsError,
)
from .utils import (
    get_instance_id,
    get_instance_region,
    get_instance_profile,
    get_instance_profile_arn,
    get_role_name_from_arn,
    get_role_name_from_profile,
    get_role_arn_from_profile,
    get_role_arn_from_name,
    get_role_name_from_arn,
    get_role_session_name,
    get_account_id,
    get_account_alias,
    get_credentials,
    get_credentials_from_sts,
    get_credentials_from_iam,
    get_credentials_from_env
