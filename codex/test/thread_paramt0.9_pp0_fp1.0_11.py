import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x07')).start()
threading.Thread(target=lambda: sys.stdout.write(chr(7))).start()

# class Song():
#     def __init__(self, name, composer):
#         self.name = name
#         self.composer = composer

#     def __repr__(self):
#         return f"Song(name='{self.name}', composer='{self.composer}')"

#     def __eq__(self, other):
#         if isinstance(other, type(self)):
#             return self.name == other.name and self.composer == other.composer
#         return NotImplemented

#     def __gt__(self, other):
#         if isinstance(other, type(self)):
#             if self.composer == other.composer:
#                 return self.name > other.name
#             else:
#                 return self.composer > other.composer
#         return NotImple
