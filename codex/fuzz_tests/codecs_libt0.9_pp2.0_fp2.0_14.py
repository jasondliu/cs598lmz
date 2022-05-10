import codecs
codecs.getwriter('utf-8')(sys.stdout)


class ColorScheme:
    def __init__(self):
        self.names = []
        self.colors = ["#C60A00","#8EBA42","#6A3A4C","#CC333F","#EB6841","#EDC951",
                "#E94E77","#D68189","#EC7063","#F0EAD6","#F4A261","#F18D9E",
                "#EE6AA7","#86E2D5","#FAD489","#FF847C","#F6A38E","#DBDB46",
                "#D7B8F9","#EFC0FE"]

    def get_color(self, name):
        try:
            return self.colors[self.names.index(name)]
        except:
            self.names.append(name)
            return self.colors[self.names.index(name)]

    def get_colored_classes(self, names):
        return [ (name, self.
