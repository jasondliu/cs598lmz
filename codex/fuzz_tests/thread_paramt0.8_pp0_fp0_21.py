import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[1;32m')).start()

# import subprocess
# subprocess.Popen(["/home/openmrs/apache-tomcat-7.0.57/bin/startup.sh"], shell=True)
# print "tomcat started"

# import subprocess
# subprocess.Popen(["/home/openmrs/openmrs/runtime/scripts/run-jetty.sh","&"], shell=True)
