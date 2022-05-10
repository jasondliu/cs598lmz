import gc, weakref
	ref_list = weakref.WeakSet()

	@safeWrapper
	def check_obj(name):
		ref_list.add(g[name])
		if name in g:
			print('{:30}: {}\n'.format(name, g[name]))
		else:
			# del g[name]
			print('{:30} has been deleted'.format(name))
		print('Number of references from g to objects:', len(ref_list))
		print('\n')

	# check_obj('BH')
	# gc.collect()
	# BH = None
	gc.collect()
	# # check_obj('BH')

	# gc.collect()
	# # CV = None
	# gc.collect()
	# # check_obj('CV')

	# gc.collect()
	# # LCV = None
	# gc.collect()
	# # check_obj('LCV')

	# gc.collect()
	# # new
