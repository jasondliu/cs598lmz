import socket
socket.if_indextoname(2)

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

IP = get_ip()

driver = webdriver.Firefox()
driver.get("http://www.whatsmyip.org/")

time.sleep(5) # Let the user actually see something!

driver.find_element_by_id("myip").send_keys(IP)
driver.find_element_by_id("randomInput").click()

time.sleep(5) # Let the user actually see something!
driver.quit()
</code>
Output:
<code>Traceback (most recent call last):
  File "C:/Users/masharesh/PycharmProjects/Selenium/Gecko/Get_IP.
