import sys, threading
threading.Thread(target=lambda:sys.stdout.write('')).start()
sys.path.append('../')
import os
#os.environ['CUDA_VISIBLE_DEVICES']=''
import generate
import tf_util
import model as model_

def main():
    print('main begins')
    tf.reset_default_graph()
    with tf.device('/gpu:' + str(0)):
        #with tf.Session(config=tf.ConfigProto(log_device_placement=True)) as sess:
        with tf.Session() as sess:
            with tf.device('/gpu:' + str(0)):
                learning_rate=7e-4
                ### only update encoder
                # epoch=5
                # batch_num=5
                # s_lr=7e-4
                ### update encoder and decoder
                epoch=25
                batch_num=10
                s_lr=6e-3
                model = model_.Model(sess,batch_num,learning_rate)
                #saver = tf.train.Saver(var
