import sys, threading
threading.Thread(target=lambda: sys.stdout.write(input())).start()
#sys.stdout.write(input())

#curl http://localhost:8080/Classification/res -X PUT -d "{\"id\":123}"
#curl http://localhost:8080/Classification/res -X PUT -d "{\"id\":123, \"output\":[90,5]}"


'''
import sys, urllib2
get_html = urllib2.urlopen(sys.argv[1]).read()
print get_html
'''
