import socket
import ssl

import pytest
import six

from nassl.legacy_ssl_client import LegacySslClient
from nassl.ssl_client import OpenSslVersionEnum

from sslyze.plugins.openssl_cipher_suites_plugin import Tlsv10ScanCommand, Tlsv11ScanCommand, Tlsv12ScanCommand, \
    Tlsv13ScanCommand
from sslyze.plugins.plugin_base import PluginScanResult
from tests.markers import can_only_run_on_linux_64
from tests.openssl_server import LegacyOpenSslServer, ClientAuthConfigEnum


@pytest.mark.parametrize(
    ('cli_command', 'expected_scan_result_enum'),
    [
        (Tlsv10ScanCommand(), PluginScanResult.SCAN_RESULT_WEAK),
        (Tlsv11ScanCommand(), PluginScanResult.SCAN_RESULT_WEAK),
        (Tlsv12ScanCommand(), PluginScanResult.SCAN_RESULT_OK),
        (Tlsv
