# thinter module
from tkinter import *
# submodule new theme widgets added in version 8.5
from tkinter import ttk


# global function for calculation of feet to meter 
def calculate(*args):
    
    # error handling, debug aid
    try:
        value = float(feet.get())
        meters.set(int(0.3048 * value * 10000.0 + 0.5)/1000.0)
    except ValueError:
        pass

# Create Application
root = Tk()
root.title("My Application - QLAN DEV")

# creating a Content Frame
mainframe = ttk.Frame(root, padding="3 3 12 12")
# grid places it directly inside the application window
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

# frame should expand to fill any space if resized
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# create Widget
feet = StringVar() # Tkinter variable class, store string values
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
# grid adds widget to frame after creation
feet_entry.grid(column=2, row=1, sticky=(W, E))

# create Widget
meters = StringVar()
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

# for loop to add padding to all child grids
for child in mainframe.winfo_childer():
    child.grid_configure(padx=5, pady=5)

# Focus Cursor on field
feet_entry.focus()

# Run calculate if Return is entered
root.bind("<Return>", calculate)

# event loop, everything appears on screen and allows users to interact with it. 
root.mainloop()
