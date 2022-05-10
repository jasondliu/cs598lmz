from bz2 import BZ2Decompressor
BZ2Decompressor.decompress


all_arches = ['x86_64', 'i386', 'arm64', 'armhf']


def _prepare_arch_root(distro_name, distro_ver, arch):
    """ Prepare architecture root tree, install distro kernel """
    arch_root = os.path.join(UNION_ROOT, '%s-%s-%s' % (distro_name,
                                                       distro_ver,
                                                       arch))

    # only need to creat root directory if base not retrieved yet
    if not os.path.isdir(ARCH_BASE_DIR):
        os.makedirs(ARCH_BASE_DIR)

    if os.path.isdir(arch_root):
        # we have a valid root tree, bootstrap into it for updates
        return arch_root, False
    else:
        # need to populate root tree
        return arch_root, True


