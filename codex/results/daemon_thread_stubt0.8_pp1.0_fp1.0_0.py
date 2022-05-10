import sys, threading

def run():
    br = mechanize.Browser()
    br.set_handle_equiv(True)
    br.set_handle_redirect(True)
    br.set_handle_referer(True)
    br.set_handle_robots(False)
    br.set_cookiejar(cj)
    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
    br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
    try:
        site = br.open(url)
        br.select_form(nr=0)
        br.form['username'] = user
        br.form['password'] = pw
        br.submit()
        log = br.geturl()
        if log in url:
            print(i+"|"+pw+" => Success")
        else:
            print(i+"|
