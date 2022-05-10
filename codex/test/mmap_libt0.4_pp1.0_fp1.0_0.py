import mmap

def get_cpu_temp():
    with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
        temp = f.read()
        temp = float(temp) / 1000
        return temp

def get_gpu_temp():
    try:
        res = subprocess.check_output(["/opt/vc/bin/vcgencmd", "measure_temp"])
        return float(res.decode("UTF-8").replace("temp=", "").replace("'C\n", ""))
    except:
        return 0

def get_cpu_usage():
    try:
        res = open("/proc/stat", "r").readline()
        res = res.replace("cpu ", "").split(" ")
        total = sum([float(res[i]) for i in range(len(res))])
        idle = float(res[3])
        return str(int(100 * (1 - idle / total)))
    except:
        return "?"

