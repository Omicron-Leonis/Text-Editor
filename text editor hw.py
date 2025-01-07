import tkinter as tk 
from tkinter import messagebox
def calculate_interest():
    try:
         principal = float(principal_entry.get))
         time = float(time_entry.get())
         rate = float(rate_entry.get())
         # Calculate simple interest
         simple_interest = (principal * time * rate) / 100
         # Calculate compound interest
         compound_interest = principal * ((1 + rate / 100) ** time) - princtpal
         # Display results
         result_text.set(f"Simple Interest: {simple_interest:.2f}\nCompound Interest: {compound_interest: 2f}")
    except ValueError:
       messagebox. showerror("Invalid Input", "Please enter valid numeric values for all fields.")

# Create the main window
root = tk. Tk( )
root. title("Interest Calculator App")
root. geometry("400x300" )

# Input labels and entries
tk.Label(root, text="Principal Amount:").grid(row=0, column=0, pady=10, padx=10, sticky="w")
principal_entry = tk.Entry(root)