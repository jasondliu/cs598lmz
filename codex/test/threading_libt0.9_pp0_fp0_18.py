import threading
threading.stack_size(67108864)


def scrabble_threads(sender, word, results):
	while True:
		word_to_check = queue.get()
		matches = find_matches(word_to_check)
		if len(matches) == 1:
			results.append(word_to_check)
			with open('matched_words.txt', 'a') as f:
				f.write(word_to_check + '\n')
		queue.task_done()

def find_matches(word_to_check):
	matches = []
	for key in scrabble_words.keys():
		if all(key.count(l) >= word_to_check.count(l) for l in word_to_check):
			matches.append(key)
	return matches

