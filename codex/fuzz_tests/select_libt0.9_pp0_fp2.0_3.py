import selector_namespace


syntax_list = [
	'python', 'javascript', 'html', 'css', 'rust', 'java', 'c', 'go', 'csharp', 'php', 'apache', 'bash', 'coffeescript', 'cpp', 'cson', 'diff', 'django', 'dockerfile', 'docker_ecosystem', 'emacs', 'erb', 'gfm', 'git', 'haml', 'ini', 'jade', 'javascript_rpde', 'json', 'lua', 'make', 'markdown', 'nginx', 'objectivec', 'pascal', 'perl', 'php_rpde', 'python_rpde', 'rhtml', 'ruby', 'sass', 'scss', 'shell', 'sql', 'stylus', 'swift', '…'
]


class make_syntax_file(sublime_plugin.EventListener):
	def on_post_save(self, view):
		# Check if the syntax file (user) is written in a python file
		syntax = selector_namespace.get_scope
