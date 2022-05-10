import ctypes
ctypes.windll.kernel32.SetConsoleMode(console, 7)

class SC_BASE_API():
    def LOAD_BASE_CONF(self, conf_name, conf_dir = "etc\\", conf_ext = "conf"):
        if os.path.isfile(conf_dir + conf_name + "." + conf_ext): #コンフィグファイルの読み込み
            f = open(conf_dir + conf_name + "." + conf_ext, "r")
            lines = f.readlines()
            f.close()
            self.conf_list = []
            for line in lines:
                if re.search(r"\A[^#].+\z", line) != None: #コメント行は除外する

                    args = line.replace("\n", "").replace("\r", "").replace("\t", "").split(":") #raw_input()が無限ループになる原因
                    self.conf_list
