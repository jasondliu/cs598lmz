import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect does not finalise collectable objects which are weakly referenced

class Obj:
    pass

def finalise1(obj, has_finaliser):
    print("Running finaliser 1")
    if has_finaliser:
        raise Exception("Finaliser should not have been run!")
    print("Finaliser 1 completed")

class TestBase:
    def __init__(self, ref, *args):
        self.obj = args
        self.ref = ref

    def test_fn(self, force_no_collection):
        if force_no_collection:
            return True

        # Try and induce a collection before finalisers are run.
        print("Collecting ...")
        gc.collect()
        try:
            gc.collect()
        except AttributeError:
            pass

        # Check the weak reference is still alive
        weaked = self.ref()
        print("Is weak ref alive?", weaked is not None)
        if weaked is not None:
            print(weaked)
            return True

        return False

class TestParentHandle(TestBase):

