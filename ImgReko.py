from tkinter import ttk
import tkinter as tk
from ttkthemes import ThemedTk
import webbrowser
import Rekog


#Main Window - Main Container
window = ThemedTk(theme="equilux")
window.geometry('400x250')
window.title('Image Recognition App')

backFrame = tk.Frame(window, width=400, height=250, background="#255FEF")
backFrame.pack()

mainFrame = ttk.Frame(window, width=390, height=240)
mainFrame.pack(fill=None, expand=False)
mainFrame.place(relx=0.013,rely=0.015)
global pic, vehicle
pic = tk.StringVar()
vehicle = tk.StringVar()
resultObt = tk.StringVar()
resultLabel = ttk.Label(mainFrame, textvariable = resultObt, font = ("Bold", 15))
resultLabel.pack()
resultLabel.place(relx = 0.5, rely = 0.45)



#eLink function, when executed it looks for the type of vehicle on Google Images
def eLink(e):
    vehicle.set(e.widget.get())
    link = 'https://www.google.com/search?q=' + vehicle.get() + '&rlz=1C1CHBF_enNZ763NZ763&sxsrf=ALeKk01bg-n7DJDmgZ-iATp3d27P1DzNdQ:1584143394995&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiX1dOC0pjoAhVqxDgGHTGMAFMQ_AUoAXoECA8QAw'
    webbrowser.open(link)
    vhcle.set(vehicle.get()[0].upper() + vehicle.get()[1:])

#unitTest function, when executed it gets the image's link and then executes the Unit Test
def test(e):
    link = e.widget.get()
    pic.set(link)
    result = Rekog.rekog(pic.get(), vehicle.get())
    resultObt.set('Vehicle detected:\n "' + result[0].upper() + result[1:] + '"')
    e.widget.delete(0, 'end')

# #Please enter the Type of Vehicle
t = tk.StringVar()
vLabel = ttk.Label(mainFrame, textvariable=t)
vLabel.pack()
vLabel.place(relx = 0.05, rely = 0.15)
t.set('Please enter the Type of Vehicle:')
#Title
titleT = tk.StringVar()
title = ttk.Label(mainFrame, textvariable=titleT, font=("Bold", 17))
title.pack()
title.place(relx=0.2, rely=0.025)
titleT.set('Image Recognition App')
#ToV Entry
ToV = ttk.Entry(mainFrame)
ToV.pack()
ToV.place(relx = 0.5, rely = 0.15, width = 170)
ToV.bind("<Return>", eLink)

#Please paste link here
text = tk.StringVar()
linklbl = ttk.Label(mainFrame, textvariable = text)
linklbl.pack()
text.set("Please paste link here:")
linklbl.place(relx = 0.05, rely = 0.25)

#Link Entry
imageLink = ttk.Entry(mainFrame)
imageLink.pack()
imageLink.place(relx = 0.5, rely = 0.25, width = 170)
imageLink.bind("<Return>", test)

#Type of Vehicle
exp = tk.StringVar()
expected = ttk.Label(mainFrame, textvariable = exp)
expected.pack()
exp.set("Type of Vehicle:")
expected.place(relx = 0.05, rely = 0.35)

#Result Obtained
rslt = tk.StringVar()
result = ttk.Label(mainFrame, textvariable = rslt)
result.pack()
rslt.set("Result Obtained:")
result.place(relx = 0.5, rely = 0.35)

#Vehicle
vhcle = tk.StringVar()
vehicleLbl = ttk.Label(mainFrame, textvariable = vhcle, font=("Italic",15))
vehicleLbl.pack(fill = None)
vehicleLbl.place(relx = 0.05, rely=0.45)

#Quit Button
quitbtn = ttk.Button(mainFrame, text = 'Quit', command = window.destroy)
quitbtn.pack()
quitbtn.place(relx = 0.05, rely=0.85)

window.mainloop()