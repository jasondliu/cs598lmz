import sys, threading

def run():
    time_end = time.time() + 45
    while time.time() < time_end:
        #shell("./bin/manager --show-all")
        shell("./bin/dynamic_cast")
        shell("./bin/observer")
        shell("./bin/simple_factory")
        shell("./bin/builder")
        shell("")
        time.sleep(0.1)



def shell(cmd):
    print("==> %s" %(cmd))
    status, output = commands.getstatusoutput(cmd)
    if status != 0:
        print("`%s` failed with status %d" %(cmd, status))
        sys.exit(1)
    print("-> %s" %(output))
    print("")



if __name__ == "__main__":
    print("")

    if os.path.exists("bin"):
        shutil.rmtree("bin")

    os.mkdir("bin")

    shell("g++ -std=c++11 -o ./bin/
