import codecs
codecs.register_error('strict', codecs.ignore_errors)

searchQuery = "Edward Maurice Corbould | Artist | Edmond Malone | Portrait | Existence  |"

def get_searchIndex(searchQuery):
    print "Target Search Query String: %s" % (searchQuery)
    publisher = u"tate"
    workPlace = u"London"
    year = u"1868"
    term = searchQuery.strip().split(" | ")
    print "The length of the search terms is %s" % len(term)
    term_list = []
    for t in range(len(term)):
        termNonEmpty = term[t].strip()
        term_list.append(termNonEmpty)
    print "And the length of the searchterms list is %s" % (len(term_list))
    #create a list of search terms that do not apply to a person
    searchTerms = []
    for t in term_list:
        #print t
        if t != publisher and t != workPlace and t != year:
            searchTerms.append(t)

