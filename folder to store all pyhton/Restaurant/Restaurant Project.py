from tkinter import * # Askterisk means everything.

#making cost of each item a variable

b_price = 2.50
s_price = 1.50
p_price = 3.00

#calculates price of quanitity times cost




def calc_total():
    button_entry.delete(0, END)
    button_entry.insert(END, int(b_quantity.get()) * b_price + int(s_quantity.get()) * s_price + int(p_quantity.get()) * p_price)
    

#window function
window = Tk()

#size of panel

window.geometry("500x500")

#window title
window.title("Menu")

label = Label(window, text = "Restaurant Ordering System")
label.grid(row = 0, column = 0)

#label means words
b_label = Label(window, text = "1. Burger")
b_label.grid(row = 1, column = 0)
#where the words go
b_quantity = Entry(window)
b_quantity.grid(row = 1, column = 2)
# same as above
s_label = Label(window, text = "2. Sandwich")
s_label.grid(row = 2, column = 0)
s_quantity = Entry(window)
s_quantity.grid(row = 2, column = 2)

#same as abovev
p_label = Label(window, text = "3. pizza")
p_label.grid(row = 3, column = 0)
p_quantity = Entry(window)
p_quantity.grid(row = 3, column = 2)

#a button is a pressable button that you can use for working out the total
button = Button(window, text = "Click to see total  £", command = calc_total )
button.grid(row = 8, column = 0, pady = 20, padx = 20)
button_entry = Entry(window)
button_entry.grid(row = 8, column = 2)




# main loop is used to make the window appear on the screen constantly
window.mainloop()


