gi = (i for i in ())
# Test gi.gi_code.co_firstlineno
gi.gi_code.co_firstlineno.should.equal(2)
# Test gi.gi_frame is None
gi.gi_frame.should.equal(None)
# Test gi.gi_running is False
gi.gi_running.should.equal(False)
# Test gi.gi_yieldfrom is None
gi.gi_yieldfrom.should.equal(None)

''' Test gc '''
import gc
# Test gc.get_count
gc.get_count().should.equal((0, 0, 0))
# Test gc.get_debug
gc.get_debug().should.equal(0)
# Test gc.get_threshold
gc.get_threshold().should.equal((700, 10, 10))
# Test gc.get_objects
get_all_objects = [i for i in gc.get_objects()]
len(get_all_objects).should.equal(6)
# Test gc.set_debug
gc.set_debug.called_with(True
