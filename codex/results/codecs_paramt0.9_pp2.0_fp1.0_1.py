import codecs
codecs.register_error("strict", codecs.ignore_errors)

class JSON:
    def open_file(self, file):
        try:
            reference_file = codecs.open(file, 'r', 'utf-8')
        except:
            reference_file = codecs.open("error_log.csv", "w", "utf-8")
            reference_file.write("Error")
            reference_file.close()
            sys.exit(1)

        return reference_file

    def extract_tag_list(self, line):
        tag_list = list(set(re.findall("<([a-z].*?)>", line)))

        return tag_list

    def extract_tag_content(self, line, tag):
        content = re.findall("<{tag}>([\s\S]*?)</{tag}>".format(tag = tag), line)

        return content

    def refine_string(self, content):
        refined_content = content
        refined_content = re.sub("<[a-z].*?>", "", refined_
