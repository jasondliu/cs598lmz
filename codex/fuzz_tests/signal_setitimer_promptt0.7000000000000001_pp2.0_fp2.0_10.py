import signal
# Test signal.setitimer
import time
signal.setitimer(signal.ITIMER_VIRTUAL, 0.01)
# t = time.time()
# print(t)
# time.sleep(0.01)
print("Exiting...")

# import os
# import platform
# import re
# from subprocess import check_output
#
#
# def check_output_decoded(args, *arg, **kwargs):
#     return check_output(args, *arg, **kwargs).decode()
#
#
# if platform.system() == 'Linux':
#     net_io_counters = psutil.net_io_counters(pernic=True)
#     for nic_name, _ in net_io_counters.items():
#         if nic_name != 'lo':
#             break
#     else:
#         raise ValueError('no nic')
#
#     nic_name = nic_name.encode('ascii')
#     with open('/sys/class/net/' + nic_name + '/statistics/tx_
