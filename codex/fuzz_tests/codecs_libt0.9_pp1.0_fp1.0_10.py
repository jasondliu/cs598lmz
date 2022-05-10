import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

#https://www.linkedin.com/jobs/search/?f_C=1486%2C1485%2C1487&f_TP=1%2C2%2C3&keywords=&location=&locationId=us%3A0
#https://www.linkedin.com/jobs/feed/1486/company:179104/companyJobType:FULL_TIME/localeCookie:US?position=1&pageNum=0




def get_html(url):
    """
    Return the html source code of a web page
    """
    try:
        return requests.get(url).text
    except:
        return "SOMETHING GOES WRONG!!!"


#DONE
def find_company_job_cards(URL):
    """
    Return the html code containing the cards with the jobs
    the search was based on
    """
    html_source = BeautifulSoup(get_html(URL))
   
