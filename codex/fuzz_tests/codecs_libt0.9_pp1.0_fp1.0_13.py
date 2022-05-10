import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

def get_duration_in_second(duration_string):
    if duration_string is None:
        return None
    pattern = re.compile(r'(?:(\d+)D)*(?:(\d+)H)*(?:(\d+)M)*(?:(\d+)S)*')
    duration_matches = pattern.match(duration_string)
    if duration_matches is not None:
        days_string = duration_matches.group(1)
        hours_string = duration_matches.group(2)
        minutes_string = duration_matches.group(3)
        seconds_string = duration_matches.group(4)
        if days_string is None:
            days = 0
        else:
            days = int(days_string)
        if hours_string is None:
            hours = 0
        else:
            hours = int(hours_string)
        if minutes_string is None:
            minutes = 0
        else:
