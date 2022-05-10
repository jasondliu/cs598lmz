import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_zones(data):
    zones = []
    for line in data:
        if line.startswith('zone '):
            zones.append(line.split(' ', 2)[1])
    return zones

def get_zone_file(data, zone):
    zone_data = []
    zone_started = False
    for line in data:
        if zone_started and line.startswith('zone '):
            break
        if zone_started:
            zone_data.append(line)
        if line.startswith('zone ') and line.split(' ', 2)[1] == zone:
            zone_started = True
    return zone_data

def parse_zone_file(data):
    res = {}
    for line in data:
        if line.startswith('$INCLUDE '):
            if os.path.exists(line.split(' ', 1)[1]):
                res.update(parse_zone_file(open(line.split(' ', 1)[1]).readlines
