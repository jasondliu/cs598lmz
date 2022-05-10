import codecs
codecs.register_error('replace_encoding', codecs.replace_errors)

# Displays a unicode string n times
def n_times(n, s):
	return ''.join([s]*n)

# Formats the iTrust output display
def prettify_iTrust_print(message):
	print(n_times(5, '-'))
	if message.strip() != '':
		print(message)
	print(n_times(5, '-'))

# Creates the launch script to run iTrust
def launch_iTrust(java_path=DEFAULT_JAVA_PATH,
				  maven_path=DEFAULT_MAVEN_PATH,
				  app_path=DEFAULT_APP_PATH,
				  lib_path=DEFAULT_LIBS_PATH,
				  launch_script_path=DEFAULT_LAUNCH_SCRIPT_PATH,
				  terminator_path=DEFAULT_TERMINATOR_PATH,
				  eclipse_path=DEFAULT_ECLIPS
