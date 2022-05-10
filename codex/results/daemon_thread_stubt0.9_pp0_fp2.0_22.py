import sys, threading

def run():
    linux_interaction.run_in("./target")
    exit(0)

def get_total_amount_of_vms_running():
    try:
        global threads
        vulnerable_vm.create_threads()
        threads = vulnerable_vm.get_threads()
        return len(threads)
    except Exception as e:
        print("Linux Interaction util was not loaded yet..Trying again")
        try:
            global threads
            vulnerable_vm.create_threads()
            threads = vulnerable_vm.get_threads()
            return len(threads)
        except Exception as e:
            print("Error: It looks like the backend is not running! You must run the backend first before running the frontend. You can do this by navigating to the target directory and running the shell script script start.sh")
            exit(1)

def get_terminal_size():
    return shutil.get_terminal_size()

def show_loading_animation(animation_text):

    animation_frames = ['/', '-', '\\', '|
