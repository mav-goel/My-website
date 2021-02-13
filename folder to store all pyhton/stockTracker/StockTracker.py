from tkinter import *
import stcks

def j():

    label1_entry.delete(0, END)

    Date1 = label2_entry.get()
    Stock= label_entry.get()
    Date2 = label3_entry.get()


    Price = stcks.GetStockPrice (Stock, Date1, Date2) 
    label1_entry.insert(END, Price)
    


window= Tk()
window.title("Stock prices")
window.configure(bg = '#6c9491')
window.geometry("400x300")



label = Label(window, text = "What stock")
label.grid (row = 0, column = 0)
label_entry = Entry(window)
label_entry.grid(row = 0, column = 1, pady = 20)

label2 = Label(window, text = "Start date")
label2.grid (row = 1, column = 0)
label2_entry = Entry(window)
label2_entry.grid(row = 1, column = 1)

label3 = Label(window, text = "End date")
label3.grid (row = 2, column = 0)
label3_entry = Entry(window)
label3_entry.grid(row = 2, column = 1, pady = 20)

label1 = Button(window, text = " recieve ", bg = "black", fg = "white", command = j )
label1.grid( row = 3, column = 0, )
label1_entry = Entry(window)
label1_entry.grid(row = 3, column = 1)

window.mainloop()