import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

class ThreadWithReturnValue(threading.Thread):
    def __init__(self, group=None, target=None, name=None, args=(), kwargs={}, Verbose=None):
        threading.Thread.__init__(self, group, target, name, args, kwargs)
        self._return = None
    def run(self):
        if self._Thread__target is not None:
            self._return = self._Thread__target(*self._Thread__args, **self._Thread__kwargs)
    def join(self, *args):
        threading.Thread.join(self, *args)
        return self._return

# For extracting the text from a given page
def get_text(page):
    return page.text

# For extracting the text from the first paragraph of a given page
def get_first_paragraph(page):
    return page.find('p').text

# For determining whether or not a given page is a redirect
