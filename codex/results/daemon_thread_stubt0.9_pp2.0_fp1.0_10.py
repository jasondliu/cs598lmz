import sys, threading

def run():
    f = Chain('liquor/reviews.json', 'liquor/reviews_clean.json')
    f.clean()
    
def main (argv):
    run()

if __name__ == "__main__":
    sys.exit(main(sys.argv))
