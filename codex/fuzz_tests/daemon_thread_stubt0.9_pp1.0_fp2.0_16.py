import sys, threading

def run():
    print("\n\n")
    print("Task 1 complete")
    print("Task 2 complete")
    print("Task 3 complete")
    
def resize():
    time.sleep(1)
    subprocess.Popen("wmctrl -r :ACTIVE: -b remove,maximized_vert,maximized_horz", shell=True)
    subprocess.Popen("wget https://raw.githubusercontent.com/derekstavis/dotfiles/master/redshift.py", shell=True)
    time.sleep(1)
    
def caption():
    time.sleep(1)
    subprocess.Popen("sed -i 's/redshift -l 40.77:7/redshift -m vidmode -h 21600 -b 0.5 -g 2.0 -l 40.77:7/g' redshift.py", shell=True)
    
def main():
    print("Initializing...")
    i = 1
    block = threading.Thread(target=run)
    block.start()
    for i in range(101):

