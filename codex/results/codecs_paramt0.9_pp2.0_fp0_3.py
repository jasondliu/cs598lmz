import codecs
codecs.register_error("Ignore.replace", lambda x:("",""))

def process_transcript_1210(folder_name, transcript_name, readable_name):
    path = "../data_raw/%s/%s.txt" % (folder_name, transcript_name)
    txt = codecs.open(path, "r", "utf-8").read().encode("utf-8", "Ignore.replace").lower()
    output_path = "../data_interim/%s/%s.txt" % (folder_name, transcript_name)
    f = open(output_path, "w")
    f.write(txt)
    f.close()

def process_transcript_1210_all(folder_name):
    for i in ['1210a', '1210b', '1210c']:
        process_transcript_1210(folder_name, i, "%s %s" % (folder_name, i))

process_transcript_1210('corruption_related', 'a', 'Corruption A')
process_transcript_1210('
