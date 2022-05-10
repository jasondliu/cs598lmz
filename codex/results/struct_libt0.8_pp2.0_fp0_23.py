import _struct
# 存放车辆的列表
cars = []

# 车辆类
class Car(object):
	# 初始化车辆，默认参数是0
	def __init__(self, id=0, color='', time=0):
		self.id = id
		self.color = color
		self.time = time
	# 获取车辆的信息
	def getInfo(self):
		print("车辆:%d  颜色:%s 进入时间:%d"%(self.id, self.color, self.time))
	# 获取车辆的停留时间
	def getTime(self):
		return _struct.gettime() - self.time

# 添加车辆
