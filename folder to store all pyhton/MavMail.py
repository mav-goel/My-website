import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from tkinter import *

#def h ():
#    print(From_entry.get())

def h():
    msg = MIMEMultipart()


    msg['From'] = From_entry.get()
    msg['To'] = To_entry.get()
    msg['Subject'] = Subject_entry.get()
    Message = Message_entry.get("1.0" , "end-1c")

    msg.attach(MIMEText(Message, "plain"))
    email = "mavgoel@gmail.com"
    password = ""
    Mail = smtplib.SMTP('smtp.gmail.com',587)
    Mail.ehlo()
    Mail.starttls()
    Mail.login(email, password)
    text = msg.as_string()
    Mail.sendmail("mavgoel@gmail.com", "drtarungoel@gmail.com", text)
    Mail.quit()



window= Tk()
window.title("Mav Email Services")
window.geometry("700x700")

From = Label(window, text = "From - ",  )
From.grid(row = 1, column = 0)
From_entry = Entry(window)
From_entry.grid(row = 1, column = 2)


To = Label(window, text = "to - ")
To.grid(row = 2, column = 0, pady = 20)
To_entry = Entry(window)
To_entry.grid(row = 2, column = 2)


Subject = Label(window, text = "subject - ")
Subject.grid(row = 3, column = 0,pady = 5)
Subject_entry = Entry(window)
Subject_entry.grid(row = 3, column = 2)

Message = Label(window, text = "message - ")
Message.grid(row = 4, column = 0)
Message_entry= Text(window, width = 16, height = 9)
Message_entry.grid(row = 4, column = 2)

send = Button(window, text = "SEND", padx = 20, pady = 20, command = h)
send.grid(row = 5, column = 3, pady = 30, padx = 30)

#From = From_entry.get()
#To = To_entry.get()
#Message = Message_entry.get("1.0" , "end-1c")
#Subject = Subject_entry.get()




window.mainloop()