import io
class File(io.RawIOBase):
    def __init__(self, conn, fh):
        self.conn = conn
        self.fh = fh
        io.RawIOBase.__init__(self)

    def readable(self):
        return True

    def writable(self):
        return True

    def seekable(self):
        return False
    
    def read(self, size=None):
        if not size:
            size = int(self.conn.get("Content-Length"))
        args = "-i %s --silent --connect-timeout 5  --speed-time 60 --speed-limit 50k --location --max-redirs 5 --user-agent 'Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.46 Safari/536.5' --referer '%s'" %  (self.fh, self.conn.get("Referer"))
        cmd = '%s %s' % (settings.CURL_PATH, args)
        out = os.popen(cmd).
