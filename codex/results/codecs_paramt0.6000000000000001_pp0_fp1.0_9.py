import codecs
codecs.register_error('ignore', codecs.lookup_error('ignore'))

# http://stackoverflow.com/questions/20716842/python-download-images-from-google-image-search
def get_soup(url,header):
    return BeautifulSoup(urllib2.urlopen(urllib2.Request(url,headers=header)),'html.parser')

def main(args):

    parser = argparse.ArgumentParser(description='Scrape Google images')
    parser.add_argument('-s', '--search', default='bananas', type=str, help='search term')
    parser.add_argument('-n', '--num_images', default=10, type=int, help='num images to save')
    parser.add_argument('-d', '--directory', default='/home/s1478785/Documents/Projects/ImageNet/', type=str, help='save directory')
    args = parser.parse_args()

    query = args.search#raw_input(args.search)
    max_images = args.num_images

