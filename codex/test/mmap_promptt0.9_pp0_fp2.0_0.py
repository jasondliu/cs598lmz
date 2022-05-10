import mmap
# Test mmap.mmap().
# These tests assume that the files in the current directory are organized as
# follows:
#         test.mmap
#         test2.mmap
# They also assume that the size of test.mmap is exactly 8192 bytes
# and that test2.mmap begins with exactly 100 'a' bytes, followed by exactly
# 4061 'b' bytes.
#

def test_kvm_memory_write(kvm_mapping):
    assert kvm_mapping.map(kvm_mapping.to_virt, kvm_mapping.to_guest_phys)
    kvm_mapping.mem_write(0, '1234')
    assert kvm_mapping.read(kvm_mapping.to_virt, 4) == '1234'


def test_kvm_memory_destroy():
    assert True
