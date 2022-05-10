import codecs
codecs.register_error('ignore', codecs.ignore_errors)

MAX_VID_LEN = 100
MAX_DESC_LEN = 30

def read_corpus(filename, is_toy):
    data = []
    with open(filename, encoding='utf-8') as f:
        for line in f:
            title = line.strip().split('\t')[0]
            description = line.strip().split('\t')[1]
            tag = line.strip().split('\t')[2]
            # video data
            video_title = title.split(' ')
            video_description = description.split(' ')
            # phrase data
            tag_list = tag.split(' ')
            for i in range(len(video_title) - 1):
                for j in range(i + 1, len(video_title)):
                    data.append([video_title[i:j + 1], video_description, tag_list])
            for i in range(len(video_description) - 1):
                for j in range(i + 1, len(video
