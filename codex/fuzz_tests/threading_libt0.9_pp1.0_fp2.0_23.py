import threading
threading.stack_size(32768)

checkpoint_file = "./model.data-00000-of-00001"

model = Model()
model.load()

global_step = model.global_step
global_step_lock = threading.Lock()
write_op = tf.summary.merge_all()
writer = tf.summary.FileWriter('./logs', sess.graph)

def train(input):
    batch_size = 0
    prev_global_step = 0
    while batch_size < 20000000:
        # 從 queue 取 batch_size 數量的 rgb/dep
        images, depths = model.step(input, batch_size)
        # 執行模型
        cost, _, summaries = sess.run([model.cost, model.train_op, write_op], 
                                        feed_dict = {model.images : images,
                                            model.depths : depths})
        print cost
        writer.add_summary(summaries, global_step =
