
import tkinter as tk
from tkinter import messagebox

total_seats = 10
seats = [None] * total_seats  # None means seat is free

def show_seats():
    seat_status = ""
    for i, name in enumerate(seats, start=1):
        status = f"Booked by {name}" if name else "Available"
        seat_status += f"Seat {i}: {status}\n"
    text_area.config(state=tk.NORMAL)
    text_area.delete(1.0, tk.END)
    text_area.insert(tk.END, seat_status)
    text_area.config(state=tk.DISABLED)

def book_seat():
    try:
        seat_num = int(entry_seat.get())
        name = entry_name.get().strip()
        if seat_num < 1 or seat_num > total_seats:
            messagebox.showerror("Error", "Invalid seat number.")
            return
        if not name:
            messagebox.showerror("Error", "Please enter a name.")
            return
        if seats[seat_num - 1] is not None:
            messagebox.showerror("Error", "Seat already booked.")
            return
        seats[seat_num - 1] = name
        messagebox.showinfo("Success", f"Seat {seat_num} booked for {name}.")
        entry_seat.delete(0, tk.END)
        entry_name.delete(0, tk.END)
        show_seats()
    except ValueError:
        messagebox.showerror("Error", "Seat number must be an integer.")

# Create the main window
root = tk.Tk()
root.title("Ticket Booking System")

# Seat status display
text_area = tk.Text(root, height=12, width=40, state=tk.DISABLED)
text_area.pack(pady=10)

# Input for seat number
frame = tk.Frame(root)
frame.pack(pady=5)
tk.Label(frame, text="Seat Number (1-10):").grid(row=0, column=0)
entry_seat = tk.Entry(frame, width=5)
entry_seat.grid(row=0, column=1)

# Input for customer name
tk.Label(frame, text="Your Name:").grid(row=1, column=0)
entry_name = tk.Entry(frame, width=20)
entry_name.grid(row=1, column=1)

# Book button
btn_book = tk.Button(root, text="Book Seat", command=book_seat)
btn_book.pack(pady=10)

# Show initial seats
show_seats()

root.mainloop()
