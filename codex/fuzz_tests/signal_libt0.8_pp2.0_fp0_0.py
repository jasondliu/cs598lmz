import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

def runner(user):
    return subprocess.Popen(cmd,shell=True) 

def changePem():
    global cmd
    filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("Key files","*.pem"),("all files","*.*")))
    cmd = "sudo chmod 400 " + filename
    runner(cmd)
    cmd = "ssh -i " + filename + " -t ec2-user@" + ip + " bash"
    ssh = runner(cmd)

def kill():
    ssh.kill()
    root.destroy()

#Setting up tkinter
root = tk.Tk()
root.title("Remote Desktop")

#Get AWS IP
ip = "3.208.125.14"

#Set up ssh to run on AWS
cmd = "ssh -i ~/Desktop/matt.pem -t ec2-user@" + ip + " bash"

#Running ssh on AWS
