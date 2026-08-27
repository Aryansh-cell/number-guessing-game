import random 
num = random.randint(0, 100)

print("=======================================================")
print("                NUMBER GUESSING GAME                   ")
print("=======================================================")
print("I am thinking of number between 0 and 100")
print("You have 10 attempts!")

count = 0
for i in range(101):
    count += 1
    guess = int(input(f"Attempt {count}/10 Guess: "))

    if guess > num:
        print("lower please")
    
    if guess < num:
        print("higher please")
        
    if num == guess:
        print(f"You guessed the number in {count} guesses.")
        print("YOU WON 🎉")
        break

    if count >= 10:
        print(f"Game over!!!\nThe number was {num}\nYOU LOSE 😢")       
        break
    


    