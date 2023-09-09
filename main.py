### Weather Application Programming Interface ###

import tkinter as tk
from tkinter import ttk

class MyApp(object):
	def __init__(self, arg):
		self.root = root
		self.root.title("Weather API")

		# set a fixed window size 
		self.root.geometry("400x200")

		# create frames for the widgets
		self.frame01 = ttk.Frame(root)
		self.frame01.grid(row=0, column=0, padx=20, pady=10)

		self.frame02 = ttk.Frame(root)
		self.frame02.grid(row=1, column=0)

		self.frame03 = ttk.Frame(root)
		self.frame03.grid(row=2, column=0)

		# create an entry for the location input
		self.entry_location = ttk.Entry(self.frame01)
		self.entry_location.grid(row=0, column=0, padx=(0, 20))


if __name__ == '__main__':
	root = tk.Tk()
	app = MyApp(root)
	root.mainloop()
