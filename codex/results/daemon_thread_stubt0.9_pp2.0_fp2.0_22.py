import sys, threading

def run():

    if len(sys.argv) == 1:
        print("USAGE: python3 wav2midi.py path")
        sys.exit()

    print("Current directory: " + os.path.dirname(os.path.abspath(__file__)))

    wav_path = str(sys.argv[1])
    print("Parsing: " + wav_path)

    piece = MusicPiece()
    for track in piece.extract_track_sentences(wav_path):
        print(track)


run()
