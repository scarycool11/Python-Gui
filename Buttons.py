from tkinter import * 
root = Tk()
root.title("Calculator")

myButton1 = Button(root, text="1", width=10, height=5)
myButton1.grid(row=4, column=1)

myButton2 = Button(root, text="2", width=10, height=5)
myButton2.grid(row=4, column=2)

myButton3 = Button(root, text="3", width=10, height=5)
myButton3.grid(row=4, column=3)

myButton4 = Button(root, text="4", width=10, height=5)
myButton4.grid(row=3, column=1)

myButton5 = Button(root, text="5", width=10, height=5)
myButton5.grid(row=3, column=2)

myButton6 = Button(root, text="6", width=10, height=5)
myButton6.grid(row=3, column=3)

myButton7 = Button(root, text="7", width=10, height=5)
myButton7.grid(row=2, column=1)

myButton8 = Button(root, text="8", width=10, height=5)
myButton8.grid(row=2, column=2)

myButton9 = Button(root, text="9", width=10, height=5)
myButton9.grid(row=2, column=3)

myButton0 = Button(root, text="0", width=10, height=5)
myButton0.grid(row=5, column=1)

myButtonMul = Button(root, text="X", width=10, height=5)
myButtonMul.grid(row=2, column=4)

myButtonDiv = Button(root, text="%", width=10, height=5)
myButtonDiv.grid(row=1, column=4)

myButtonEqual = Button(root, text="=", width=10, height=5)
myButtonEqual.grid(row=5, column=4)

myButtonAdd = Button(root, text="+", width=10, height=5)
myButtonAdd.grid(row=4, column=4)

myButtonSubtract = Button(root, text="-", width=10, height=5)
myButtonSubtract.grid(row=3, column=4)

myButtonClear = Button(root, text="AC", width=10, height=5)
myButtonClear.grid(row=1, column=1)

myButtonDivision = Button(root, text="/", width=10, height=5)
myButtonDivision.grid(row=1, column=3)




root.mainloop()