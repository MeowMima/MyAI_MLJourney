#14. FUNCTIONS

#def hello(name, age):     #'def' keyword-to define a func; 'hello'-name of the func;'()'- define parameters(as in str/int/ets. type var) ':'- start of the func block   
#    print("Hello ", name, ", you're", str(age), "years old!")             

#hello("Mimansa", 21)      #calling the function

#a different way - Formatting "using 'f"-string ' - BEST PRACTICE - Most Pythonic Way
#def helloHello(nme, ag):
#    print(f"Hello {nme}, you're {ag} years old!")

#helloHello("Mimansa", 21)            

#But,but,but - remember to use it this way if you are-
#def helloLadiesnGentlemen(name_is, age_old):
#    print("Hello " + name_is+ ", you're "+str(age_old)+" years old")        #as we're using '+' operator/ 'concatenation' operation- which is a method of 'sting' so we need to conver int data type into string- type casting

#helloLadiesnGentlemen("Mimansa", 21)

#taking user input in a function
#nme = input("What's your good name?")
#Body
#def my_func(name):

#    print("Hello",name)
#Main Program
#my_func(nme)

#'return' - keyword to basically allow Python to return some information
#def cube(num):
#    return num*num*num
#Main Program
#print(cube(3))

#Nested Function- func inside a func
#def talk(phrase):
#    def say(word):
#        print(word)

#    words = phrase.split(' ')
#    for word in words:
#        say(word)

#Recursion - function calling itself
#Factorial of a number-
#def factorial(n):
#    if n==1:
#        return 1
#    return n* factorial(n-1)
#Main Program/Function Call
#print(factorial(6))

#talk("This is a Nested Function created to break a sentence into words!")

#14. IF-ELIF-ELSE STATEMENTS
#ADVANCED CALCULATOR
#import math
#print("________________________________________________")
#print("CALCULATOR")
#print("________________________________________________")
#3print("List of operations")
#print("_ _ _ _ _ _ _ _ _ _ _ _ _ _  _ _ _ _ _ _ _ _ _ __ ")
#print("1. Addition")
#print("2. Subtraction")
#print("3. Multiplication")
#print("4. Quotient")
#print("5. Remainder")
#print("6. Power")
#print("_ _ _ _ _ _ _ _ _ _ _ _ _ _  _ _ _ _ _ _ _ _ _ __ ")
#num = int(input("Which operation do you like to perform out of the given list? "))
#a = float(input("Please enter first number:"))
#b = float(input("Please enter second number:"))
#main program using if-elif-else
#if num==1:
 #   print("Sum is :", a+b)
#elif num == 2:
 #   if a>b:
  #      print("Difference is: ",a-b)
   # else:
    #    print("Difference is: ",b-a)
#elif num==3:
 #   print("Product is: ", a*b)
#elif num==4:
 #   print("Quotient is: ", a/b)
#elif num==5:
 #   print("Remainder is: ", a%b)
#elif num==6:
 #   print("Power is: ", math.pow(a,b))
#else:
 #   print("Please enter a valid choice!")
#print("Thank You!") 

#15. LOOP - 'for - range', 'while' & ''while-true' instead of 'do-while''
#i = [1,2,3,4,5]
#for j in i:
#    print("Hello dirty fella!")
#for x in range(0,5):
#    print(x)
#print(list(range(11))) #same for 'tuple', but not for 'set' or 'dictionary' since they aren't callable aobjects
#list = [0,1,2,3,4,5]
#empty = []
#for item in list:              |
 #   empty.append(item**2)      |
#print(empty)                  \/(all this in one line)
#empty = [item**2 for item in list]
#print(empty)

#while guess!=sec_wrd and not(out_of_guesses):
 #   if guess_count < guess_lim:
  #      guess = input("\n So what do you think, what could be the impostor's mobile phone brand?: ")
   #     guess_count+=1
        #if guess!=sec_wrd:
         #   print("What you thought, my deadass system has forever for a dumbass like you, Hurry Up Dumb shit, you only got", (guess_lim-guess_count), "turns left :p")
    #else:
     #   out_of_guesses = True
      #  print("Idiot, you ran out of guesses!")
#if out_of_guesses:
 #   print("HAHH, I knew you got an IQ of a bottle cap Loser!")
#else:
 #   print("No need to jump just yet Whore, my Dumbass novice programmer doesn't know anything beside hello world!")

#16. LAMBDA EXPRESSION ,MAPPING('map()' keyword), FILTERING('filter()' keyword), REDUCING('reduce()' keyword) - global funcs to work on aollections

#16)A. lambda expressions/lambda functions/anonymous function(funcs with no name)
#t = lambda var: var*2   #lambda fun is assigned to var 't'
#print(t(6))

#16)B. Map Function
#numbers = [1,2,3]      #a lsit named 'numbers' is created
#[def double(a):          #a function named 'double' is created
#    return a*2
#double = lambda a: a*2] ----> Thus instead of going through so many lines of code
#result = map(lambda a: a*2,numbers)   #we just used lambda func in 1 line
#print(list(result))      #we have to print the output in the form of the listt or the memory location of the output will be printed


#16)C. Filter Function
#res = filter(lambda n: n%2==0, numbers)
#print(list(res))

#16)D. Reduce Function
#from functools import reduce

#expenses = [('Mall', 57), ('Salon', 30)]
#sum = reduce(lambda a,b: a[1]+b[1], expenses)
#print(sum)

#17. Try-Except Block
#try:
#    num = int(input("Enter an integer:"))      #'Try' block where a piece of code is trial run for an exception
#    print(num)
#except ValueError as e:                         #Remember to define what type of error it is - 'ValueError'ZeroDivisionError', so that the system will look for that speciifc type of error only
#    print("Invalid Input")                      #'Except' block is run when an exception is caught by the system
#    num = int(input("Please enter an integer:"))
#    print("The entered integer is ",num)
#else:
#    print("The program has 0 errors")
#finally:
#    print("This is the 'finally' block which will run no matter an exception is there or not")

#try:
#    raise Exception("An Error!")
#except Exception as error:
#    print(error)

#class NoErrorProgramException(Exception):
 #   pass

#try:
#    raise NoErrorProgramException()
#except NoErrorProgramException:
#    print("Error not found!")