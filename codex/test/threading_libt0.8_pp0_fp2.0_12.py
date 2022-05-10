import threading
threading.stack_size(67108864) # 64MB stack

class model:
	def __init__(self,model_number):
		self.model_number = model_number
		self.lower_bound = 0
		self.upper_bound = 0
		self.x_values = []
		self.y_values = []

	def set_lower_bound(self, lower_bound):
		self.lower_bound = lower_bound
		return

	def set_upper_bound(self, upper_bound):
		self.upper_bound = upper_bound
		return

	def set_x_values(self, x_values):
		self.x_values = x_values
		return

	def set_y_values(self, y_values):
		self.y_values = y_values
		return

	def get_model_number(self):
		return self.model_number

	def get_lower_bound(self):
		return self.lower_bound

