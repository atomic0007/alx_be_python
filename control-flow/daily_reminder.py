# daily_reminder.py

# Prompt the user for task priority
Priority = input('Priority (high/medium/low): ')

# Process the task based on priority and time sensitivity using a match-case statement
match Priority:
    case 'high':
        if Time_bound == 'yes':
            print(f"Reminder: '{Task}' is a high-priority task that requires immediate attention.")
        else:
            print(f"Reminder: '{Task}' is a high-priority task. Please address it soon.")

    case 'medium':
        if Time_bound == 'yes':
            print(f"Reminder: '{Task}' is a medium-priority task and requires your serious attention.")
        else:
            print(f"Reminder: '{Task}' is a medium-priority task with no time constraints but needs your attention.")

    case 'low':
        if Time_bound == 'no':
            print(f"Note: '{Task}' is a low-priority task. Consider completing it when you have free time.")
        else:
            print(f"Note: '{Task}' is a low-priority task with a time constraint, so allocate some attention to it.")

    case _:
        print("Note: Hey, take a break! There are no tasks to handle.")
