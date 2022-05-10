import codecs
codecs.register_error('strict', codecs.lookup_error('ignore'))

# utf-8 standard
sys.stdout = codecs.getwriter('utf-8')(sys.stdout)
sys.stdin = codecs.getreader('utf-8')(sys.stdin)

#=========================================================================
# 
#
#
def main():

    up = True

    while True:
        buf = raw_input().strip()
        #buf = input().strip()
        if buf == 'DONE':
            return

        buf = buf.replace('.','')
        buf = buf.replace(',','')
        buf = buf.replace('!','')
        buf = buf.replace('?','')
        buf = buf.replace('\'','')
        buf = buf.replace(' ','')

        for i in range(len(buf)):
            buf = buf.lower()

        ans = buf

        if (ans == ans[::-1]):
            print('You won\'t be eaten!')
        else:
            print('Uh oh..
