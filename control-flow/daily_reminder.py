# daily_reminder.py

# Prompt the user for input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process the task based on priority and time sensitivity using a match-case statement
match priority:
    case "high":
        reminder_message = f"Reminder: '{task}' is a high priority task"
    case "medium":
        reminder_message = f"Reminder: '{task}' is a medium priority task"
    case "low":
        reminder_message = f"Note: '{task}' is a low priority task. Consider completing it when you have free time."
    case _:
        reminder_message = "Invalid priority entered."

# Modify the message based on time sensitivity
if time_bound == "yes":
    reminder_message += " that requires immediate attention today!"
elif time_bound == "no":
    reminder_message += " but it's not time-sensitive."

# Print the final reminder
print(reminder_message)
