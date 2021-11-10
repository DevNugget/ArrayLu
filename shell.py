# Loop variable
running = True

# Main control array
main_array = []

# Extending array function
def add_array_instance(instances_num):
	for i in range(instances_num):
		main_array.append(0)

# Contracting array function
def deduct_array_instance(num):
	for i in range(num):
		main_array.remove(main_array[-1])

# Input loop
while running:
	user_input = input(">> arr lu >> ")
	input_content = user_input.split()

	keyword = input_content[0]

	if keyword == "ar":
		if input_content[1] == "ext":
			add_array_instance(int(input_content[2]))

		elif input_content[1] == "mul":
			if input_content[2] != "loo":
				main_array[int(input_content[2])] *= int(input_content[3]) # ar add 1 5

			elif input_content[2] == "loo":
				loo_list = [x*int(input_content[3]) for x in main_array] # ar add loo 4
				main_array = loo_list

		elif input_content[1] == "div":
			if input_content[2] != "loo":
				main_array[int(input_content[2])] /= int(input_content[3]) # ar add 1 5

			elif input_content[2] == "loo":
				loo_list = [x/int(input_content[3]) for x in main_array] # ar add loo 4
				main_array = loo_list

		elif input_content[1] == "defu":
			print("defualt array load")
			print("")

			main_array = [0, 0, 0, 0, 0, 0, 0, 0]

		elif input_content[1] == "ded":
			deduct_array_instance(int(input_content[2]))

		elif input_content[1] == "add":
			if input_content[2] != "loo":
				main_array[int(input_content[2])] += int(input_content[3]) # ar add 1 5

			elif input_content[2] == "loo":
				loo_list = [x+int(input_content[3]) for x in main_array] # ar add loo 4
				main_array = loo_list

		elif input_content[1] == "sub":
			if input_content[2] != "loo":
				main_array[int(input_content[2])] -= int(input_content[3]) # ar sub 1 5

			elif input_content[2] == "loo":
				loo_list = [x-int(input_content[3]) for x in main_array] # ar sub loo 4
				main_array = loo_list

		elif input_content[1] == "set":
			if input_content[2] != "loo":
				main_array[int(input_content[2])] = int(input_content[3])
			
			elif input_content[2] == "loo":
				count = 0
				for i in main_array:
					main_array[count] = int(input_content[3])
					count += 1

		elif input_content[1] == "loo":
			loo_func = input(">> arr lu > sub > loo fnc >> ")
			loo_input = loo_func.split()

			if loo_input[0] == "add":
				for i in range(int(input_content[2])):
					main_array[int(loo_input[1])] += int(loo_input[2]) # ar add 1 5
			if loo_input[0] == "sub":
				for i in range(int(input_content[2])):
					main_array[int(loo_input[1])] -= int(loo_input[2])
			if loo_input[0] == "mul":
				for i in range(int(input_content[2])):
					main_array[int(loo_input[1])] *= int(loo_input[2])
			if loo_input[0] == "div":
				for i in range(int(input_content[2])):
					main_array[int(loo_input[1])] /= int(loo_input[2])

		elif input_content[1] == "byt":
			if input_content[2] == "str":
				if input_content[3] == "prt":
					string = ''

					counter = 0

					for i in main_array:
						string += str(chr(main_array[counter]))
						counter += 1

					print(string)
					print("")

		elif input_content[1] == "ins":
			print("this will override arr, continue? (y/n)")
			insert_text = input(">> arr lu > sub > ins fnc >> ")
			if insert_text == "y":
				print("confirmed")
				insert_text = input(">> arr lu > sub > ins fnc >> ")
				insert_list = insert_text.split()
				for i in range(0, len(insert_list)):
					insert_list[i] = int(insert_list[i])

				main_array = insert_list

		elif input_content[1] == "cls":
			print("this will clear arr, continue? (y/n)")
			confirmation = input(">> arr lu > sub > cls fnc >> ")
			if confirmation == "y":
				main_array = []

		elif input_content[1] == "prt":
			pass

	elif keyword == "qu":
		quit()

	else:
		print("syntax error")

	print("\n" + str(main_array) + "\n")