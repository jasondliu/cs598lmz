import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

#`pip install mysqlclient`
#`pip install --upgrade pip`

#print(REC_DATE_TIME)

#print(TIMESTAMP)

#print(REMOTE_ADDR)

#print(SCRIPT_NAME)

#print(REQUEST_METHOD)

#print(HTTP_HOST)

#print(HTTP_USER_AGENT)

#print(HTTP_REFERER)

#print(PATH_INFO)

#print(QUERY_STRING)

#print(FORM_DATA)

#print(HTTP_VERSION)

#print(HTTP_CONNECTION)

#print(HTTP_ACCEPT)

#print(HTTP_ACCEPT_ENCODING)

#print(HTTP_ACCEPT_LANGUAGE)

#print(HTTP_COOKIE)

#print(HTTP_UPGRADE_INSECURE_REQUESTS)

