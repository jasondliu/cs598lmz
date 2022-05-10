import socket

from cli.push_log_file import push_file_to_nrel_ftp
from cli.send_email import send_email


def start_up_test():
    """Uses the existing set of test functions to check the network
    configuration, gzip version, and sample interval."""

    network_test_result, network_test_message = network_test()
    gzip_version_result, gzip_version_message = gzip_version()
    sample_interval_result, sample_interval_message = sample_interval()
    test_result_list = [network_test_result, gzip_version_result,
                        sample_interval_result]
    test_message_list = [network_test_message, gzip_version_message,
                         sample_interval_message]
    if all(test_result_list):
        return test_result_list, test_message_list
    else:
        return test_result_list, test_message_list


def network_test():
    """Test the network configuration."""

   
