import threading
threading.stack_size(2**27)


class InputChannel(object):
	"""InputChannel Establishes communication between the Processors and their input ports,
		by creating a Channel Object which is a combination 
			of a 'queue' (for keeping the buffer of input) and 
			of a 'socket' (for fetching data from the outside world)
			of a 'fetching thread' (for getting packets from the socket's buffer)
	"""

	def __init__(self, log, input_params, next_processor, output_channels):
		self.log = log
		self.input_params = input_params
		self.next_processor = next_processor
		self.output_channels = output_channels
		self.packet_capture = pcapy.open_live(input_params['port'], 65536, 1, 1)
		self.input_queue = queue.Queue(input_params['buffer_size'])
		self.source_ip = input_params['source_ip']
	
