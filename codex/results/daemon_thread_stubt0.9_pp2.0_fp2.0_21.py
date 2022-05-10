import sys, threading

def run():
    try:
        print "\nSetting up connection..."
        rp = RPi()
        print "Connected to Raspberry Pi\n"
    except:
        print "\nFailed to connect to Raspberry Pi\n"
        sys.exit(0)

    rp.play_wav("bgm.wav", blocked = False)
    talk = False

    try:
      with open("phrases.txt") as f:
        content = f.readlines()
    
      print "\nPhrases to speak:"
      while len(content) > 0:
          print content.pop(0).strip("\n")

      print "\nGo?"
      ans = raw_input()
      pygame.mixer.music.set_volume(0.0)
      while ans.lower().strip(" ") != "go":
        print "Go?"
        ans = raw_input()

    except:
      print "\nError loading phrases.txt"
      sys.exit(0)

    h = he()

    print "\n"

    for p in content: # printing the phrases

