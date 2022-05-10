import sys, threading
threading.Thread(target=lambda:sys.stdout.write("\r%i"%i)).start()

def read_image(image_name):
    image = tf.read_file(image_name)
    #read the file as raw bytes
    image = tf.image.decode_image(image, channels = 3)
    image = tf.image.convert_image_dtype(image, dtype=tf.float32)
    image = image* 2 - 1
    return image

def compute_gram_matrix(image):
    img_tensor = tf.reshape(image, [-1, image_size, image_size, 3])
    #compute the gram of a matrix
    #input: image 2x2x3
    #output: gram matrix 2x2 3x3 flattened
    #tf.transpose(a, perm=None, name='transpose')
    #Transposes a. 
    #perm is an optional list of <int> permutation of the dimensions of input.
    #output: 3x2x2
    #tf.linalg.matmul(a,
