import threading
threading.stack_size(2**27)

sys._enablelegacywindowsfsencoding() # Fixes an issue where MP3s can't be encoded properly on Windows
# set debug level to warning logging.basicConfig(level = logging.INFO) logging.debug("asdf")

THREADS = 16

def main():
    posts = grab_posts(16)
    
    for post in posts:
        if post.is_album == True:
            print("[-] Album found at: " + post.url)
            post.download_album()

if __name__ == "__main__":
    Pool(THREADS, main, (1,))
