import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("Youtube Downloader")

try:
    from pytube import YouTube
except ImportError:
    print("\n[!] Please install pytube first")
    print("\n[!] pip install pytube3")
    exit()

def banner():
    print("""
    
    ################################################
    #                                              #
    #       Youtube Downloader                      #
    #       Author: @muh_syahidin                  #
    #       Github: https://github.com/muhsyahidin #
    #                                              #
    ################################################
    
    """)

def download(url):
    yt = YouTube(url)
    stream = yt.streams.first()
    stream.download()
    print("\n[+] Download Success")

def main():
    banner()
    url = input("[?] Youtube URL: ")
    download(url)

if __name__ == "__main__":
    main()
