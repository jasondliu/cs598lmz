import lzma
lzma.decompressor().decompress

 
class Detector:
    def __init__(self, graph_path, labels_path, threshold=.5, gpu_memory_fraction=.3):
        current_path = os.path.dirname(os.path.abspath(__file__))

        # Subtracting some extra to compensate for the GPU memory required by TensorFlow.
        gpu_fraction = gpu_memory_fraction - 0.01
        if gpu_fraction < 0:
            gpu_fraction = 0

        self.threshold = threshold
        self.sess = tf.Session(config=tf.ConfigProto(gpu_options=tf.GPUOptions(per_process_gpu_memory_fraction=gpu_fraction)))

        with tf.gfile.FastGFile(graph_path, 'rb') as f:
            graph_def = tf.GraphDef()
            graph_def.ParseFromString(f.read())
            tf.import_graph_def(graph_def, name='')

        self
