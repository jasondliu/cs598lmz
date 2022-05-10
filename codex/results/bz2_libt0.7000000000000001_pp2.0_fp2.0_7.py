import bz2
bz2_file = bz2.open('./data/json/banner_page_returns.json.bz2', 'rb')
page_count = 0
page_returns = []
for line in bz2_file:
    page = json.loads(line)
    page_returns.append(page)
    page_count += 1
print "Done"

print "Counting pages with each type of return code..."
return_codes = {}
for page in page_returns:
    return_code = page['response']['code']
    if return_code not in return_codes:
        return_codes[return_code] = 1
    else:
        return_codes[return_code] += 1
print "Done"
print "Printing return code counts..."
for return_code in sorted(return_codes):
    print return_code, return_codes[return_code]

print "Printing pages with non-200 return code..."
for page in page_returns:
    return_code = page['response']['code']
    if return_code
