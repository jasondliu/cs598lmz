import ctypes
ctypes.windll.kernel32.SetConsoleTitleW(title)

#
# Set the logging level
#
logging.basicConfig(level=logging.INFO)

#
# Clear the terminal
#
os.system('cls' if os.name == 'nt' else 'clear')

#
# Set the working directory
#
os.chdir(os.path.dirname(os.path.realpath(__file__)))

#
# Set the argument parser
#
parser = argparse.ArgumentParser(description="This script will create a new project with a specified name.")
parser.add_argument("project_name", help="The name of the project to create")
parser.add_argument("-v", "--verbose", help="Increases the program's output verbosity", action="store_true")
parser.add_argument("-s", "--src", help="Specify the source directory", action="store_true")
parser.add_argument("-d", "--dest", help="Specify the destination directory", action="store_true")
parser.add_argument("--version
