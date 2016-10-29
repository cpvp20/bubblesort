def sortit(numbers):
    for i in range(len(numbers)):
        if i[1]>i[2]:
            i[1],i[2]=i[2],i[1]
    return(numbers)

#ACTIAL CODE
x=list(input("type some integers randomly, separating them with spaces "))
#creates a list with the numbers the user gives
y=[int(i) for i in range(len(x))]#turns list of str into list of int
sortit(y) #sort the list of int
