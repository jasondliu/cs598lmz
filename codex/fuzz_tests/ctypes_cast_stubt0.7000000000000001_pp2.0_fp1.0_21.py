import ctypes
ctypes.cast(data, ctypes.POINTER(ctypes.c_float))
mv = np.ctypeslib.as_array(data)
# format the array
mv = mv.reshape(shape[::-1])

# plot 
import matplotlib.pyplot as plt
plt.imshow(mv)
plt.show()
</code>
Output:


