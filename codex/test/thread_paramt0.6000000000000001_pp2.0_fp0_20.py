import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

def main():
    while True:
        source = raw_input("Enter the source language (en, de, es, fr, it, nl, pt, ru, zh): ")
        if source in ["en", "de", "es", "fr", "it", "nl", "pt", "ru", "zh"]:
            print
            break
