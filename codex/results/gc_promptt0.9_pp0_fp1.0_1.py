import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
hdr = _testcapi.test_gc_runs
hdr.hdr_cnt = 0
hdr.hdr_has_finaliser = 0
hdr.hdr_finaliser_cnt = 0
hdr.hdr_finaliser_raise = 0
hdr.hdr_finaliser_ran = 0
hdr.hdr_destructor_cnt = 0
hdr.hdr_destructor_raise = 0
hdr.hdr_destructor_ran = 0
hdr.hdr_rawmalloc_cnt = 0
hdr.hdr_rawmalloc_fail = 0
hdr.hdr_getdealloc_func_fail = 0
hdr.hdr_get_make_func_fail = 0
hdr.hdr_rawrealloc_cnt = 0
hdr.hdr_rawrealloc_fail = 0
hdr.hdr_rawfree_cnt = 0
hdr.hdr_rawfree_unknown = 0
hdr.hdr_rawfree_wrong_hdr = 0
hdr
