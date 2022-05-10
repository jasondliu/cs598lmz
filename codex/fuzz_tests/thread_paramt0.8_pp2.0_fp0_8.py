import sys, threading
threading.Thread(target=lambda: os.system('python web/web.py')).start()
time.sleep(1)

def ask(question):
	return input(question).lower()

def get_answer(question):
	response = ask(question)
	try:
		return answerDict[response]
	except KeyError:
		print('An unexpected answer was given. Please try again.')
		return get_answer(question)

def start_game(response):
	print('\nWelcome to Who Wants to be a Millionaire!')
	time.sleep(1)
	print('\nThe rules are simple: answer a series of trivia questions to get rich!')
	time.sleep(1)
	print('\nYou\'ll get 4 choices, and you can use 3 lifelines to help you:')
	time.sleep(1)
	print('\n1. Call a friend: ask a friend for help!')
	time.sleep(1)
	print('\n2. 50/50: eliminates 2 of your 4 choices!')
	time.sleep(1)
	
