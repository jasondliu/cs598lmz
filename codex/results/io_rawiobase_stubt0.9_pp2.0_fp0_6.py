import io
class File(io.RawIOBase):
	def _file_transfer(self,remote,filename,local=None,makedirs=False, callback=None, confirm=False, arg_callback=None, mode='binary'):

		local_dir = os.path.dirname(local)
		if not os.path.exists(local_dir):
			if makedirs:
				os.makedirs(local_dir, exist_ok=True)
			else:
				raise IOError('Path not exists.local_dir:{}'.format(local_dir))

		if not local or local == '-':
			# use stdout
			outfile = sys.stdout.buffer
			validate = False
		else:
			outfile = open(local, 'wb')
			validate = True

		def _close_callback(infile, outfile, validate, bytes_so_far):
			# close all file objects after transfer
			infile.close()
			outfile.close()
