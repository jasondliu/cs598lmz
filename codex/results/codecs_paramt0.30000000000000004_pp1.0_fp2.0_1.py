import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_transcript(filename):
    """
    Given a filename, returns the transcript for the corresponding audio file.
    """
    transcript = []
    with open(filename) as f:
        for line in f:
            transcript.append(line.strip())
    return transcript

def get_audio(filename):
    """
    Given a filename, returns the audio for the corresponding audio file.
    """
    audio = []
    with open(filename) as f:
        for line in f:
            audio.append(line.strip())
    return audio

def get_all_transcripts(path):
    """
    Given a path, returns a list of all transcripts in the directory.
    """
    transcripts = []
    for filename in os.listdir(path):
        if filename.endswith(".txt"):
            transcripts.append(get_transcript(path + filename))
    return transcripts

def get_all_audio(path):
    """
    Given a path, returns a list of all audio in the
