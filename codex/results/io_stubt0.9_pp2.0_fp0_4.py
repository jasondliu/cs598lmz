import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f
gc.collect()
print(view)
`,
		`view = None
f = io.BufferedReader(File())
f.read(1)
f = None
gc.collect()
print(view)`,
	},
	Error: "Buffer is not owned by any object",
}

func init() {
	addTestCases(bufferSliceTests, BufferSliceTest)
}
