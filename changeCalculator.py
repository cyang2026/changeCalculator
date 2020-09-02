print("Welcome to this change calculator!")
print("Just enter the cost, how much you paid, and I'll return the quarters, dimes, nickels, and pennies you'll need.")
print("First enter the total cost...")
cost = input()
print("Great! Now enter how much you've paid...")
paid = input()
change = paid - cost
num_dollars = change // 1
change -= (num_dollars * 1)
num_dollars = int(num_dollars)
if num_dollars > 1:
    print(str(num_dollars) + " dollars")
elif num_dollars == 1:
    print(str(num_dollars) + " dollar")
if change != 0:
    num_quarters = change // .25
    change -= (num_quarters * .25)
    num_quarters = int(num_quarters)
    if num_quarters > 1:
        print(str(num_quarters) + " quarters")
    elif num_quarters == 1:
        print(str(num_quarters) + " quarter")
    if change != 0:
        num_dimes = change // .10
        change -= (num_dimes * .10)
        num_dimes = int(num_dimes)
        if num_dimes > 1:
            print(str(num_dimes) + " dimes")
        elif num_dimes == 1:
            print(str(num_dimes) + " dime")
        if change != 0:
            num_nickels = change // .5
            change -= (num_nickels * .5)
            num_nickels = int(num_nickels)
            if num_nickels > 1:
                print(str(num_nickels) + " nickels")
            elif num_nickels == 1:
                print(str(num_nickels) + " nickel")
            if change!= 0:
                num_pennies = change * 100
                num_pennies = int(num_pennies)
                if num_pennies > 1:
                    print(str(num_pennies) + " pennies")
                elif num_pennies == 1:
                    print(str(num_pennies) + " penny")
