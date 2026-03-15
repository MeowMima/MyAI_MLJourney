#Let's learn about Pips, Modules, Classes, Objects and Getting Started with OOP!

#18)A. Python Built-In Modules
#import math
#print(math.sqrt(16))

#18)B. Importing my Own Modules
#Refer to Classes_Objects Module for better understanding of this topic

#Importing a Module
#import Classes_Objects       #Classes_Objects is another python file which is imported here as a Module

#itemA = Classes_Objects.Item("Headphones", 2000, 3)     #In classes_objects file/module- 'Item' is a clas & here, 'itemA' has been instatntiated as Object of Item Class
#print(itemA.calc_total_price())                          #where 'calc_total_price()' is a method defined under Item class

#itemA.apply_discount()                                   #'apply_discount()' is also another class defined under the Item class
#print("Discounted Price:", itemA.price)

#ANOTHER WAY - to import a Module
#from lib.Classes_Objects import Item

#instrument= Item("Accoustic Guitar", 3339, 1)
#print(instrument.__dict__)
#print("Original Price per item: ",instrument.price)
#print("Discounted Price per item:", instrument.discount_price)
#print("So your total amount for the purchase is: ", instrument.discount_price*instrument.qty)

#18)C. PIP-Installed(Third-Party) Modules-

#pip install numpy - command- to be written in 'Terminal'-to work with mathematical operations, arrays, and scientific computing

#import numpy as np

#arr = np.array([1, 2, 3, 4, 5])
#print("Numpy Array:", arr)

#19. Accepting Arguments in Python-
#19)A. Console Input(using input()) - when you ask the user for their input in the middle of running the program
#name = str(input("What's your name? "))
#print(f"Oh hey there {name}!")
#age = int(input(f"{name}, now plaese enter your age: "))
#print(f"Great so {name} is {age} years old!")

#19)B. Command-Line Arguments(using sys.argv/argparse) - Here even the input is entered previously before running the program- i.e. fully automated program
#import sys                #It’s like saying: “Hey Python, give me access to the system-level stuff, especially command-line arguments.”

#name = sys.argv[1]    #i.e. Python will print everything on the ouput screen in list form as soon as the arguments are entered on the terminal 

#print("Hello "+name)

#19)C. CLI Professional Way- argparse
import argparse         # built-in Python module (no pip needed) that makes handling command-line arguments easier, cleaner, and professional

parse = argparse.ArgumentParser(                #Creating parse
    description = "A sample greeting program"
)

#Adding Arguments
parse.add_argument("name", help="Your name")
parse.add_argument("age", type=int, help="Your age")

#Parsing Arguments
args = parse.parse_args()

print(f"Hello {args.name}, you're {args.age} years old!")