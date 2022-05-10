import sys, threading

def run():
  global thread_run
  thread_run = True
  while thread_run:
    from YNM.videoio.camera import CameraThread
    if not os.path.exists(CameraThread.camFile):
        os.mkfifo(CameraThread.camFile)
    p = subprocess.Popen(['/usr/bin/raspivid','--nopreview','--timeout','0','-o',CameraThread.camFile,'-t','0','-w','640','-h','480','-fps','30','-b','5000000','-g','50','-awb','off','-ev','0'],preexec_fn=os.setpgrp)
    print 'subprocess id:',str(p.pid)
    p.wait()

thread = None

def start():
 global thread
 if thread == None or not thread.is_alive():
   thread = threading.Thread(target=run)
   thread.setDaemon(True)
   thread.start()

def stop():
 global thread_run
 thread_run = False
 if thread
