import ctypes
ctypes.windll.user32.SetProcessDPIAware()

def uniqify(sequence):
    seen = set()
    for x in sequence:
        if x not in seen:
            seen.add(x)
            yield x

def is_alpha(unicode):
    if (ord(unicode) >= 0x4E00 and ord(unicode) <= 0x9FFF):
        return False
    return True

def clip_by_threshold(val, thre):
    if val <= thre:
        return val
    return thre

def shuffle_in_unison_scary(a, b):
    '''
    shuffles input data pair

    a, b: two matrices in shape of (height1, width1, channel1), (height2, width2)
    '''
    rng_state = np.random.get_state()
    np.random.shuffle(a)
    np.random.set_state(rng_state)
    np.random.shuffle(b)

def load_vocab_dict(
