import bz2
bz2.BZ2File.fileno = lambda x: x.file.fileno()

def main():
    '''
    Reads in, parses, and writes out bz2 compressed file.
 
    Input:  bz2 file containing xml data
    Output: three tab-delimited files:
            i) artists.dat
            ii) albums.dat
            iii) tags.dat
            where the nth line of each file describes the nth artist, album, or tag in the XML file.
 
    '''
 
    with bz2.BZ2File('lastfm_subset.tar.bz2') as file:
        for i, line in enumerate(file):
            element = ET.fromstring(line)
            if element.tag == 'artist':
                artist = element.find('name').text.encode('utf-7').lower()
                with open('artists.dat','a') as artist_out:
                    artist_out.write('%i\t%s\n' % (i, artist))
 
            elif element.
