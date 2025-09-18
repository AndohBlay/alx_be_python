task_variable = input("Enter the task description: ")
priority = input("Enter the task's priority (high, medium, low): ")
time_bound = input("Is the task time-bound? (yes or no): ")

match priority.lower():
    case "high":
        reminder = f"URGENT: {task_variable} (Priority: High)"
    case "medium":
        reminder = f"Reminder: {task_variable} (Priority: Medium)"
    case "low":
        reminder = f"Low priority: {task_variable} (Priority: Low)"
    case _:
        reminder = f"Task: {task_variable} (Priority: Unknown)"

if time_bound.lower() == "yes":
    reminder += " — This task requires immediate attention today!"

print(reminder)
