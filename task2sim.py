import tkinter as tk
from tkinter import messagebox

# Function to perform calculation
def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                messagebox.showerror("Error", "Cannot divide by zero.")
                return
            result = num1 / num2
        else:
            messagebox.showerror("Error", "Select a valid operation.")
            return

        result_label.config(text=f"Result: {result}")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

# GUI Window
window = tk.Tk()
window.title("Simple Calculator")
window.geometry("300x300")
window.configure(bg="#f0f8ff")

# Input Fields
tk.Label(window, text="Enter first number:", bg="#f0f8ff", font=("Arial", 10)).pack(pady=5)
entry1 = tk.Entry(window, font=("Arial", 12))
entry1.pack()

tk.Label(window, text="Enter second number:", bg="#f0f8ff", font=("Arial", 10)).pack(pady=5)
entry2 = tk.Entry(window, font=("Arial", 12))
entry2.pack()

# Operation Dropdown
tk.Label(window, text="Select operation:", bg="#f0f8ff", font=("Arial", 10)).pack(pady=5)
operation_var = tk.StringVar(window)
operation_var.set("+")  # Default value
operations = tk.OptionMenu(window, operation_var, "+", "-", "*", "/")
operations.config(font=("Arial", 12))
operations.pack()

# Calculate Button
calculate_button = tk.Button(window, text="Calculate", command=calculate, font=("Arial", 12), bg="#007acc", fg="white", padx=10, pady=5)
calculate_button.pack(pady=10)

# Result Label
result_label = tk.Label(window, text="Result: ", font=("Arial", 12, "bold"), bg="#f0f8ff")
result_label.pack(pady=10)

# Run the application
window.mainloop()