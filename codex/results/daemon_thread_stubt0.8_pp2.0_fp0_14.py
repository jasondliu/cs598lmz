import sys, threading

def run():
    global read_file
    file_len = len(read_file)
    print("File length:", file_len)
    old_line_len = 0
    new_line_len = 0
    count = 1

    while True:
        new_line_len += len(read_file[count])
        print("{} of {}".format(new_line_len, file_len))
        count += 1
        if (new_line_len * 100 // file_len) != (old_line_len * 100 // file_len):
            old_line_len = new_line_len
            percent = 100 * new_line_len // file_len
            print("{}%".format(percent))
            sys.stdout.flush()

f = open("file1.txt")
read_file = f.readlines()
f.close()

t = threading.Thread(target=run)
t.start()

input("Press ENTER to stop...")
