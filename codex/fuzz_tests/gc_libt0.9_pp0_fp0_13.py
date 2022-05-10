import gc, weakref, operator

#voxel engine
import voxelengine

class Cubes(voxelengine.Engine):
    def __init__(self, width, height, depth):
        voxelengine.Engine.__init__(self, width, height, depth)
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        size = (width, depth, height)
        self.lines = list()
        self.lines.append(voxelengine.EngineHelper.linesForBox(width, depth, height))
        self.lines += voxelengine.EngineHelper.linesForBox(width, depth, height, (1,1,1), (1,1,1))
    def draw(self):
        pygame.event.pump()
        self.screen.fill((255, 255, 255))
        for line in self.lines:
            pygame.draw.lines(self.screen, (255, 0, 0), True, line, 2)
        pygame.display.flip()
import time
if __
