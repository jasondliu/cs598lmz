import gc, weakref

class UncollectableClass:
    def __del__(self):
        print('not collectable!')
        super().__del__()

