### Weather Application Programming Interface ###

import tkinter as tk
from tkinter import ttk

class MyApp(object):
	def __init__(self, arg):
		self.root = root
		self.root.title("Weather API")

		# set a fixed window size 
		self.root.geometry("400x200")

		# # create frames for the widgets
		# self.frame01 = ttk.Frame(root)
		# self.frame01.grid(row=0, column=0, padx=30)

		# self.frame02 = ttk.Frame(root)
		# self.frame02.grid(row=1, column=0)

		# self.frame03 = ttk.Frame(root)
		# self.frame03.grid(row=2, column=0)

		# create a label for the entry
		self.entry_label = ttk.Label(self.root, text="Enter location name")
		self.entry_label.grid(row=0, column=0, pady=(10), padx=(20), sticky='w')

		# create an entry for the location input
		self.entry_location = ttk.Entry(self.root)
		self.entry_location.grid(row=1, column=0, padx=20,pady=(0, 0),sticky='n')

		# create the output display window
		self.output_display = tk.Text(self.root, height=5, width=23)
		self.output_display.grid(row=1, column=1, padx=(10, 0))
  	

if __name__ == '__main__':
	root = tk.Tk()
	app = MyApp(root)
	root.mainloop()
