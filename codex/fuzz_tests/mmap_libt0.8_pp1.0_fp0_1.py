import mmap

spec_path = '/home/dalmo/work/2017.1-M2SID-2017/trabalhos/Escarlate/discogs_20160227_songs'
file = open(spec_path, "r+b")
mm = mmap.mmap(file.fileno(), 0)

number_of_files = int(len(mm)/259)

fakes = 0
for i in range(number_of_files):
    mm.seek(259*i)
    artist_name = mm.read(200).split(b'\x00', 1)[0]
    song_title  = mm.read(200).split(b'\x00', 1)[0]
    song_year   = mm.read(4).split(b'\x00', 1)[0]
    disc_number = mm.read(4).split(b'\x00', 1)[0]
    song_number = mm.read(4).split(b'\x00', 1)[0]
    genre_id    = mm.read(4).split(
