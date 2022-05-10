from bz2 import BZ2Decompressor
BZ2Decompressor.flush = lambda self: ""

def get_rank_info(data):
    initial_rank = re.search("Initial Rank: (\d+)", data)
    initial_exp = re.search("Initial EXP: (\d+)", data)
    if initial_rank is not None and initial_rank.groups() > 0:
       product_id=initial_rank.group(1)
    else:
       product_id="(Not Visible)"

    return product_id

def get_time_played(data):
    time_played = re.search("Total Minutes Played: (\d+)", data)
    if time_played is not None and time_played.groups() > 0:
       product_id=time_played.group(1)
    else:
       product_id="(Not Visible)"

    return product_id

def get_fireteam_size(data):
    fireteam_size = re.search("Fireteam Size: (\d+)", data)
    if fireteam_size is not None and fireteam_size.groups() > 0:
       product
