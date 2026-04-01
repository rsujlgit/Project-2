print("Welcome to the Pattern Generator and Number Analyzer! ")

while True:
    print("Select an option : ")
    print("1.Genrate a Pattern")
    print("2.Analyze a Range of Number")
    print("Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        Num = int(input("enter the number of rows for the patterns : "))
        print("patterns")
        for i in range(1,Num+1):
            print("*" * i)

    elif choice ==2:
        start = int(input("Enter your range: "))
        end = int(input("Enter your range: "))
    
        even =[]
        odd = []
        total_sum = 0
        count = 0

        for num in range(start,end+1):
            if num %2== 0:
                even.append(num)
            else:
                odd.append(num)

            total_sum += num
            count += 1
        print("\n even number:",even)
        print("odd number:",odd)
        print("total Number:",count)
        print("sum:",total_sum)

    elif choice == 3:
        print("Exiting the program..")
        break

    else:
        print("invaid choice please try again and keep work hard..")
