import codecs
codecs.register_error('surrogate_or_strict', codecs.surrogateescape)

def get_time(timezone):
    time = datetime.datetime.now(tz=pytz.timezone(timezone))
    return time

def get_time_for_other_timezone(country_timezone):
    time = datetime.datetime.now(tz=pytz.timezone(country_timezone)).strftime('%H:%M:%S')
    return time

def get_time_for_country_in_english(country_timezone):
    time = datetime.datetime.now(tz=pytz.timezone(country_timezone)).strftime('%I:%M:%S %p')
    return time

def get_time_for_country_in_english_without_seconds(country_timezone):
    time = datetime.datetime.now(tz=pytz.timezone(country_timezone)).strftime('%I:%M %p')
    return time

def get_time_for_country_in_english
