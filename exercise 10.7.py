#making try-except-else block with while loop
while True:
    try:
        a = int(input("enter number 1: "))
        b = int(input("enter number 2: "))
    except ValueError:
        print("This is not an integer!!!")
    else:    
        answer = a + b
        print(answer)