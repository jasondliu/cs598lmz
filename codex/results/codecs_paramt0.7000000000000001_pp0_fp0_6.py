import codecs
codecs.register_error('replace_with_space', lambda e: (u' ',e.start + 1))

def process_sentence(data):
	text = ""
	for word in data:
		text += word.name + " "

	text = text.strip()
	return text

def process_file(input_file, output_file):
	parsed_file = open(input_file, "r")
	output = open(output_file, "w")

	text_data = parsed_file.read().decode('utf-8', 'replace_with_space')
	parsed_file.close()
	data = json.loads(text_data)

	for sentence in data["sentences"]:
		output.write(process_sentence(sentence) + "\n")

	output.close()

if __name__ == "__main__":
	process_file(sys.argv[1], sys.argv[2])
