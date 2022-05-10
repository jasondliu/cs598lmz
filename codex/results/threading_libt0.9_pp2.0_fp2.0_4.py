import threading
threading.initialize()
from threading import Thread


frame_dir = 'images/left_up/'
file_list = sorted(os.listdir(frame_dir))


## Update per thread
def update_params(frames, counter):
	global params, num_updates
	curr_params = copy.deepcopy(params)
	for frame_array in frames:
		#print('Updating')
		loss = compute_loss(frame_array)
		gradient = compute_gradient(frame_array)
		curr_params += -lr*np.sign(gradient)
	params = curr_params
	num_updates += len(frames)
	#print('Thread {} loss: {}'.format(counter, loss))

## Thread func
def worker(counter, frames):
	print('Thread {} starting!'.format(counter))
	if update_per == THREAD:
		update_params(frames, counter)
	p_frames = process_frames(frames, counter)
	if update_per == IMAGE:
		for frame_array in
