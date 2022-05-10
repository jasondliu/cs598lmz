import sys, threading

def run():
    sys.stdout.write('\x1b]2;%s\x07' % 'Notification')
    os.system('notify-send -a "Notification" "Notification" "Notification"')

thread = threading.Thread(target=run)
thread.start()
</code>
The problem is that the notification is only displayed when the program is closed, and not while it is running.
How can I make the notification appear while the program is running?


A:

You can use <code>gobject.timeout_add</code> to show a notification every second:
<code>import gobject
import os

def show_notification():
    os.system('notify-send -a "Notification" "Notification" "Notification"')
    return True

gobject.timeout_add(1000, show_notification)
gobject.MainLoop().run()
</code>

