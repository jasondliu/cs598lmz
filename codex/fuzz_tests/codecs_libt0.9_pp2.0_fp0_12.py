import codecs
codecs.register_error('ignore', codecs.ignore_errors)

class MediaCodecs:

    def __init__(self,media_data=None,media_type=None,media_extension=None,media_name=None,media_description=None,media_online=None):
        self.media_data = media_data
        self.media_type = media_type
        self.media_extension = media_extension
        self.media_name = media_name
        self.media_description = media_description
        self.media_online = media_online
        self.media_type_text = ['.wav']
        self.media_type_image = ['.png','.jpeg','.jpg']
        self.media_type_video = ['.avi','.mp4']
        self.media_type_media = ['.wav','.midi','.mid','.aac','.mp2','.mp3','.ra','.rm','.ram','.flac','.video','.mkv','.webm','.flv','.vob']

