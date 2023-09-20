### Weather Application Programming Interface ###
import tkinter as tk
from tkinter import ttk
from tkinter import font as tkFont
import requests

class MyApp(object):
    
    def __init__(self, arg):
        self.root = root
        self.root.title("Weather API")
        self.root.minsize(500, 250)
        self.root.maxsize(500, 250)

        # Create a style object
        #style = ttk.Style()
        # Set the font for the ttk buttons
        #style.configure("TButton", font=("Arial", 10))  # Change "Arial" and 10 to your desired font family and size

        # set a fixed window size 
        self.root.geometry("500x250")

        # create the frames
        self.frame01 = tk.Frame(self.root)
        self.frame02 = tk.Frame(self.root)
        self.frame03 = tk.Frame(self.root)

        # grid the frames
        self.frame01.grid(row=0, column=0, padx=(20, 20), pady=20, sticky='n')
        self.frame02.grid(row=0, column=1, padx=(0, 20), pady=20, sticky='n')
        self.frame03.grid(row=1, column=0, padx=(20, 0),sticky='w', columnspan=2)

        # label text
        self.label_text = tk.Label(self.frame01, text='Enter location name')
        self.label_text.grid(row=0, column=0, sticky='w')
  
        # entry field
        self.entry_field = ttk.Entry(self.frame01, width=30)
        self.entry_field.grid(row=1, column=0, pady=(10, 20), sticky='w', columnspan=2)

        # fetch data button
        self.fetch_data = ttk.Button(self.frame01, text='Fetch', command=self.fetchData)
        self.fetch_data.grid(row=2, column=0, sticky='w')
  
        # reset button
        self.parse_button = ttk.Button(self.frame01, text='Parse', command=self.parseData)
        self.parse_button.grid(row=2, column=1, padx=(0,0))
  
          # output field
        self.output_field = tk.Text(self.frame02, font=('Verdana', 7), width=35, height=12)
        self.output_field.grid(row=0, column=0)
  
        # Prevent keystrokes
        self.output_field.bind("<Key>", self.ignore_keypress)
  
        # prevent input
        # self.output_field.config(state=tk.DISABLED)
  
        # output data button
        self.output_data_button = ttk.Button(self.frame03, text='Output Data', padding=10, width=25, command=self.outputData)
        self.output_data_button.grid(row=0, column=0)
  
          # reset button
        self.reset_button = ttk.Button(self.frame03, text='Reset', padding=10, width=37, command=self.resetCommand)
        self.reset_button.grid(row=0, column=1, padx=(30, 0))

        ###################################################
        # functionality 
  
    def resetCommand(self):
        self.entry_field.delete(0, tk.END)
        self.output_field.delete('1.0', tk.END)
        # Test code
  
    def fetchData(self):
        apiKey = '065e4fee10f2926dbe94a8df021b63a0'
        base_url = 'https://api.openweathermap.org/data/2.5/weather'
        self.cityName = self.entry_field.get()
  
        parameters= {
            'q': self.cityName,
            'appid': apiKey,
            'units': 'metric'
           }
        if self.entry_field.get() != '':
            self.response = requests.get(base_url, params=parameters)
            self.entry_field.delete(0, tk.END)
            if self.response.status_code != 200:
                self.output_field.insert(tk.END, "No data for such location, please counter check...\n" )
            elif self.response.status_code == 200:
                self.entry_field.delete(0, tk.END)
                self.output_field.insert(tk.END, 'Data has been collected Succesfully...\nParse the data please.\n')
                
        else:
            self.output_field.insert(tk.END, 'Could not fetch data, check input\n')
   
    def parseData(self):
        try:
            if self.response.status_code == 200:
                self.weather_data = self.response.json()
                # Extract the data
                
                if 'main' in self.weather_data:
                    self.temp = self.weather_data['main']['temp']
                    self.output_field.insert(tk.END, 'Data has been parsed succesfully...\n')
                    print("Data")
                    #self.output_field.insert(tk.END, "Temperature:"  + str(weather_data['main']['temp']) + " Celcius \n")
                else:
                    self.output_field.insert(tk.END, 'Data can not be parsed....\n')
        except:
                self.output_field.insert(tk.END, "Could not establish connection....\n")
    
    def  outputData(self):
        if self.response.status_code == 200 and 'main' in self.weather_data:
            self.output_field.insert(tk.END, 'Temperature:{0} Celcius.\n'.format(self.temp))
        else:
            self.output_field.insert(tk.END, 'No temperature data.....\n')
                        
    def ignore_keypress(self, event):
        # Ignore keypress events
        return "break"
    
 
if __name__ == '__main__':
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()


