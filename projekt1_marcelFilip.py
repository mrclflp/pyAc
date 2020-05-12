# 0 - input

'''
author = Marcel Filip
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]

# 1 - welcome

oddelovac = "="*60

print(oddelovac)
print("Hello! Welcome to Text Analyzer!")
print(oddelovac)

# 2 - login & 3 - auth

registered = {"bob":"123", "ann":"pass123", "mike":"password123", "liz":"pass123"}

while registered:
    username = input("Username: ")
    password = input("Password: ")
    if username in registered and password in registered.values():
        print(oddelovac)
        print("Welcome,", username,"Let's analyze some text!")
        print(oddelovac)
        break
    else:
        print(oddelovac)
        print("Incorrect credentials! Please try again.")
        print(oddelovac)
        continue

# 4 - user choice

print("Following 3 texts are available:")
print(oddelovac)
print("Text #1 >>>")
print(TEXTS[0])
print(oddelovac)
print("Text #2 >>>")
print(TEXTS[1])
print(oddelovac)
print("Text #3 >>>")
print(TEXTS[2])
print(oddelovac)

chosen_text = []

while TEXTS:
    user_choice = int(input("Choose number of the text to analyze: "))
    if user_choice == 1:
        chosen_text = TEXTS[0]
        print(oddelovac)
        print("You've chosen text #1")
        print(oddelovac)
        break
    elif user_choice == 2:
        chosen_text = TEXTS[1]
        print(oddelovac)
        print("You've chosen text #2")
        print(oddelovac)
        break
    elif user_choice == 3:
        chosen_text = TEXTS[2]
        print(oddelovac)
        print("You've chosen text #3")
        print(oddelovac)
        break
    else:
        print("Unfortunately, you've entered wrong number :( Choose again.")
        continue

# 5 - text stats

words = chosen_text.split()

wordsAlpha = 0
wordsNumeric = 0
wordsCapital = 0
wordsUpper = 0
wordsLower = 0

for word in words:
    if word.isnumeric():
        wordsNumeric += 1
        continue
    else:
       wordsAlpha += 1
       continue

for word in words:
    if word.isupper():
        wordsUpper += 1
        continue
    else:
        wordsLower += 1
        continue

for word in words:
    if word[0].isupper():
        wordsCapital += 1
        continue

print("Some basic stats:")
print("There are", wordsAlpha,"words in the text.")
print("There are", wordsNumeric,"strings containing a number in the text.")
print("There are", wordsCapital,"titlecase words in the text.")
print("There are", wordsUpper,"uppercase words in the text.")
print("There are", wordsLower,"lowercase words in the text.")

# 6 - words' length diagram

words_length = dict()

for word in words:
    words_length[len(word)] = words_length.setdefault(len(word), "*") + "*"
    continue

print(oddelovac)
print("Occurence of words' lenghts:")
[print(ln, occ) for ln, occ in sorted(words_length.items())]

# 7 - sum of numbers

sum = 0

for word in words:
    if word.isnumeric():
        sum += int(word)
        continue

print(oddelovac)
print("Sum of numbers from the selected text is:", sum)

# end