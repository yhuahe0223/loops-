#Exercise 1: 

answer = print(input('Whats your favorite programming language:'))

if answer == 'python' or 'Python':  
    print('You love Python')
else:
    print('Different Choice')


#Exercise 2: 
    
score = int(input( 'What is your score:'))

if score >= 90:
    print('A')
elif score >= 80 and score < 90:
    print('B')
elif score >= 70 and score < 80:
    print('C')
elif score >= 60 and score < 70:
    print('D')
elif score < 60:
    print('F')
else:
    print('Try again')

# Exercise 3:
    
username = input('What is your username?:')

if username == 'admin':
    print('Welcome admin!')
else:
    print('Wrong username, try again')

# Exercise 4:
    
a = [1,2,3,4]
b = a    

if id(a) == id(b):
    print('Same')
else:
    print('Differnt')
