import ctypes
import ctypes.util
import threading
import sqlite3
import time

# TODO: D-Bus, PulseAudio

class SpeechError(Exception):
    pass

class SpeechSynthesizer:
    """The interface class for all synthesizers.
    
    Implements the core functionality of all synthesizers, especially the
    interfaces to the user application.
    """
    
    def __init__(self, speak_chars):
        """Initializes the synthesizer.
        
        Args:
            speak_chars: If True, the synthesizer will speak char-by-char
                when the speak_text method is called. Otherwise, it will
                speak by word.
        """
        
        self.queue = []
        
        self.speak_chars = speak_chars
        self.queue_lock = threading.RLock()
        self.synthesizing = False
        
        self.callback = {}
        self.synth_thread = None
        
        self.register_callback("SPEECH_START")
        self.register_callback("SPEECH_STOP")
        self.register_
