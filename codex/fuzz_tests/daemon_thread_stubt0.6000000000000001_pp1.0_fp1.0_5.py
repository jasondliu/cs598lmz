import sys, threading

def run():
    os.system("python3.5 /home/pi/Desktop/python/logger.py")

def main():
    sys.path.append('/home/pi/Desktop/python')
    import logger
    run()

main()
</code>
I want to run <code>logger.py</code> in a thread, and when I do it with <code>os.system</code> it works perfectly fine. But when I try to do it with <code>threading</code>, it doesn't work. I have no idea why.


A:

The script is running in the thread. I think you are confused because the <code>print</code> statements are not executed.
What happens is that the thread is created and the script is started. The <code>while True</code> loop starts and the <code>print</code> statement is executed. Then the script waits for the user to press enter. In the meantime the main thread finished execution.
To prevent the main thread from exiting, you can join the thread:
<code>def main():
    sys.path.append('/home/pi/Desktop
