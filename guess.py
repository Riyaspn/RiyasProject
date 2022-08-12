word = "kunna"
i = 1
guess = ""
print("Guess the word,  only 3 chances")
while guess != word and i <= 3:
    guess = input("Enter the word")
    if guess == word:
        print("You won")
    i = i+1
if guess != word:
    print("You lost")
