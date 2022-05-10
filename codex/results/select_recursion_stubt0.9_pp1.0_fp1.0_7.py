import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated().append(1)
            return 111111
        def recv(self,*args,**kargs):
            return ''

    class T:
        def read(self,*args,**kargs):
            return ''

    class F(F,T): pass

    b = select.select([F()],[],[],0.00001)

class stupid_socket1(socket.socket):
    'an object that harms itself to test `throttle` feature'

    def recv(self,*args,**kwargs):
        'override default recieve method for test'

        res=socket.socket.recv(self,*args,**kwargs)
        os.write(2,''.join(traceback.format_stack()))
        self.send("stupid_socket1.recv")
        return res

if __name__=='__main__':
    test_filter()
