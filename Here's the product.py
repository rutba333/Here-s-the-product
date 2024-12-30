from tkinter import *

def calculate_product():
    try:
        num1 = int(entry1.get())
        num2 = int(entry2.get())
        result_label["text"] = f"Result: {num1 * num2}"
    except:
        result_label["text"] = "Invalid input!"

# Create the main window
root = Tk()
root.title('getting started with widgets')
root.geometry('400x300')

# Add input fields and button
Label(root, text="First Number:").pack()
entry1 = Entry(root)
entry1.pack()

Label(root, text="Second Number:").pack()
entry2 = Entry(root)
entry2.pack()

Button(root, text="Calculate", command=calculate_product).pack()

# Add a label to show the result
result_label = Label(root, text="Result: ")
result_label.pack()

# Run the app
root.mainloop()
