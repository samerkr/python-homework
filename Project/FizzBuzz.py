##BASIC
mylist =list(range(1,101))
##print(mylist)
for i in mylist:
    if (i % 5 == 0) and (i % 3 == 0): print(F" {i} is Multiples of three and five  --FizzBuzz")
    elif i%3 ==0: print(F" {i} is Multiples of three --Fizz")
    elif i % 5 == 0: print(F" {i} is Multiples of five  --Buzz")
    else: print(" "+str(i))
