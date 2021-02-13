from tkinter import * 
from DataBaseBasketball import database

window= Tk()
window.title("Score")
window.geometry("500x500")

db = database("basketball.db")


def calc_total():
    button_entry.delete(0, END)

    if (Gsw_score.get()) > (Tr_score.get()) or  (Gsw_score.get()) > (Cb_score.get()) or (Gsw_score.get()) > (La_score.get()):
        button_entry.insert(END, "Golden State won by - " + str(int(Gsw_score.get()) - int(Tr_score.get()) - int(Cb_score.get()) - int(La_score.get())))

    
    elif (Cb_score.get()) > (Gsw_score.get()) or  (Cb_score.get()) > (Tr_score.get()) or (Cb_score.get()) > (La_score.get()):
        button_entry.insert(END, "Chicago Bulls won by - " + str(int(Cb_score.get()) - int(Gsw_score.get()) - int(Tr_score.get()) - int(La_score.get())))

    elif (Tr_score.get()) > (Gsw_score.get()) or  (Tr_score.get()) > (Cb_score.get()) or (Tr_score.get()) > (La_score.get()):
        button_entry.insert(END, "Toronto Raptors won by - " + str(int(Tr_score.get()) - int(Gsw_score.get()) - int(Cb_score.get()) - int(La_score.get())))
    
    elif (La_score.get()) > (Gsw_score.get()) or  (La_score.get()) > (Cb_score.get()) or (La_score.get()) > (Tr_score.get()):
        button_entry.insert(END, "Lakers won by " + str(int(La_score.get()) - int(Gsw_score.get()) - int(Tr_score.get()) - int(Cb_score.get())))
    
l = Label(window, text = "How many points did each team score??")
l.grid(row = 0, column = 0)


Gsw_label = Label(window, text = "Golden State Warriors",)
Gsw_label.grid(row = 1, column = 0)
Gsw_score = Entry(window)
Gsw_score.grid(row = 1, column = 2)


Cb_label = Label(window, text = "Chicago Bulls")
Cb_label.grid(row = 2, column = 0)
Cb_score = Entry(window)
Cb_score.grid(row = 2, column = 2)


La_label = Label(window, text = "Los Angeles Lakers")
La_label.grid(row = 3, column = 0)
La_score = Entry(window)
La_score.grid(row = 3, column = 2)


Tr_label = Label(window, text = "Toronto Raptors")
Tr_label.grid(row = 4, column = 0)
Tr_score = Entry(window)
Tr_score.grid(row = 4, column = 2)



button = Button(window, text = "Press to see who won", command = calc_total, bg = "orange", fg = "white" )
button.grid(row = 8, column = 0, pady = 20, padx = 20)
button_entry = Entry(window)
button_entry.grid(row = 8, column = 2, ipadx = 30, )


window.mainloop()

