

print("Welcome! To Booking System of Western Indian Railway")
restart = ('Y')

while restart != ('N','NO','n','no'):
	print("1.Check pnr status")
	print("2.Ticket Reservation")
	option = int(input("Enter your option : "))

	if option == 1:
		print("Your pnr status is s2")
		exit(0)

	elif option == 2:
		people = int(input("Enter no. of Ticket you want : "))
		name_l = []
		age_l = []
		sex_l = []
		for p in range(people):
			name = str(input("Name : "))
			name_l.append(name)
			age  = int(input("Age  : "))
			age_l.append(age)
			sex  = str(input("Male or Female : "))
			sex_l.append(sex)

		restart = str(input("Oops! Forget someone : "))
		if restart in ('y','YES','yes','Yes'):
			restart = ('Y')
		else :
			x = 0
			print("Total Ticket : ",people)
			for p in range(1,people+1):
				print("Ticket : ",p)
				print("Name : ", name_l[x])
				print("Age  : ", age_l[x])
				print("Sex : ",sex_l[x])
				x += 1



	