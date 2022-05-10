import codecs
codecs.register_error('ignore_bad_chars', lambda x: ('', x.start + 1))

# requires: python3, pyperclip
# credits: https://github.com/nesl247/openthesaurus-thesaurus.de_scraper/blob/master/README.md

# TODO:
# 1. search thesaurus: synonyms, antonyms

# TODO: GUI
# 1. GUI search
# 2. GUI search results
# 3. GUI search thesaurus


# TODO: get synonyms for "succeed"
# synonyms = get_synonyms("succeed")
# for synonym in synonyms:
#     print(synonym)

# TODO: search google
# search_google("succeed")


# TODO:
# 1. get data from clipboard
# 2. search thesaurus, google
# 3. append search results:
# -- append synonyms
# -- append google search
# 4. update clipboard

# clipboard_text = pyperclip.paste()
# print(clipboard_text)


