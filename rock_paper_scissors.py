# Made by Devroop Banerjee
# Play rock, paper, scissors against a computer and keep track of score

import random

user_score = 0
cpu_score = 0
options = ['rock', 'paper', 'scissors']

while True:
	user_input = input("\nType rock/paper/scissors or q to quit\n").lower()

	if user_input == "q":
		break

	if user_input not in options:
		continue

	r_num = random.randint(0,2)	# rock:0, paper:1, scissors:2
	cpu_input = options[r_num]
	print("CPU picks", cpu_input)

	if (user_input == 'rock' and cpu_input == 'scissors') or (user_input == 'paper' and cpu_input == 'rock') or (user_input == 'scissors' and cpu_input == 'paper'):
		print("You win!")
		user_score +=1

	elif (user_input == 'rock' and cpu_input == 'paper') or (user_input == 'paper' and cpu_input == 'scissors') or (user_input == 'scissors' and cpu_input == 'rock'):
		print("CPU wins!")
		cpu_score +=1

	else:
		print("Tied!")

print("\nThe final score is:\nYou: "+str(user_score)+"\nCPU: "+str(cpu_score))