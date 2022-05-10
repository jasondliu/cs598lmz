from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(urlopen("http://psf.upfronthosting.co.za/public/books/programming/python/ormm/en/ormm.bz2").read()).decode("utf-8")


"""
Extra feature request:
- I wrote:

   ```
   Ormm is a utility that converts OLAP cubes in memory 
   to a SQL database store. It's pronounced like "awesome".
   ```

   You wrote:

   ```
   Ormm is a utility that converts a SQL database store to 
   an OLAP cube in memory. It's pronounced like "awesome".
   ```

This would make ormm a cube reader: 
https://en.wikipedia.org/wiki/OLAP_cube#Building_cube_structures

So `ormm` would be an acronym for `OLAP RMM reader`.

But in my book, `ormm` is a cube writer. 
So I would like to know if you do cube writing with `ormm`.

Extra feature request (v2.0):

I took the liberty
