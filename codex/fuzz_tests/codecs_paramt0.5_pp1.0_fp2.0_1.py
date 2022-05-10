import codecs
codecs.register_error('ignore', ignore_errors)

def find_files(path, ext):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(ext):
                yield os.path.join(root, file)


def extract_text(path):
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
        soup = BeautifulSoup(content, 'html.parser')
        for script in soup(["script", "style"]):
            script.extract()
        text = soup.get_text()
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = '\n'.join(chunk for chunk in chunks if chunk)
        return text


def get_content(path):
    content = extract_text(path)
    return content


def main():
    path = "./data/html"
    output_
