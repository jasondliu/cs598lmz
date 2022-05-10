import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

#class list:
#    def __init__(self):
#        self.list=[]
#    def add(self,num):
#        self.list.append(num)
#    def remove(self,num):
#        self.list.remove(num)
#    def get_list(self):
#        return self.list

#class set_list:
#    def __init__(self):
#        self.list=[]
#    def add(self,num):
#        self.list.append(num)
#    def remove(self,num):
#        self.list.remove(num)
#    def get_list(self):
#        return self.list

class Team:
    def __init__(self,name,rank,point,difference):
        self.name=name
       
