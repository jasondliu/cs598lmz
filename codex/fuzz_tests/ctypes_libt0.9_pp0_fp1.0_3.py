import ctypes
ctypes.windll.user32.SetProcessDPIAware()
# 直接拖入图片的路径
My_picFile = easygui.fileopenbox(msg='输入图片的路径',default='*',filetypes=["*.jpg","*.png","*.bmp","*.ico","*.gif","*.jpeg"],multiple=True)
My_img = Image.open(My_picFile[0]) # 获取图片
img = np.asarray(My_img)

# 显示图片
plt.figure("imageshow") # 图像窗口名称
plt.imshow(img)
plt.axis('off') # 关掉坐标轴与刻度
plt.show()

# img = img[:, :, ::-1] # 由于pyplot弹出窗口与原
