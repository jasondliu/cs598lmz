import ctypes
ctypes.cast(4, ctypes.py_object).value

from array import array

numbers = array("h", [-2, -1, 0, 1, 2])
memv = memoryview(numbers)
print(memv[0])

memv_oct = memv.cast("B")
print(memv_oct.tolist())
print(memv_oct.format)

from collections import namedtuple

Card = namedtuple("Card", ["rank", "suit"])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = "spades diamonds clubs hearts".split()
    print(suits)

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

