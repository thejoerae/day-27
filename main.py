from tkinter import *

def button_clicked():
    #print(my_label.config(text="Button Got Clicked"))
    print(my_label.config(text=input.get()))


# gives us a window
window = Tk()
# calls title
window.title("My First GUI Program")
#padding
window.config(padx=100, pady=200)

# sizing
window.minsize(width=500, height=300)


#label
my_label = Label(text="Bite Me!", font=("Arial", 24, "bold"))
# packed - in the center of the program
#my_label.pack()
#my_label.place(x=100, y=200)
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

my_label["text"] = "New Test"
# or
my_label.config(text="New Text")

#button
button1 = Button(text="HONK!", command=button_clicked)
button1.grid(column=1, row=1)
#button.pack()

button2 = Button(text="HONK!", command=button_clicked)
button2.grid(column=2, row=0)

#Entry

input = Entry(width=10)
#input.pack()
input.grid(column=3, row=3)
# return the input as a string
print(input.get())






# keeps window on screen - always at the end
window.mainloop()






