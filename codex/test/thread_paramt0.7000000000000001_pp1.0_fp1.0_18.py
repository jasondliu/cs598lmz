import sys, threading
threading.Thread(target=lambda:sys.stdout.write("hello, world\n")).start()

# 3. Once running, your code can print to stdout by calling print(...),
# but it won’t display in the console window until the program exits.
# To force the console to print your output while the program is running,
# you can call sys.stdout.flush()
#
# To print the output to a file, you can redirect stdout (“1> file”),
# or you can open the file and assign it to sys.stdout before printing.
#
# 4. If you want to allow the program to read from stdin, you can assign
# sys.stdin to some other file object, such as sys.stdin = open("data")
#
# 5. If your program needs to read the command-line arguments passed in,
# you can access them through the list variable sys.argv.
# sys.argv[0] is the name of your program, and sys.argv[1:] are the
# arguments that were passed in.
import sys
print(sys.argv)
#
