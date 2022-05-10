import codecs
codecs.register_error('strict', codecs.ignore_errors)

class TopicFrame:
	def __init__(self, root_path= "../LDA-topic-Model/documents/", frame_names = 'test_frame.txt', cluster_names = 'test_cluster.txt'):
		#self.file_path = root_path + str(topic_id) + '.txt'
		self.root_path = root_path
		self.frame_names = frame_names
		self.cluster_names = cluster_names
		self.topic_frame = pd.read_table(self.root_path + self.frame_names, encoding="utf-8")
		self.topic_clusters = pd.read_table(self.root_path + self.cluster_names, encoding="utf-8")

	def get_cluster(self, cluster_id):
		data = self.topic_clusters[self.topic_clusters['cluster'] == cluster_id]
		return data['frame']

	def get_frame(self,
