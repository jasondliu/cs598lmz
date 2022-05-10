import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect without GC roots for non-prioritized containers
def no_prio_roots(containers, gc_collect=gc.collect):
    containers_ids = [id(container) for _, container in containers.items()]
    gc_collect()
    collected_containers = {
        name: container
        for name, container in containers.items()
        if id(container) in containers_ids}
    containers_before = repr(collected_containers)
    gc_collect()
    collected_containers = {
        name: container
        for name, container in collected_containers.items()
        if container.data[0] is keepalive_handle} # weak_refs should not unreachable
    gc_collect()
    containers_after = repr(collected_containers)
    assert containers_before == containers_after, (
        'Some ids in %s deleted after collection' % containers_before)

# Test gc.collect without GC roots for prioritized containers
def prio_roots(containers, gc_collect=gc.collect):
   
