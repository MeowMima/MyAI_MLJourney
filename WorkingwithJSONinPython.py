#JSON - Javascript Object Notation

import json        #part of the std libraries/built-in libraries in Python

"""
#Below is a small snippet to understand working with '.json' files

people_info = '''
{ 
    "people": [
        {
            "name" : "Mimansa",
            "phone" : "9812345609",
            "email" : "abcdmmmm@hotmail.com",
            "has_license" : true
        },
        {
            "name" : "Shawtyyy",
            "phone" : "6678290653",
            "email" : "divadiva@yahoo.com",
            "has_license" : false
        }

    ]
}
'''

data = json.loads(people_info)
#print(type(data))                            # a <class 'dict'> data type

for person in data["people"]:                 #much readable way to get data
    #print(person)

    del person["phone"]

new_peopleInfo = json.dumps(data, indent=2, sort_keys=True)     #to dump data from a python script to a 'json' file
print(new_peopleInfo)

"""

with open('IndianStates.json') as f:
    data = json.load(f)            #Note - '.load()' method - for file objects. '.loads()' method - for string data types

"""
#to print the data
for region in data["regions"]:
    print(region)
"""

#to del a data
for region in data["regions"]:
    del region['pin_code_range']

#to dump the formatted file
with open('New_IndianStates.json', 'w') as f:
    json.dump(data, f, indent=2)