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
print(view[0])
</code>
In the C code I tried this:
<code>/*. This file is part of pykdgrav.
 *
 * pykdgrav is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * pykdgrav is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with pykdgrav.  If not, see &lt;http://www.gnu.org/licenses/&gt;.
 *
 *
 * Created by Matt Spraggs on 13/03/2020.
 *
 *
 *
 * */

#include &lt;Python
