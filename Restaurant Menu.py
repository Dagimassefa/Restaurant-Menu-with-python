from tkinter import *
from tkinter import messagebox
window=Tk()
listbox=Listbox(window,bg="#f7ffde",font=("Constantia",30),width=15,selectmode=MULTIPLE)
def submit():
    # order=listbox.get(listbox.curselection())
    food=[]
    for i in listbox.curselection():
        food.insert(i,listbox.get(i))
    # print("You have orderd the following:")
   
    for foodlist in food:
         messagebox.showinfo(title="You have orderd the following items!",message=foodlist)
   # print("You have ordered "+order)
def AddItem():
    listbox.insert(listbox.size(),entrybox.get())
    listbox.config(height=listbox.size())
def RemoveItem():
    for i in reversed(listbox.curselection()):
        # listbox.delete(i)
        if (messagebox.askyesno(title="WARNING",message="Do you want to remove this item?")):
            messagebox.showinfo(title="Removing Item",message="Item has been removed!")
            listbox.delete(i)
        else:
            break
    listbox.config(height=listbox.size())
listbox.pack()
listbox.insert(1,"Pizza")
listbox.insert(2,"Pasta")
listbox.insert(3,"Salad")
listbox.insert(4,"Soup")
listbox.insert(5,"Burger")
listbox.config(height=listbox.size())
entrybox=Entry(window)
entrybox.pack()
AddItem=Button(window,text="Add to the menu",command=AddItem)
AddItem.pack()
RemoveItem=Button(window,text="Remove from the menu",command=RemoveItem)
RemoveItem.pack()
submit=Button(window,text="Submit",command=submit)
submit.pack()
window.mainloop()