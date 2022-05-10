import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()

def main():
    try:
        connection = sqlite3.connect(":memory:")
        connection.close()
    except Exception as e:
        print("Error:", e)
        return 1

    return 0

if __name__ == "__main__":
    import sys
    sys.exit(main())
