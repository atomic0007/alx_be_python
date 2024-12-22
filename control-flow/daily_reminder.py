# daily_reminder.py

# Prompt the user for input
Task = input('Enter your task:')

Time_bound =input('Is it time-bound? (yes/no):')

Priority = input('Priority (high/medium/low):')

# Process the task based on priority and time sensitivity using a match-case statement
match Priority:
    case 'high':
        if Time_bound =='yes': 
            print(f' Reminder:{Task} is a {Priority} priority task that requires immediate attention')
    case 'medium':
        if Time_bound =='yes':
            print(f'Reminder:{Task} is a {Priority} priority task and requires your seious attention')
        else:
            print(f'REminder:{Task} is a {Priority} priority task with no time bound therefore requires some level attention')
    case 'low':
        if Time_bound =='no':
            print(f'Note:{Task} is a {priority} task. Consider completing it when you have free time')
        else:
            print(f'Note:{Task} is a {Priority} priority task with time bound therefore requires some level attention')

# Print the final reminder
    case _:
        print('Note: Hey, take a break no more tasks to handle today')
