import codecs
codecs.register_error("ignore", codecs.lookup_error("ignore"))

def wiki_summarize(string, n_sentences=5):
    if not isinstance(string, str):
        string = string.encode("utf-8")
    if len(string.encode("utf-8")) > 40000:
        return "string is too long"
    article = wikipedia.page(string)
    return summarize(article.content, n_sentences)


def wikipedia_search(article):
    results = wikipedia.search(article)
    return results


def summarize_article(string, n_sentences=5):
    article = Article(string)
    article.download()
    article.parse()
    return summarize(article.text, n_sentences)


if __name__ == '__main__':
    qstring = sys.argv[1]
    print wikipedia_search(qstring)
    print wiki_summarize(qstring)
