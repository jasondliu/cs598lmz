import threading
threading.stack_size(2**27)

def run_thread(n):
    from urllib.request import urlopen
    from bs4 import BeautifulSoup
    import re
    import csv
    import time
    global root_url
    global locked_nodes
    global locked_nodes_file
    global target
    global counter
    global res_file
    global link_counter
    global total_nodes
    global time_start
    global time_end

    try:
        html = urlopen(root_url + n)
    except:
        locked_nodes.append(n)
        locked_nodes_file.write(n + '\n')
        locked_nodes_file.flush()
        print('link locked: ', root_url + n)
        return
    bsObj = BeautifulSoup(html, 'lxml')
    name = bsObj.find('div', {'class':'card-header'}).get_text()
    print(n, name)
    counter.append(n)
