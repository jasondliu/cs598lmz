import select
import traceback


def get_pixels(frame, gray=False):
    if gray:
        return np.array(frame.getdata(), dtype=np.uint8).reshape(frame.size[1], frame.size[0])
    else:
        return np.array(frame, dtype=np.uint8).reshape(frame.shape[0], frame.shape[1], frame.shape[2])


def resize_and_format(frame, new_width=320, new_height=240, gray=False):
    return get_pixels(frame.resize((new_width, new_height)), gray)


def create_socket(address='0.0.0.0', port=8081, bufsize=1024, ipv4=True, ipv6=False):
    '''
    Creates a listening socket
    '''

    if ipv4 and ipv6:
        s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
