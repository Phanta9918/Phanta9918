#let's make a simple quiz game...

print("Welcome to my computer quiz!")

playing = input("Do you want to play? (yes/no) ")
if playing != "yes":
	quit()

print("Okay! Let's play :)")
score = 0
print("score = 0")

answer = input("What does GH stand for? ")
if answer.lower() == "glizzy hands":
	print("Correct!")
	score += 1
else:
	print("Ah-h-h, that's not the right answer...")
	cont = input("Would you still like to continue with this quiz? (yes/no) ")
	if cont == "no":
		print("Current score: " + str(score))
		quit() 

answer = input("In Smash, what character does 'Big A' play? ")
if answer.lower() == "sheekh":
	print("Correct!")
	score += 1
else:
	print("Incorrect!")
	cont = input("Would you still like to continue with this quiz? (yes/no) ")
	if cont == "no":
		print("Current score: " + str(score))
		quit()

answer = input("Which twitch emote was inspired by a Hitman level? ")
if answer.lower() == "back to paris":
	print("Correct!")
	score += 1
else:
	print("Ah-h-h, that's not the right answer...")
	cont = input("Would you still like to continue with this quiz? (yes/no) ")
	if cont == "no":
		print("Current score was " + str(score))
		quit()

answer = input("What is Atrioc's favorite drink? ")
if answer.lower() == "coffee":
	print("Correct!")
	score += 1
else:
	print("Ah-h-h, that's not the right answer...")
	cont = input("Would you still like to continue with this quiz? (yes/no) ")
	if cont == "no":
		print("Current score: " + str(score))
		quit()

answer = input("Who is Ari's Husband? ")
if answer.lower() == "atrioc":
	print("Correct!")
	score += 1
else:
	print("Shucks... that's not the right answer")
	cont = input("Would you still like to continue with this quiz? (yes/no) ")
	if cont == "no":
		print("Current score " + str(score))
		quit()

answer = input("What game did Atrioc mald at? ")
if answer.lower() == "all of the above":
	print("Correct!")
	score += 1
else:
	print("Tough luck... that's not the answer")
	cont = input("Would you still like to continue with this quiz? (yes/no) ")
	if cont == "no":
		print("Current score: " + str(score))
		quit()

print("...")
print("...")
print("...")

end = input("Congratulations, you have completed the Atrioc quiz? Would you like to play the game again? (yes/no) ")
if end == "yes":
	print("then make your own game...")
else:
	print("You got " + str(score) + " questions correct!")
	quit()

#it's a success!








