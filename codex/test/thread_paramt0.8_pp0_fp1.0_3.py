import sys, threading
threading.Thread(target=lambda: sys.stdout.write('')).start()

import music21

def note_to_midi(note):
    """
    Converts a Music21 Note object to a MIDI value
    """
    return note.pitch.midi

def write_to_midi(filename, score, quantize=True):
    """
    Writes a score to a MIDI file.
    """
    stream = music21.stream.Stream(score)
    if quantize:
        quantizer = music21.quantize.Quantizer(stream)
        quantizer.process()
    stream.write('midi', fp=filename)

def write_to_musicxml(filename, score):
    """
    Writes a score to a MusicXML file.
    """
