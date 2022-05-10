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
view[0] = 1
</code>
The only difference from my original code is that I created a <code>BufferedReader</code> instead of a <code>BufferedWriter</code>.
Is the correct way to close a file to call <code>f.close()</code>, or to explicitly delete the reference to it?


A:

The short answer is yes and no. The longer answer is that <code>close()</code> is part of a "file interface" which is a common pattern in python whereby a close is called to terminate the object. However, python itself doesn't care whether you call <code>close()</code> or not. It will clean up everything in the object when that object goes out of scope.
If you're writing code that will be used by others, I recommend following the idioms of the language and calling <code>close()</code> when you're done with the object. It's good practice, and will make others using your code feel more at home.

