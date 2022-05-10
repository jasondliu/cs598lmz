import weakref


def test_conversion():
    ctx = Context.create_for_live_video(live_delay=30, audio_format=DIS8u16u32f, video_format=REI420p_8u48u48u88yuv444)
    ctx.run()
    with ctx:
        return video_to_picture(ctx.install_forwarding_output_handler(ctx.display_driver))


class HashTester:
    def __init__(self, fmt):
        self.fmt = fmt
        self.it = iter(range(1024))

    def read_packet(self, buf, pts, dts, flags):
        try:
            next(self.it)
        except StopIteration:
            return b''

        h = sha1(buf).hexdigest()

        return b''.join((m.to_bytes(1, 'big') for m in map(int, h)))


