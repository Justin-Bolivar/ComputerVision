import os

def run_activity():
    while True:
        print('[1] - Activity 1\n[2] - Activity 2\n[3] - Activity 3\n[4] - Activity 4\n[5] - Activity 5\n[6] - Exit\n')
        user_input = input("Enter Activity number: ")
        
        if user_input.isdigit():
            activity_number = int(user_input)
            
            if activity_number >= 1 and activity_number <= 5:
                activity_name = f"Activity{activity_number}.py"
                
                if os.path.exists(activity_name):
                    os.system(f"python {activity_name}")
                else:
                    print("Activity not found.")
            elif activity_number == 6:
                print("Exiting the Activity.")
                break
            else:
                print("Invalid input. Please enter a number from 1 to 6.")
        else:
            print("Invalid input. Please enter a number.")

run_activity()