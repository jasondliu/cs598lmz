import mmap
# Test mmap.mmap(0,4096) on gbenga's system to ensure it doesn't raise an error
# Example: https://github.com/ggbaker/embedded-shell/blob/master/embedshell.py
'''
This script will print the remaining time in seconds before a processwith the given PID is killed.
This script also repeatedly prints the CPU, MEM and Command-line of the process with the given PID.

Usage: python3 <PID-of-process> <kill-time>
'''

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python3 <PID-of-process> <kill-time>", file=sys.stderr)
        sys.exit(1)

    pid = sys.argv[1]
    kill_time = int(sys.argv[2]) # given in seconds

    # /proc/[pid]/status contains several fields of information about the process.
    ps_file_path = "/proc/" + pid + "/status"
    # /proc/[pid]
