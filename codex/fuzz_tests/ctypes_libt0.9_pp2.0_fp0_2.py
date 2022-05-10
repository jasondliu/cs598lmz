import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(currentAppID)
</code>
@EDIT
I am using Python 3.3 on Windows 10.
@EDIT 2
As requested, this is an example about how my code currently looks like:
<code>import ctypes

def main():
    class WindowSurface(pygame.Surface):
        def __init__(self):
            super().__init__((640, 480))
            self.fill((255, 255, 255))
            pygame.draw.rect(self, (0, 0, 0), (10, 10, 30, 30))
            pygame.draw.rect(self, (255, 0, 0), (20, 20, 30, 30))
            pygame.draw.rect(self, (0, 255, 0), (30, 30, 30, 30))
            pygame.draw.rect(self, (0, 0, 255), (40, 40, 30, 30))
            pygame.display.set_caption("test")
        def update(self):
            pass

    pygame.init
