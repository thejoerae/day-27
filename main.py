from tkinter import *

# gives us a window
window = Tk()
# calls title
window.title("My First GUI Program")

# sizing
window.minsize(width=500, height=300)


#label
my_label = Label(text="Bite Me!", font=("Arial", 24, "bold"))
# packed - in the center of the program
my_label.pack()

my_label["text"] = "New Test"
# or
my_label.config(text="New Text")

def button_clicked():
    #print(my_label.config(text="Button Got Clicked"))
    print(my_label.config(text=input.get()))


button = Button(text="HONK!", command=button_clicked)
button.pack()

#Entry

input = Entry(width=10)
input.pack()
# return the input as a string
print(input.get())






# keeps window on screen - always at the end
window.mainloop()






