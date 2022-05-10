import codecs
codecs.register_error('strict', codecs.ignore_errors)

def text_clean(text):
    
    text = text.lower()
    
    # Special handlings
    
    # Correct some words from the original text
    text = re.sub('master system', 'master system', text)
    text = re.sub('pokemon firered', 'pokemon fire red', text)
    text = re.sub('pokemon leafgreen', 'pokemon leaf green', text)
    text = re.sub('pokeflute', 'poke flute', text)
    text = re.sub('fog badge', 'fogbadge', text)
    text = re.sub('^pkmn ', 'pokemon ', text)
    text = re.sub('^pokemon go ', 'pokemongo ', text)
    text = re.sub('^pokémon$', 'pokemon', text)
    text = re.sub('incense', 'incense', text)
    text = re.sub('super nintendo', 'suprnintendo', text)
    text = re.sub('nintendo 64', '
