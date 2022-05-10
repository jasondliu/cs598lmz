import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

def main():
    while True:
        source = raw_input("Enter the source language (en, de, es, fr, it, nl, pt, ru, zh): ")
        if source in ["en", "de", "es", "fr", "it", "nl", "pt", "ru", "zh"]:
            print
            break
        else:
            print "Invalid language. Please try again."
    while True:
        target = raw_input("Enter the target language (en, de, es, fr, it, nl, pt, ru, zh): ")
        if target in ["en", "de", "es", "fr", "it", "nl", "pt", "ru", "zh"]:
            print
            break
        else:
            print "Invalid language. Please try again."
    while True:
        word = raw_input("Enter a word in the " + source + " language (or type 'exit'): ")
        if word == "exit":
            break
        else:

