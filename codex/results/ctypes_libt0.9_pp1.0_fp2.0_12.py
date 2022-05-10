import ctypes
ctypes.CDLL('libc.so.6', ctypes.RTLD_GLOBAL)
# End ctypes.CDLL inject

import threading
import logging

import iot_logging
import iot_device
import iot_protocol
import iot_client
import iot_utils

logger = logging.getLogger(__name__)


def main():
    random_id = iot_utils.random_id()
    channel = iot_utils.get_channel()

    device = iot_device.IoTDevice(random_id, channel)
    protocol = iot_protocol.IoTProtocol(device)
    client = iot_client.IoTClient(protocol)
    client.connect()

    try:
        while True:
            old_value = device.set_number(33)
            logger.info('Value is {}'.format(old_value))
            time.sleep(1)
    except KeyboardInterrupt:
        logger.info('Cleaning up')

    client.close()
    device.close()
