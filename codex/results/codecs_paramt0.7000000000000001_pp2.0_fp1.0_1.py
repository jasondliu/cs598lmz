import codecs
codecs.register_error("replace_with_space", codecs.lookup_error("replace"), lambda e:(" ",""))

def read_txt(path):
    with codecs.open(path, encoding="utf-8", errors="replace_with_space") as f:
        text = f.read()
    return text

def write_json(path, data):
    with codecs.open(path, encoding="utf-8", mode="w") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def read_json(path):
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    return data

def write_txt(path, data):
    with codecs.open(path, encoding="utf-8", mode="w") as f:
        f.write(data)

if __name__ == "__main__":
    args = sys.argv
    path = args[1]
    txt = read_txt(path)
    write_txt(path,
