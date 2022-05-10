import bz2
bz2.decompress(response)

# You can now use the response object to get the decompressed data like this
#response.decompressed_data

# Getting the image from the response object
#img_data = response.content

# Saving the image
#with open('01_page.jpg', 'wb') as handler:
#    handler.write(img_data)

# getting the information about the status of the request
#print(response.status_code)

# Checking the url of the response object to see if we were redirected
#print(response.url)

# Checking the history of the request object to see if we were redirected
#print(response.history)

# We can also use the builtin functions of the requests module to extract the url and history object of the response object
#print(requests.utils.dict_from_cookiejar(response.cookies))

# Here we will print the history of the request
#for resp in response.history:
#    print(resp.status_code, resp.url)

# Here we will print the current url
#print(response
