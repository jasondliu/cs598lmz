import threading
threading.stack_size(2**27)
import sys
import subprocess
from robot_parser import robot_parser
import robots_class

sys.setrecursionlimit(10**7)
threading.Thread(target=main).start()

def main():
    new_folder = make_new_folder(folder_name)
    parse_robots_txt(robots_url, new_folder)

def make_new_folder(folder_name):
    if os.path.isdir(folder_name):
        shutil.rmtree(folder_name)
        os.mkdir(folder_name)
    else:
        os.mkdir(folder_name)
    return folder_name

def parse_robots_txt(url, folder):
    if url_is_valid(url):
        soup = BeautifulSoup(get_url_data(url), "html.parser")
        robots_txt_url = url + '/robots.txt'

        if url_is_valid(robots_txt_url):
            robot_txt_file = open(folder
