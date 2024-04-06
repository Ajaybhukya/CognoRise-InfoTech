import random
def roller(max_slides,rolls):
    print("Rolls are:")
    for i in range(rolls):
        print("Roll",i+1,':',random.randint(1, max_slides))
max_slides=int(input("Enter no of slides:"))
rolls=int(input("Enter no of rollls:"))
roller(max_slides,rolls)