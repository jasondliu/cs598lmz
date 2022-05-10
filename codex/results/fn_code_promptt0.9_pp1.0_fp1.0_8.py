fn = lambda: None
# Test fn.__code__
setattr(fn, '__code__', 42)
raise TypeError(
    "%s %s" % (fn.__code__, type(fn.__code__))
)

# CSV export with changed filename
# ################################
filename = getRandomString()
# Open webservice
driver.get("%s/services/?mode=csv" % baseUrl)
driver.find_element_by_id("csv_query").click()
# There should be only one file
if len(driver.find_elements_by_link_text("Download query (%s)" % filename)) != 1:
    raise Exception()
# Save and load file
exec(open(downloaderJsFilename).read())
# Check if file is ok
if not checkFile(filename, True):
    raise Exception(filename)

# PDF export with changed filename
# ################################
filename = getRandomString()
# Open webservice
driver.get("%s/services/?mode=pdf" % baseUrl)
driver.find_element_by_id("pdf_query").click()
# There
