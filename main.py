### Weather Application Programming Interface ###

import tkinter as tk
from tkinter import ttk
from tkinter import font as tkFont

class MyApp(object):
	def __init__(self, arg):
		self.root = root
		self.root.title("Weather API")
		self.root.minsize(400, 230)
		self.root.maxsize(400, 230)

		# Create a style object
		style = ttk.Style()
		# Set the font for the ttk buttons
		style.configure("TButton", font=("Arial", 10))  # Change "Arial" and 10 to your desired font family and size

		# set a fixed window size 
		self.root.geometry("400x230")


		# create frames for the widgets
		self.frame01 = ttk.Frame(root)
		self.frame01.grid(row=0, column=0, sticky='w', pady=(10, 0))

		self.frame02 = ttk.Frame(root)
		self.frame02.grid(row=1, column=0, padx=30, pady=(20, 0))

		self.frame03 = ttk.Frame(root)
		self.frame03.grid(row=2, column=0, padx=(30, 0),pady=(30, 0), sticky='w')

		# create labels for the entry and output windows
		self.entry_label = ttk.Label(self.frame01, text='Enter Location Name')
		self.entry_label.grid(row=0, column=0, padx=(30, 40))

		self.output_label = ttk.Label(self.frame01, text='Output')
		self.output_label.grid(row=0, column=1)

		# create an entry for the location input
		self.entry_location = ttk.Entry(self.frame02)
		self.entry_location.grid(row=0, column=0, padx=(0, 20), sticky='n', pady=(0, 50))

		# create the output display window
		self.output_display = tk.Text(self.frame02, height=5, width=23)
		self.output_display.grid(row=0, column=1, padx=(10, 0))

  		# some buttons
		self.fetch_button = ttk.Button(self.frame02, text='Fetch',width=7)
		self.fetch_button.grid(row=0, column=0, sticky='sw')
		self.parse_button = ttk.Button(self.frame02, text='Parse', width=7)
		self.parse_button.grid(row=0, column=0, padx=(50, 0), sticky='s')

		# more buttons
		self.output_button = ttk.Button(self.frame03, text='Output Data', padding=(25,10))
		self.output_button.grid(row=0, column=0)
		self.reset_button = ttk.Button(self.frame03, text='Reset', padding=(30,10))
		self.reset_button.grid(row=0, column=1, padx=(70, 0))

if __name__ == '__main__':
	root = tk.Tk()
	app = MyApp(root)
	root.mainloop()
