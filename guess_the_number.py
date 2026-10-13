import random
secret = random.randint(1,100)
while True:
    i = int(input("Enter Your Guess:"))
    if i == secret:
        print("You Won!!!")
    elif  i > secret:
        print("Too High!!!\n Try A Smaller Number")
    else:
        print("Too Low!!!\n Try A Bigger Number")
    print("*" * 20)