import bz2
bz2.decompress(b'BZh91AY&SY\xc4\x00\x00\x00\x01\x01\x80\x00\x00 \x007\x80Q\x07\xe78\xef&lt;\x82r\xe0\x1e\xf1#\x80\xff\xbf\xbf\xc0\x00\x00\x01&lt;\t\x00\x00\x00\x97\xc8'
</code>
I'm not sure what I am doing wrong here. (As a side note, I am always willing to be educated on why giving a zip archive with a single folder and a single file did not unzip nicely to a directory: that was another thing that gave me a headache)


A:

I figured it out. I didn't realize that I had to put the archive from Dropbox into a variable to use it. It shouldn't make a difference but it does, sooooooo yeah . . . 

