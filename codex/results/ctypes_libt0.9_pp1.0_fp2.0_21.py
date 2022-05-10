import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)


class Main_window():

	def __init__(self, master):
		self.master = master

		self.fecha = datetime.date.today()

		self.abrir_directory = "C:\\Users\\usuario\\Desktop\\Algoritmo\\Receita"

		self.filename1 = "C:\\Users\\usuario\\Desktop\\Algoritmo\\Receita\\"+str(self.fecha)+" "+"Receita.xlsx"
		self.filename2 = "C:\\Users\\usuario\\Desktop\\Algoritmo\\Receita\\"+str(self.fecha)+" "+"Gastos.xlsx"

		self.receita = pd.read_excel(self.filename1)
		self.gasto = pd.read_excel(self.filename2)

		self.acc_1 = 3836.02
		self.acc_2 =
