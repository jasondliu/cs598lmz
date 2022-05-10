import socket
socket.if_indextoname(1)`
```

Here is some other information we can find about the local system:
```python
import psutil
print("CPU count: [{}]".format(psutil.cpu_count(logical=True)))
print("CPU percent [idle]: {}".format(psutil.cpu_percent(interval=None, percpu=True)))
print("Available Memory: {:.2f}Gb".format(psutil.avail_phymem() / (1024*1024*1024)))
print("Total Memory: {:.2f}Gb".format(psutil.total_phymem() / (1024*1024*1024)))
print("Partitions")
for partition in psutil.disk_partitions(all=True):
	print("  {}: {} {:.2f}Gb ({:.2f}Gb free)".format(partition.device, partition.mountpoint,
											(psutil.disk_usage(partition.device).total / (1024*1024*1024)),
											(ps
