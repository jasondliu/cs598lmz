import select
# Test select.select()

def main():
    print("Testing select.select()")
    r, w, x = select.select([], [], [], 0.0)
    print("select.select() returned r=%s w=%s x=%s" % (r, w, x))

if __name__ == "__main__":
    main()
