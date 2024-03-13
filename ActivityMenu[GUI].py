import tkinter as tk
import os

def run_activity():
    root = tk.Tk()
    root.title("Activity Menu")

    def execute_activity(activity_number):
        activity_name = f"Activity{activity_number}.py"
        if os.path.exists(activity_name):
            os.system(f"python {activity_name}")
        else:
            print("Activity not found.")

    def handle_button_click(activity_number):
        if activity_number >= 1 and activity_number <= 5:
            execute_activity(activity_number)
        elif activity_number == 6:
            print("Exiting the Activity.")
            root.destroy()
        else:
            print("Invalid input. Please enter a number from 1 to 6.")

    activity_labels = ['Activity 1', 'Activity 2', 'Activity 3', 'Activity 4', 'Activity 5', 'Exit']
    for i, label in enumerate(activity_labels):
        button = tk.Button(root, text=label, command=lambda i=i: handle_button_click(i+1))
        button.pack()

    root.mainloop()

run_activity()