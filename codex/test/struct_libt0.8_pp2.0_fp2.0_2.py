import _struct

class FONT5x5(object):
    def __init__(self, font_path):
        with open(font_path, "rb") as font5x5_file:
            font5x5_data = font5x5_file.read()
        self.data = []
        for index in range(0, len(font5x5_data), 8):
            self.data.append((font5x5_data[index:index+4], font5x5_data[index+4:index+8]))

    def __getitem__(self, index):
        return self.data[index]

    def __len__(self):
        return len(self.data)

class FONT4x4(object):
    def __init__(self, font_path):
        with open(font_path, "rb") as font4x4_file:
            font4x4_data = font4x4_file.read()
        self.data = []
