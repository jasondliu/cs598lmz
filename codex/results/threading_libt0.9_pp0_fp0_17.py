import threading
threading.stack_size(20000*1024)

opt = {
	"flow_path": os.path.join(os.getcwd(), 'hourly_flow'),
	"label_path": os.path.join(os.getcwd(), 'annotation/gytd_train.csv')
}


def make_flow_set():
	print("[INFO] Making flow_set ...")
	# read flow
	for folder in (os.listdir(opt["flow_path"])): 
		folder_path = os.path.join(opt["flow_path"], folder)
		if folder != ".DS_Store":
			for i in range(1, 6): # 5 minute
				flow_name = folder+"_flow_"+str(i)
				flow_path = os.path.join(folder_path, flow_name)
				flow_img = imageio.imread(flow_path)

				# read img
				if i == 1:
					img
