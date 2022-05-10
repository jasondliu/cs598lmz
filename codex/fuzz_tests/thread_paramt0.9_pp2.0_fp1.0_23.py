import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\a')).start()
sleep(10)

# sys.stdout.write('\a')
# os.system('echo -e "\a\a"')
</code>
But on Windows, it doesn't make any sound...
I tried many things, but I just cannot make a thread making a beep sound after a delay. The beep sound is immediately triggered before the sleep...
I tried :

Subprocess to call CMD with echo -e "\a\a"
La bibliotheque playsound
subprocess.Popen(["CMD", "/C", "echo -e \"\a\a\""], stdout=subprocess.PIPE)
threading.Thread(target=lambda: sys.stdout.write('\a')).start()

But on the last trial the beep sound is produced immediately, but the 10s delay is not applied, it only wait 10s after the sound has been produced...
Anyone can help to make it work?


A:

Use <code>threading.Thread</code> to spawn a thread like this:
<code>
