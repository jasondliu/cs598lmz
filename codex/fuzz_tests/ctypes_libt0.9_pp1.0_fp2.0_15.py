import ctypes
ctypes.cdll.LoadLibrary('bazel-out/local-opt/bin/tensorflow/core/_pywrap_tensorflow_internal.so')
sys.path.append("bazel-out/local-opt/bin")
</code>
However, you'll need to adjust the paths to reflect the file structure of your current build. Alternatively, you could figure out how to build the Cython layer into a Python package and install it into your site-packages folder (which I don't know how to do). This would let you avoid the above code and let you directly import tensorflow.keras as opposed to importing tensorflow.python.keras.

