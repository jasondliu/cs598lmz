import bz2
bz2.BZ2File()

# Once the script has completed, the user should be able to use the tool to
# display extracted information like the following.

# $ python ./samples.py
# Product Version: 6.00.2900.2180
# Registry: Software\Microsoft\Windows\CurrentVersion\Run
# \Yahoo! Updater: "C:\Program Files\Yahoo!\SoftwareUpdate\YahooAUService.exe" /startup
# \iTunesHelper: "C:\Program Files\iTunes\iTunesHelper.exe"
# \MSMSGS: "C:\Program Files\Messenger\msmsgs.exe" /background
#
# ... additional output truncated ...

if __name__ == '__main__':
    import optparse

    parser = optparse.OptionParser(description='Extract information from a Windows NT user hive.',
                                   prog='hivelist.py',
                                   version='0.1',
                                   usage='%prog system.hive')

    # Fold the parser's options (e.g., --help)
