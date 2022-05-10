import sys, threading

def run():
    while True:
        line = sys.stdin.readline()
        print('%s' % (line.rstrip()))
        sys.stdout.flush()


t = threading.Thread(target=run)
t.setDaemon(True)
t.start()

time.sleep(10)
</code>
If I put a line <code>time.sleep(10)</code> to the end, I will get the following result. It will wait 10 seconds to print out the next lines.
<code>$ head -10 /dev/urandom | ./stream.py
$&gt; '�P�d�#�eB�mZ��D�\�m8�[f��:�4��o�P@�X��8��H�G0��s�
$&gt; I�\�IRl�t�P�C�n
$&gt; 9�\s�'�����T�T&amp;�t�W;����:�d�� �
$�
$&gt; 
$&gt; ���D��A�
