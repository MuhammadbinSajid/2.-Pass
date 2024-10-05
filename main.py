for x in range(10): #iterate for loop
    print("Next Iteration\n")
    if x %20 == 0: #condition 1
        print("Twist")

    elif x % 15 == 0: #condition 2
        pass        #passstatement

    elif x % 5 == 0: #condition 3
        print("fizz")   #display result
    
    elif x % 3 == 0: #condition 4 
        print("buzz")

    else:
        print(x)