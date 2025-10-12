
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")
print ()

match priority:
	case "high":
		if time_bound =="yes":
			print ("Reminder", task, "is high priority task that requires immediate attention today!")
		else:
			print ("Reminder", task, "is  a high priority task. Try to complete it as soon as possible.")


	case "medium":
		if time_bound == "yes":
			print ("Reminder", task, "is a medium priority task that is time-sensitive. Schedule it today.")
		else:
			print ("Note:", task, "is a medium priority task. Complete it within the next few days.")


	case "low":
		if time_bound == "yes":
			print ("Reminder:", task, "is a low priority but time-bound task. Don't forget to finish it today.")
		else:
			print ("Note:", task, "is a low priority task. Consider completing it when you have free time.")


        case _:
			print ("Invalid priority level. Please enter high, medium, or low.")
