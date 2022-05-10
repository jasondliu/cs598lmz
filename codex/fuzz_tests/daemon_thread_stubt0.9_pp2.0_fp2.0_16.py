import sys, threading

def run():
    start_time = time.time()
    no_of_line_changes = 0 
    prevline = ""
    print("\n\t[+] Installing XSSER Framework for you my dear user....\n")
    f = open("/home/linux/install/packages_to_install.txt", 'r')
    for line in f.readlines():
        subprocess.call(line, shell=True)
        no_of_line_changes += 1   
    f.close()
    sys.stdout.write("\n\t[+] Execution completed in %.2f seconds "% (time.time() - start_time))
    print("\n\t[+] Installed "+str(no_of_line_changes)+" Packages ....\n")

class Command(BaseCommand):
    help = 'Installer'
    def handle(self, *args, **options):
    	thread = threading.Thread(target=run)
    	thread.start()
