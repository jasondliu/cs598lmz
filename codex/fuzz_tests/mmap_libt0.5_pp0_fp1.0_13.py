import mmap
import os
import sys
import time
import traceback

from pyVmomi import vim

from common import get_args
from common import get_obj
from common import get_si
from common import task_wait
from common import vm_power_state

args = get_args()

si = get_si(args.host, args.user, args.password, args.port)

vm = get_obj(si, [vim.VirtualMachine], args.vm_name)

if vm_power_state(vm) != 'POWERED_OFF':
    print('The VM has to be powered off to run this script.')
    sys.exit(1)

dev_changes = []
for dev in vm.config.hardware.device:
    if isinstance(dev, vim.vm.device.VirtualDisk) and \
            dev.backing.fileName == '[%s]' % vm.config.files.vmPathName:
        dev_changes.append(vim.vm.device.VirtualDeviceSpec(
            device=dev,
            operation=vim.vm.device
