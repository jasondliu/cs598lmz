import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# # 读取图片
# def read_image(image_name):
#     image_path = os.path.join(image_path, image_name)
#     image_data = tf.gfile.FastGFile(image_path, 'rb').read()
#     return image_data

def generate_caption(session, image_model, word_to_idx, idx_to_word, max_length, beam_size, image_filename):

    # load trained model
    saver = tf.train.Saver()
    saver.restore(session, 'model/model.ckpt')


    # get image feature
    image_feature = image_model.get_image_feature(image_filename)

    # generate sentence
    initial_state = session.run(image_model.initial_state)
    initial_beam = Caption(sentence=[word_to_idx['<START>']],

