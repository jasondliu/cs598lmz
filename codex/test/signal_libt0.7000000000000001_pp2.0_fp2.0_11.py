import signal
signal.signal(signal.SIGINT, signal.SIG_DFL) 


def main():
	root = tk.Tk()
	root.title("Python e-puck manager")
	root.geometry('250x170')

	# Icon
	root.iconbitmap(default='../images/pymobility_icon.ico')
	
	# Create the notebook
	nb = ttk.Notebook(root)
	nb.grid(row=1, column=0, columnspan=50, rowspan=49, sticky='NESW')

	# List of the different tabs
	tabControl = {}
	tabControl["tabStart"] = tk.Frame(nb, borderwidth=3, relief="groove")
	tabControl["tabMap"] = tk.Frame(nb, borderwidth=3, relief="groove")
	tabControl["tabSim"] = tk.Frame(nb, borderwidth=3, relief="groove")
	tabControl["tabControl"] = tk.Frame(nb, borderwidth=3, relief="groove")
	tab
