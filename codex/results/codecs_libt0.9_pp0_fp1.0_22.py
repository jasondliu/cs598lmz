import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

def rot_90(x):
   return tf.transpose(x, [0, 2, 1, 3])

def rot_180(x):
   return tf.transpose(x, [0, 1, 3, 2])

def rot_270(x):
   return tf.transpose(x, [0, 3, 2, 1])

def flip_ud(x):
   return tf.reverse(x, [1])

def flip_lr(x):
   return tf.reverse(x, [2])

jigsaw_puzzle_operations = [rot_90, rot_180, rot_270, flip_ud, flip_lr]
jigsaw_puzzle_inv_operations = [rot_270, rot_180, rot_90, flip_ud, flip_lr]
def jigsaw_puzzle_logits(
      x,
      keep_prob,
      num_tasks,
      is_training):
  
