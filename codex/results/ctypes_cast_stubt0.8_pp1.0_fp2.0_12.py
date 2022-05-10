import ctypes
ctypes.cast(tf_nccl_stream, ctypes.c_void_p).value

nccl_data = {
  "comm": tf_nccl_comm, 
  "stream": tf_nccl_stream
}
nccl_data_path = "/tmp/nccl_data.json"
with open(nccl_data_path, 'w') as fp:
  json.dump(nccl_data, fp)
!cat /tmp/nccl_data.json

# start server
server = tf.train.Server(cluster,
                         job_name=job_name,
                         task_index=task_index,
                         protocol='grpc+verbs',
                         config=config,
                         start=True)


# Start training
if job_name == "ps":
  server.join()
elif job_name == "worker":
  with tf.device(tf.train.replica_device_setter(
    worker_device="/job:worker/task:%d" % 0, cluster=cluster)):
   
