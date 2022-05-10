import mmap
import sys
import os
import re

def main():
    """
    読み込むファイルを指定する
    """
    file_name = input('Input file name >>> ')

    with open(file_name, "r") as f:
        # ファイルをメモリ上にマップする
        m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)

        # ファイルの末尾まで繰り返す
        while True:
            # ファイルから1行分を読み込む
            line = m.readline()
            # ファイルの末尾に到達したら終了
            if not line:
                break
            # 文字列を表示
            print(line)

