## While Loops & For loops ##
# are forms of iterations 
# iterations is the process of repeating or looping through
# a set of steps or instructions 
# to iterate is the verb 
# form of iteration 
# be careful of infinite loops 
# they will crash your program 

#while loop = execute some code WHILE some condition remains true 

##EXAMPLE 1
# name = input('Enter your name: ')

# while name == "":
#     print('Enter your name: ')
    
# print(f"Hello {name}")

##EXAMPLE 2
# age = int(input('Enter your age;'))

# while age <0:
#     print("Age can't be negative")
#     age = int(input("Enter your age: "))

# print(f'You are {age} years old')

##EXAMPLE 3

# food = input("enter a food you like (q to quit):")

# while not food == "q": 
#     print(f'You like {food}')
#     food = input("Enter another food you like (q to quit): ")

# print('Bye')

##EXAMPLE 4

# num = int(input(' Enter a # between 1-10: '))

# while num < 1 or num > 10:
#     print(f"{num} is not valid")
#    num + int(input('Enter a # between 1-10:'))

# print(f'Your number is {num}')


################### FOR LOOPS ##################################

#for loops = execute a block of code a fixed number of times. 
#            You can iterate over a range, string, sequence, etc. 

#iterate = going through a list 

# creditCard = "1234-5678-9012-1231"

# for x in creditCard:
#     print(x)

# for x in range(1,123,):
#     if x == 13 or 15 or 19:
#       break # break stops the count # CONTINUE skips over a number 
#     else:
#         print(x)


#CHALLENGE #1

favMovies = ['Incantation', 'Long Legs','Grave of the fireflies' ]

for x in favMovies:
  if x == 'Incantation':
     print('Incantaion is found ')
else:
    print('Incantation is not found')
    print(x)


#CHALLENGE #2 
    
movieDir = ['Kevin Ko', 'Oz Perkins','Isao' ]
  
for x in movieDir:
  if x == 'Kevin Ko':
    continue 
  print(x)



#CHALLENGE #3 
movieMon = [' Mother budda', "Devil",' Life ']
  
for x in movieMon: 
  if x == 'Life ':
    x.replace('Life', " Mother budda")
  print(x)
       