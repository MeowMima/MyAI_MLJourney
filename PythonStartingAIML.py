#BASICS OF PYTHON

# - this symbol represents comment in Python
# There's no specific multiline comments in Python
"""
THIS IS A DOCSTRING
GIVES AN ILLUSION OF A MULTILINE COMMENT IN PYTHON
AND PYTHON DOESN'T GIVE ANY OUTPUT FOR THIS
"""

#print("Hello Pyhton in VSCode!") #this statement is used to print outputs on the output screen   

#Fundamentals of Python

#1. VARIABLES & KEYWORDS
#nme = "MeowMima" 
#int a = 10 #int - 'keyword for integers'
#if = "Darla" #Error since 'if' is a control statement keyword

#2. EXPRESSIONS & STATEMENTS
#5+3 #Expression
#int b = 5+3 #Statement

#3. Programs and Indentation in Python
#if(a == b):
 #   print("True")
#else:
 #   print("False")
#An 'if-else' statement to show 'Indentation suggesting division of Python programs in blocks of code

#4. DATA TYPES
#Let's see the data type of 'nme' variable-
#print(type(nme))
#TypeCasting - let's make our string data type to integer
#num = 20
#qty = int(num)
#print(isinstance(qty, int)) #boolean value is returned(refer to notes to understand boolean values
#num = "yo"
#greet = int(num)
#print(isinstance(greet, int))
#doesn't really work if you would want to convert a string value into integer- why? - because by type casting, Pythpn tries extracting the specified data type out of the entered value, which is apparently not their in a string data type


#5. STRINGS - ' '/" " (' ' - also for characters, single words)
#name = "Mimansa"
#line = """ This is a
#multiline string """
#letUsprint = name + line
#print(letUsprint)

#6. BOOLEANS
#done = True
#if done:
 #   print("yes")
#else:
 #   print("no")
#print(bool(0))        # False
#print(bool(3.14))     # True
#print(bool(""))       # False
#print(bool("hello"))  # True
#print(bool([]))       # False
#print(bool([1,2]))    # True
#print(bool({}))       # False
#print(bool({"x":10})) # True
#print(bool(None))     # False

#7. Numeric - complex numbers
#num1 = 2+3j #can be represented just as represented in simple mathematics
#num2 = complex(3,2)  #can be represented as set, where 1st value is a real number, and the second value will be imaginary
#print(num1.real, num1.imag)
#print(num2.real, num2.imag)

#8. Enumeration- For constants
#from enum import Enum
#class State(Enum):
 #   INACTIVE = 0
  #  ACTIVE = 1
#Usage
#print(State.ACTIVE)
#print(State.ACTIVE.name)
#print(State.ACTIVE.value)

#9. CONTROL STATEMENTS - break/continue/pass
#for i in range(0,5):
#    if i == 4:
#        break
#    elif i == 3:
#        continue
#    else:
#        pass
#    print(i," ")

#10. LISTS & LIST COMPREHENSIONS
"""
dogs = ["Nick", 1, "Cassie", "Tory", 3] #defining a list
print(dogs[0]) #getting the 1st element(or 0th index element) of the list

dogs[3] = 2    #updating 4th element(or 3rd index) in the list
print(dogs)    #updated list will be printed

print(dogs[2:]) #slicing of list
dogs.append("Ceaser") #adding an extra element to the end of the list
print(dogs)

dogs.extend(["Ceaser", 44]) #adds elements as lists in the already existing list 
print(dogs)
dogs += ["Ceaser", 44]     #does the same as '.extend' built-in method #\n print(dogs)

dogs.remove(dogs[6])        #removing an item in the list
print(dogs)

print(dogs.pop())       #remove the last element added in the list and print - 44
print(dogs)             #print the newly updated list after removing the last element added i.e. w/o 44

dogs.insert(4, "Tory")   #to insert an elemnt at any index in a list- remember only 2 values can be passed in this built-in method; 1st val- index(always), 2nd val- elem
print(dogs)
"""
"""
#Sorting a list- we can only sort same data type elements in a list, so we'll create a new list-
#Sorting 'str' data type list(based on ASCII Value)
senseOrg = ["Eyes", "Ears", "Nose", "Tongue", "Skin"]
print("Original List:", senseOrg)
senseOrg.sort()
print("Sorted List:", senseOrg)
senseOrgCopy = senseOrg[:]
print("Copied List:", senseOrgCopy)
#Sorting 'numeric' data type
num = [2, 6.99, -8, 2+3j]  #system does not compare simple and complex numbers
num = [2, 6.99, -8]
print("Original:", num)
print("Sorted:", sorted(num))
"""
"""
#NESTED LIST
nest = [1,2,3,[4,5,['target']]]
print(nest[3][2][0])            #At 3rd index - nested list([4,5,['target']]), At 2nd index of the nested list - (['target']), At 0 index - 'target'
myList[0] = 'New'
print("The mutated list is - ",myList)   #List is Mutable
"""
"""
#Getting Started with List Comprehensions
nums = [1,2,3,4,5,6,7,8,9,10]
#To get n*n for each element in the given list

#1st Method - By Iterartion
my_list=[]
for n in nums:
    my_list.append(n*n)
print(my_list)

#2nd Method - List Comprehension
my_list=[n*n for n in nums]
print(my_list)

#3rd Method - Map & Lambda Fn
#Map - used to run through the elements of the list using a certain fn, mostly a lamda fn
# Lambda  Fn- an anonymous fn
my_list = map(lambda n: n*n, nums)
print(list(my_list))
"""

"""
#Filter & Lambda Function
nums = [34,45,56,9002,85,51]
my_list = filter(lambda n: n%2==0, nums)  #'map' fn here will give boolean values, while 'filter' fn here gives exact elements 
print(list(my_list))
"""

#11. TUPLES
#dogs = ("Tory", "Bob", "Hachi", "Beck") #notice the diffrence in syntax, for tuples- parantheses('()') is used
#print("Original Tuple:", dogs)
#i = dogs.index("Hachi") 
#print(i)
#print(dogs[2])
#print(dogs.count("Hachi"))  #frequency of the occurence of the elements in the tuple
#print("No. of elemnets in the tuple:", len(dogs))
#print("Sorted Tuple:", sorted(dogs))

#12. DICTIONARIES & DICTIONARY COMPREHENSIONS
#dogs={"name":"Hachi", "breed": "Japanese Akita", "age":8, "furCol":"White-Brown"}
#print(dogs.keys())     
#print(dogs.values())
#print(dogs.items())
#print(list(dogs.keys()) , list(dogs.values()))     #to get output in a list format
#print(list(dogs.items()))      #instead of individually practicing converting dict into list, we can just use '.items()' built-in method/func
#dogs["Origin Country"] = "Japan"    #to add an item in the dictionary
#print(list(dogs.items()))
"""
#To match up superheroes with their first names
names = ['Bruce', 'Clark', 'Peter']
supeheroes = ['Batman', 'Superman', 'Spiderman']

# Method -1: Iteration 
for i in range(len(names)):
    for j in range(len(supeheroes)):
        if i==j:
           print(names[i], supeheroes[j])
        elif i==1:             #when we don't want Clark
            break
        else:
            continue

# Method -2: 'Zip' Fn - gives a list format
print(list(zip(names, supeheroes)))

# Method-3: Dictionary Comprehension
my_dict = {names:supeheroes for names, supeheroes in zip(names,supeheroes) if names!='Clark'} #we can also put cond in dict comprehensions
print(my_dict)

"""

#13. SETS & SET COMPREHENSIONS
#Set - Collection of unique values
"""
marvel = {"Iron Man", "Thor", "Hulk", "Captain America", "Black Widow", "Spider-Man"}
marvel.pop()   #very random
print(marvel)

print("Marvel Universe:", list(marvel))
dc = {"Batman", "Superman", "Wonder Woman", "Flash", "Aquaman", "Cyborg"}
print("DC Universe:", list(dc))

#Operations on Sets-
superheroes = marvel | dc    #to get 'union' of the two sets
common = marvel & dc         #to get 'intersection' of the two sets
print(common)                #o/p = 'set()' i.e. empty set since no common superheroes in both the universe
avengers = marvel - dc      
print(avengers)              #o/p = marvel superheroes only
justiceLeague = dc - marvel
print(justiceLeague)        #o/p = dc superheroes only
"""
"""
#Getting started with Set Comprehensions
#to create a set of the given list of numbers, 'nums'

nums = [1,1,2,2,1,3,4,3,4,5,5,6,7,8,7,9,9]

#Method 1 - Using loop
my_set = set()
for n in nums:
    my_set.add(n)
print(my_set)            #o/p- {1,2,3,4,5,6,7,8,9}

#Method 2 - Using Set Comprehension
my_set = {n for n in nums}
print(my_set)
"""
#14. GENERATOR FUNCTIONS & GENERATOR EXPRESSIONS
"""
#Generator Function
#to loop through a given range of numbers
def my_range(start, end):
    current = start
    while current <= end:
        yield current
        current += 1

nums  = my_range(1,10)
print(list(nums))

#through 'for' loop
for num in nums:
    print(num, end = " ")


#Generator Expression
nums = [1,2,3,4,5,6,7,8,9,10]
#to yield n*n for each element of 'nums'

#Method 1 - Using 'Loop'
for i in nums:
    print(i**2, end = " ")

#Method 2 - Using 'gen' func
def gen_func(nums):  #creating the func
    for n in nums:
        yield n*n

my_gen = gen_func(nums)   #making obj for gen_func()

for i in my_gen:
    print(i, end = " ")

print(list(my_gen))          #or simply print out the result in the list format without any loop
"""

#15. ITERATORS & ITERABLES
"""
#Iterable - something that can be iterated/repeated (e.g. A list, a func block, a tuples, a string, a file/ an object)
#To check for iteration - if the object has a method '__iter__()'(a special/dunder method) to be able to repeat

#An 'iterator' - can be uderstood as an object with a state so that it can remember where it is during the process of 'iteration'
#To check for iterator - if the objcet has a method '__nect__()'(a special method to remeber it's current memory space)(e.g. a 'list' is not an iterator as there is no '__next__()' method)

nums = [1,2,3,4] 
#print(dir(nums))            #just 'iterable' 
i_nums = iter(nums)          #or nums.__iter__(), thus converting 'list' data type an 'Iterator'

while True:
    try:
        item = next(i_nums)
        print(item,end = " ")
    except StopIteration:
        break
#An 'Iterator' can only go forward
#An 'Iterator' can go on forever

#Making a whole 'class' Iterator
class MyRange:

    def __init__(self, start, end):
        self.value = start
        self.end = end
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current
    
nums = MyRange(1, 10)

for num in nums:
    print(num, end = " ")
"""


