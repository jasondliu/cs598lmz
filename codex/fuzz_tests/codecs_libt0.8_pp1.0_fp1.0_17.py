import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)

# checker class
class Checker:
    def __init__(self):
        self.url_list = []
        self.selected_url_list = []
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
        
        # data variable
        self.data_var_1 = tkinter.StringVar()
        self.data_var_2 = tkinter.StringVar()

        # check variable
        self.check_var_1 = tkinter.IntVar()
        self.check_var_2 = tkinter.IntVar()
        self.check_var_3 = tkinter.IntVar()
        self.check_var_4 = tkinter.IntVar()
        
        # init application
        self
