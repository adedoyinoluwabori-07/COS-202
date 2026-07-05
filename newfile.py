
# Create window
root = Tk()
root.title("MATHEMATICAL CALCULATOR (MC)")
root.geometry("400x550")
root.resizable(False, False)
root.configure(bg="lightblue")

# Display screen
screen = Entry(root, font=("Arial", 22), bd=10, relief=RIDGE, justify=RIGHT)
screen.grid(row=0, column=0, columnspan=4, padx=10, pady=20, ipady=10)

# Function to insert numbers/operators
def press(value):
    screen.insert(END, value)

# Function to clear screen
def clear():
    screen.delete(0, END)

# Function to calculate result
def calculate():
    try:
        expression = screen.get()
        expression = expression.replace("^", "**")  # Power
        result = eval(expression)
        screen.delete(0, END)
        screen.insert(END, result)
    except:
        screen.delete(0, END)
        screen.insert(END, "Error")

# Function to turn OFF calculator
def off():
    root.destroy()

# Buttons
buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('%',4,2), ('+',4,3),
    ('^',5,0), ('//',5,1), ('C',5,2), ('=',5,3)
]

# Create buttons
for (text, row, col) in buttons:
    if text == "=":
        Button(root, text=text, width=8, height=3,
               font=("Arial", 12, "bold"),
               bg="green", fg="white",
               command=calculate).grid(row=row, column=col, padx=5, pady=5)

    elif text == "C":
        Button(root, text=text, width=8, height=3,
               font=("Arial", 12, "bold"),
               bg="orange", fg="black",
               command=clear).grid(row=row, column=col, padx=5, pady=5)

    else:
        Button(root, text=text, width=8, height=3,
               font=("Arial", 12, "bold"),
               command=lambda t=text: press(t)).grid(row=row, column=col, padx=5, pady=5)

# OFF Button
Button(root, text="OFF", width=35, height=2,
       font=("Arial", 12, "bold"),
       bg="red", fg="white",
       command=off).grid(row=6, column=0, columnspan=4, pady=15)

root.mainloop()