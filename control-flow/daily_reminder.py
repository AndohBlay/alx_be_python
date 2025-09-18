
taskvariable = input("Enter the taskvariable description: ")


priority = input("Enter the taskvariable's priority (high, medium, low): ").lower()

time_bound = input("Is the taskvariable time-bound? (yes or no): ").lower()


match priority:
    case "high":
        reminder = f"Reminder: '{taskvariable}' is a HIGH priority taskvariable."
    case "medium":
        reminder = f"Reminder: '{taskvariable}' is a MEDIUM priority taskvariable."
    case "low":
        reminder = f"Reminder: '{taskvariable}' is a LOW priority taskvariable."
    case _:
        reminder = f"Reminder: '{taskvariable}' has an UNKNOWN priority."


if time_bound == "yes":
    reminder += " This taskvariable requires immediate attention today!"


print(reminder)
