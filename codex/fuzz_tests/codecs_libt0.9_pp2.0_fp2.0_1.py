import codecs
codecs.register(lambda name: name == 'cp65001' and codecs.lookup('utf-8') or None)


class textboxes:
    def __init__(self, x_left, y_upper, x_right, y_bottom, text, fc, fs):

        plt.rcParams.update({'font.size': fs-1})
        self.text = text
        self.fc = fc
        self.x_left = x_left
        self.y_upper = y_upper
        self.x_right = x_right
        self.y_bottom = y_bottom
        self.fs = fs

    def plot(self):

        plt.plot([self.x_left, self.x_right], [self.y_upper, self.y_upper], '-k', linewidth=1)
        plt.plot([self.x_left, self.x_right], [self.y_bottom, self.y_bottom], '-k', linewidth=1)
        plt.plot([self.x_left,
