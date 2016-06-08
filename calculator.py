current = True 

while current:
    print("1 = Addition")
    print("2 = Subtraction")
    print("3 = Multiplication")
    print("4 = Division")
    print("5 = Exit program")
    option = int(input("Enter number : "))
    if option == 1:
        print("Addition")
        first = int(input("Enter first number :"))
        second = int(input("Enter second number :"))
        result = first + second
        print(first ,'+' ,second ,'=' , result)
    elif option == 2:
        print("Subtraction")
        first = int(input("Enter first number :"))
        second = int(input("Enter second number :"))
        result = first - second
        print(first ,"-" ,second ,"=" , result)
    elif option == 3:
        print("Mmltiplication")
        first = int(input("Enter first number :"))
        second = int(input("Enter second number :"))
        result = first * second
        print(first ,"*" ,second ,"=" , result)
    elif option == 4:
        print("Division")
        first = int(input("Enter first number :"))
        second = int(input("Enter second number :"))
        result = first / second
        print(first ,"/" ,second ,"=" , result)
    elif option == 5:
        print("Quit!")
        current = False
