import bz2
bz2.BZ2Compressor()
# from IPython.display import display,HTML
from IPython.display import IFrame

class AudioSample:
    def __init__(self, jar, sample_id, filename, filetype, feature_data, offset=0, duration=None, 
                 language=None, gender=None, age=None, voice=None, created=None, filetype_from=None, 
                 filetype_to=None, feature_extractor=None, feature_extractor_version=None,
                 stored=None, modified=None, feature_key=None, mime_type=None):
        self.jar = jar  # the connection to the database
        self.sample_id = sample_id
        self.filename = filename
        self.filetype = filetype
        self.feature_data = feature_data
        self.offset = offset
        self.duration = duration
        self.language = language
        self.gender = gender
        self.age = age
        self.voice = voice
        self.created = created
        self.filetype_from = file
