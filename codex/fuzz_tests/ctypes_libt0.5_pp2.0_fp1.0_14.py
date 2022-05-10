import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("Tower of Hanoi")

class Tower:
    def __init__(self, n, source, destination, spare):
        self.n = n
        self.source = source
        self.destination = destination
        self.spare = spare
        self.move_count = 0

    def move_discs(self, n, source, destination, spare):
        if n > 0:
            self.move_discs(n - 1, source, spare, destination)
            print("Move disc from %s to %s" % (source, destination))
            self.move_count += 1
            self.move_discs(n - 1, spare, destination, source)


tower = Tower(3, "A", "B", "C")
tower.move_discs(tower.n, tower.source, tower.destination, tower.spare)
print("\nMoved %d discs." % tower.move_count)
