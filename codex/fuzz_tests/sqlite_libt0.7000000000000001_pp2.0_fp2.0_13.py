import ctypes
import ctypes.util
import threading
import sqlite3


def get_wallpaper_path():
    """
    获取桌面背景图片地址
    """
    try:
        # ctypes.windll.user32.SystemParametersInfoW(20, 0, r"C:\Users\lz\Pictures\Saved Pictures\3.jpg", 0)
        SPIF_SENDWININICHANGE = 2
        SPI_SETDESKWALLPAPER = 20
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, r"C:\Users\lz\Pictures\Saved Pictures\3.jpg", SPIF_SENDWININICHANGE)
        return True
    except Exception as e:
        print(e)
        return False

def main():
    get_wallpaper_path()
    pass


if __name__ == '__main__':
    main()
    pass
