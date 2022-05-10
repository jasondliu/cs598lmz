import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

def main():
    s = sys.argv[1]
    print(s)
    f = codecs.open(s, 'r', 'utf-8')
    try:
        lines = f.readlines()
    except UnicodeError:
        print("Unicode error")
    finally:
        f.close()
    for line in lines:
        print(line)

if __name__ == "__main__":
    main()
