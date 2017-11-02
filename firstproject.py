monty = True
python = 1.234
monty_python = 1.234 ** 2
print (monty_python)

name = raw_input("What is your name ")
quest = raw_input("What is your quest ")
color = raw_input("What is your color ")
print ("Ah, so your name is %s, yor quest is %s, and your favourite color is %s. " %(name, quest, color))




meal = 44.50
tax = 0.0675
tip = 0.15
meal = 44.50 + 44.50 * 0.0675
total = meal + meal * tip
print (total)
brian = "Hello Life!"
caesar = "Graham"
praline = "John"
viking = "Teresa"
print (caesar)
print (praline)
print (viking)
"""
+---+---+---+---+---+---+
! P ! Y ! T ! H ! O ! N !
+---+---+---+---+---+---+
"""
parrot = "Norwegian blue"
print (len(parrot))
print (parrot.lower())
print (parrot.upper())
print (len(parrot))
pi = 3.14
print (str(pi))
ministry = "The ministry of silly walks"
print (len(ministry))
print (ministry.upper())
the_machine_goes = "ping"
print (the_machine_goes)
print ("life" + "of" + "brian")
print ("I have " + str(2) + " coconuts!")
print ("The value of pi is around " + str(3.14))
g = "Golf"
h = "Hotel"
print ("%s, %s" %(g, h))
my_string = "move right"
print (len(my_string))
print my_string.upper()
print my_string.lower()
#Date Time
from datetime import datetime
print datetime.now()
past = datetime.now()
print past
now = datetime.now()
print now
from datetime import datetime
print datetime.now()
current_year = now.year
current_month = now.month
current_day = now.day
print now
print now.year
print now.month
print now.day
print '%s/%s/%s' %(now.day, now.month, now.year)
print now.hour
print now.minute
print now.second
print '%s-%s-%s' %(now.hour, now.minute, now.second)
date = '%s/%s/%s' %(now.day, now.month, now.year)
Time = '%s-%s-%s' %(now.hour, now.minute, now.second)
print date + " " + Time

import time
import datetime
print("Current date and time: " , datetime.datetime.now())
print("Current year: ", datetime.date.today().strftime("%Y"))
print("Month of year: ", datetime.date.today().strftime("%B"))
print("Week number of the year: ", datetime.date.today().strftime("%W"))
print("Weekday of the week: ", datetime.date.today().strftime("%w"))
print("Day of year: ", datetime.date.today().strftime("%j"))
print("Day of the month : ", datetime.date.today().strftime("%d"))
print("Day of week: ", datetime.date.today().strftime("%A"))

#Calendar
import Calendar
bc = calendar.TextCalendar(firstweekday=0)
print bc.formatyear(2017, 2, 1, 1, 6)


def clinic():
    print "you have just entered the clinic!"
    print "Do you take the room on the left or the right?"
    answer = raw_input("Type left or right and hit 'Enter'.").lower()
    if answer == "left" or answer == "l":
        print "This is the verbal abuse room, you heap of parrot dropings!"
    elif answer == "right" or answer == "r":
        print "Of course this is the argument room, I have told you already!"
    else:
        print "you didn't pickup left or right! Try again."
        clinic()
clinic()

""" equal to ==
    not equal to !=
    less than <
    greater than >
    less than or equal to <=
    greater than or equal to >=
"""

bool_one = True or False
print bool_one

raw_input("Press enter to exit")




"""
True and False is False
False and True is False
False and False is False
True and True is True
"""

"""
True or False is True
False or True is True
False or False is False
True or True is True
"""

"""
not True is False
not False is True
"""
bool_one = not (True)
bol_one = True and False
print bol_one
bool_two = False or not True and False
print bool_two
bool_three = not not True or False and not True
print bool_three
bool_four = True and not (False or False)


answer = "kela"
if answer == "kela":
  print ("you can eat")
def statement():
  if not(False):
    return"executed"
print (statement())

answer = "let's goto movie"
def weekend():
  if answer == "let's go to movie":
    return True
  else:
    return False
  weekend()
print (weekend())


def trueorfalse(answer):
  if answer > 5:
    return 1
  elif answer < 5:
    return -1
  else:
    return 0
print (trueorfalse(4))
print (trueorfalse(5))
print (trueorfalse(6))



def flying_circus():
  if 6>6 and 8!=9:
    return False
  elif 5 == 5:
    return True
  else:
    return 0
print (flying_circus())

 #PygLatin
"""
Pig Latin is a language game, where you move the first letter of the word to the end and add "ay."
so "Python" becomes "ythonpay."
"""
#"watermelon"
#"atermelonway"
my_input = input("please enter your word here:")
user_input = "watermelon"
print (user_input)
last_letter = user_input[0]
print (last_letter)
print (user_input[1:]  + last_letter + "ay")

original = input("Enter a word:")
word = original.lower()
print (word)
first = word[0]
print (first)
new_word = word + first + "ay"
print (new_word)
print (new_word[1:])

if len("original") > 0 and original.isalpha():
  print (original)
else:
  print ("empty")

 def square(n):
     """ returns the swuare of a number """
     squared = n ** 2
     print "%d squared is %d", %(n, squared)
     return squared
print square(10)

def power(base, exponent):
	result = base ** exponent
	print "%d to the powewr of %d gives %d" %(base, exponent, result)
	return result

print power(10, 3)

def cube(number):
	return number ** 3

def by_three(number):
    if number % 3 == 0:
		return cube(number)
	else:
		return false
print cube(3)

import math
print math.sqrt(44)

from math import sqrt
print sqrt(33)

from math import *
print tan(45)

print max(20,39,589,450)
print min(23,48,33,5,32,5,34554,33)
print abs(-342243)
print type(3.43)
print type(44)
print type("go fetch it!")

#Functions
def shut_down(s):
	if s == "yes":
		return "shutting down"
	elif s == "no":
		return "shutdown aborted"
	else:
		return "sorry"
print shut_down("yes")

def distane_from_zero(answer):
	if type(answer) == int or type(answer) == float:
		return abs(answer)
	else:
		return "Nope"

def wages(hours):
	return 8.35 * hours
print wages(20)

def hotel_cost(nights):
	return 140 * nights
 print hotel_cost(2)

def plane_ride_cost(city):
	if city == 'charlotte':
		return 183
	elif city == 'tampa':
		return 220
	elif city == 'pittsburgh':
		return 222
	elif city == 'los angeles':
		return 475
print plane_ride_cost('tampa')

def rental_car_cost(days):
	day_rate = 40
	total_cost = day_rate * days
	if days >= 7:
		totl_cost = total_cost - 50
	elif days >= 3:
		total_cost = total_cost - 20
 print rental_car_cost(3)


 def trip_cost(city, night, days):
	return rental_car_cost(days) + hotel_cost(night) + plane_ride_cost(city)

print trip_cost('los angeles', 2, 7)

#Lists

zoo_animals = ['pengun', 'elephant', 'tiger', 'panda']
if len(zoo_animals) > 3:
	print "The first animal of the zoo is "  + zoo_animals[0]
	print "The second animal of the zoo is "  + zoo_animals[1]
	print "The third animal of the zoo is "  + zoo_animals[2]
	print "The fourth animal of the zoo is "  + zoo_animals[3]


numbers = [5, 6, 7, 8]
print "Adding the numbers at indices 0 and 2..."
print numbers[0] + numbers[2]

#Replace item in the list
zoo_animals[1] = 'tiger'
zoo_animals[3] = 'giraffe'
print zoo_animals

#Add items to the list
letters = ['a', 'b', 'c']
letters.append('d')
print letters


suitcase = []
suitcase.append("sunglasses")
suitcase.append("deoderant")
suitcase.append("undergarment")
suitcase.append("bodylotion")
print suitcase

list_length = len(suitcase)
print list_length
print "There are %s items in the suitcase." %(list_length)

suitcase = ['sunglasses', 'deoderant', 'undergarment', 'bodylotion']
first = suitcase[0:2]
middle = suitcase[2:3]
last = suitcase[-1]
print last

animals = "catdogfrog"
animals[0:3]
'cat'
animals[6:]
'frog'
cat = animals[:3]
frog = animals[6:]
print frog

animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
animals.index('duck')
#output = 2
animals.index("emu")
#output = 3
duck_index = animals.index('duck')
print duck_index

animals.insert(duck_index, 'cobra')
print animals
#output = ['aardvark', 'badger', 'cobra', 'duck', 'emu', 'fennec fox']

animals.insert(3,'panda')
print animals
#output = ['aardvark', 'badger', 'cobra', 'panda', 'duck', 'emu', 'fennec fox']


my_list = [1,9,3,8,5,7]
for number in my_list:
    print number
for number in my_list:
    print 2 * number
""" output
2
18
6
16
10
14
"""
animals = ["cat", "ant", "bat"]
animals.sort()
for animal in animals:
    print animal

"""	output
ant
bat
cat
"""
#loop
start_list = [5, 3, 1, 2, 4]
square_list =[]
for number in start_list:
	squared_number = number ** 2
	square_list.append(squared_number)
    square_list.sort()
print square_list()

#Dictionary {KEY : value}

residents = {'puffin': 104, 'sloth': 105, 'Burmese python': 106}

print residents['puffin']
print residents['sloth']
print residents[0]

residents['car'] = 108 #Add new items to the dictionary list
print residents
#output ={'sloth': 105, 'puffin': 104, 'Burmese python': 106, 'car': 108}

menu = {}
menu['grilled chicken'] = 10.5
menu['chicken handi'] = 8.99
menu['zinger burger'] = 4.99
menu['dessert'] = 3.99
print "There are " + str(4) + " items on the menu. "
#output = There are  4 items on the menu.
print menu
#output = {'grilled chicken': 10.5, 'zinger burger': 4.99, 'chicken handi': 8.99, 'dessert': 3.99}
print len(menu)
4

del residents['car']  #delets item from dictionary list
print residents
#output {'sloth': 105, 'puffin': 104, 'Burmese python': 106}

residents['puffin'] = 108 #Change the value of Key
print residents
#output {'sloth': 105, 'puffin': 108, 'Burmese python': 106}

inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'breadloaf']
}
print(inventory['gold'])
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']
inventory['pocket'] = ['seashell' 'strange berry', 'lint']
inventory['backpack'].sort()
inventory['backpack'].remove('dagger')
incentory['gold'] = inventory['gold'] + 50

webster = {
        "Aardvark" : "A star of a popular children's cartoon show.",
        "Baa" : "The sound of agoat makes.",
        "Carpet" : "Goes on the floor",
        "Dab" : "A small amount"
}   #looping

for item in webster:
    print(webster[item])


a = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
for number in a:
	if number % 2 == 0:
		print number


def fizz_count(x):
	count = 0
	for item in x:
		if item == 'fizz':
			count = count + 1
	return count

fizz_count(['fizz', 'cat', 'fizz'])
2

def count_small(numbers):
	total = 0
	for n in numbers:
		if n < 10:
			total = total +1
	return total

lost = [4,8,15,16,28,45]
small = count_small(lost)
print small
2

#string looping

word = "programming is fun!"
for letter in word:
	if letter == "i":
		print letter

counter = 0
for letter in word:
	if letter == "i":
		counter = counter + 1
		print letter
# output i, i

prices = {"banana" : 4,}
prices = {"banana" : 4,}
prices = {"banana" : 4,}
prices = {"banana" : 4, "apple" : 2, "orange" : 1.5, "pear" : 3}
stock = {"banana" : 6, "apple" : 0, "orange" : 32, "pear" : 15}
for key in prices:
	print key
	print "price : %s" %prices[key]
	print "stock: %s" %stock[key]

total = 0
for key in prices:
    value = prices[key] * stock[key]
    print (value)
    total = total + value
    print (total)
shopping_list =['banana', 'orange', 'apple']

def compute_bill(food):
    total = 0
    for item in food:
        if stock[item] > 0:
            total += price[item]
            stock[item] = stock[item] - 1
    return total

#Class

Llyod = {"name" : 'llyod', "homework" : [90.0,97.0,75.0,92.0], "quizzes": [88.0,40.0,94.0], "tests": [75.0,90.0]}
alice = {"name" : 'Alice', "homework" : [100.0,92.0,98.0,100.0], "quizzes": [82.0,83.0,91.0], "tests": [89.0,97.0]}
tyler = {"name" : 'Tyler', "homework" : [0.0,87.0,75.0,22.0], "quizzes": [0.0,75.0,78.0], "tests": [100.0,100.0]}
students = [Llyod, alice ,tyler]

def average(numbers):
	total = sum(numbers)
	total = float(total)
	return total / len(numbers)

def get_average(student):
        homework = average(student["homework"])
        quizzes = average(student["quizzes"])
        tests = average(student["tests"])
        weighted_homework = .10 * homework
        weighted_quizzes = .30 * quizzes
        weighted_tests = .60 * tests
        return weighted_homework + weighted_quizzes + weighted_tests

def get_letter_grade(score):
        if score >= 90:
                return "A"
        elif score>= 80:
                return "B"
        elif score >= 70:
                return "C"
        elif score >= 60:
                return"D"
        else:
                return "F"

print get_letter_grade(get_average(Llyod))
print get_letter_grade(get_average(alice))

def get_class_average(students):
	results = []
	for student in students:
		student_average = get_average(student)
	results.append(student_average)
	return average(results)

print get_class_average(students)

#format method
for i in range(1, 101):
	print("Sr. no {}".format(i)) #It will print Sr. no 1 to 100

#Lists and Functions

n = [1, 3, 5]
print n[1]
# 3
n[1] = n[1] * 3
print n
# [1, 9, 5]
n.append(4)
print n
# [1, 9, 5, 4]
print n.pop()
# 4
print n
# [1, 9, 5]
print n.pop(1)
# 9
del(n[0])
print n
# [5]
number = 5
def my_function(x):
	return x + 3

print my_function(number)
# 8

m = 5
n =3
def fun(m, n):
	return m % n

print fun(m, n)
# 2

def add_function(num1, num2):
	return num1 + num2

print add_function(m, n)
# 8

def string_function(s):
	return s + 'world'
print string_function(s)
# Helloworld

def list_function(x):
	return x

n = [3, 5, 7]
print list_function(n)
# [3, 5, 7]

def list_function(x):
	x[1] = x[1] + 3
	return x

print  list_function(n)
# [3, 8, 7]

def list_extender(lst):
	lst.append(9)
	return lst

print list_extender(n)
# [3, 8, 7, 9]

n = [3, 5, 7]
for index in range(0, len(n)):
	print n[index]

def print_list(x):
	for i in range(len(x)):
		print x[i]
print print_list(n)

def double_list(n):
	for i in range(len(n)):
		n[i] = n[i] * 2
	return n

print double_list(n)
# [6, 10, 14]

def double_list(x):
	for i in range(0, len(x)):
		x[i] = x[i] * 2
	return x
print double_list(n)
# [12, 20, 28]

range(0, 101, 1)
range(0, 101, 2)
sum(range(0, 101, 3))
range(101, 2, -2)
range(10, 2, -1) #[10, 9, 8, 7, 6, 5, 4, 3]


n = [3, 5, 7]
def total(numbers):
	result = 0
	for i in range(0, len(numbers)):
		result += numbers[i]
	return result

print (total(n))
#15

n = ["Michael", "Liberman"]
def join_strings(words):
	result = ""
	for word in words:
		result = result + word
	return result

print(join_strings(n))
#MichaelLiberman

''.join(n)
'name '.join(n)
m = ["game", "players", "console"]
n = ["soccer", "cricket", "baseball"]
m + n
['game', 'players', 'console', 'soccer', 'cricket', 'baseball']

list_of_lists = [[1,2,3], [4,5,6]]
for lists in list_of_lists:
	print (lists)


#[1, 2, 3]
#[4, 5, 6]

for lists in list_of_lists:
	for item in lists:
		print(item)

""" output
1
2
3
4
5
6
"""
n = [[1,2,3], [4,5,6,7,8,9]]
def flatten(lists):
	result = []
	for numbers in lists:
		for number in numbers:
			result.append(number)
	return result

print(flatten(n))
#[1, 2, 3, 4, 5, 6, 7, 8, 9]


#Battleship

board = []
for _ in range(5):
	board.append(['o'] * 5)
print (board)

#output [['o', 'o', 'o', 'o', 'o'], ['o', 'o', 'o', 'o', 'o'], ['o', 'o', 'o', 'o', 'o'], ['o', 'o', 'o', 'o', 'o'], ['o', 'o', 'o', 'o', 'o']]
def print_board(board):
	for row in board:
		print(row)

print(print_board(board))
""" ['o', 'o', 'o', 'o', 'o']
    ['o', 'o', 'o', 'o', 'o']
    ['o', 'o', 'o', 'o', 'o']
    ['o', 'o', 'o', 'o', 'o']
    ['o', 'o', 'o', 'o', 'o'] """"

#" ".join(print_board(board))
def print_board(board):
	for row in board:
		print(' '.join(row))

 print(print_board(board))
""" output
o o o o o
o o o o o
o o o o o
o o o o o
o o o o o
"""
#LIST[row][col]--> the item you are looking for in a 2D list.

from random import randint
randint(0, 10)
#9
randint(0, 10)
#8
randint(0, 10)
#5

def random_row(board):
	return randint(0, len(board)- 1)

def random_col(board):
    return randint(0, len(board) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

guess_row = int(input("Guess Row: "))
guess_col = int(input("guess col: "))


for turn in range(4):

  guess_row = int(input("Guess Row: "))
  guess_col = int(input("guess col: "))

  if guess_row == ship_row or guess_col == ship_col:
	  print("Congaratulations! you sank my battleship!")
	  break

  else:
    print("You missed my battleship")

    if guess_row not in range(5) or guess_col not in range(5):
      print("Oops, that's not even in the Ocean")
    else:
      print("You missed my battleship")
      board[guess_row][guess_col] = 'X'
      if turn == 3:
        print("Game over!")
      elif board[guess_row][guess_col] == 'X':
      print('you guessed that already')
      print_board(board)


#OOPS class

class Fruit(object):
    """A class that makes various tasty fruits."""
    def __init__(self, name, color, flavor, poisonous):
        self.name = name
        self.color = color
        self.flavor = flavor
        self.poisonous = poisonous

    def description(self):
        print "I'm a %s %s and I taste %s." % (self.color, self.name, self.flavor)

    def is_edible(self):
        if not self.poisonous:
            print "Yep! I'm edible."
        else:
            print "Don't eat me! I am super poisonous."

lemon = Fruit("lemon", "yellow", "sour", False)
Mango = Fruit("Mango", "Green", "sweet", False)
print lemon.description()
print lemon.is_edible()


class Animal(object):
    def __init__(self, name):
        self.name = name
zebra = Animal("Jeffrey")
print zebra.name


# Class definition
class Animal(object):
    """Makes cute animals."""
    # For initializing our instance objects
    def __init__(self, name, age, is_hungry):
        self.name = name
        self.age = age
        self.is_hungry = is_hungry

# Note that self is only used in the __init__()
# function definition; we don't need to pass it
# to our instance objects.

zebra = Animal("Jeffrey", 2, True)
giraffe = Animal("Bruce", 1, False)
panda = Animal("Chad", 7, True)

print zebra.name, zebra.age, zebra.is_hungry
print giraffe.name, giraffe.age, giraffe.is_hungry
print panda.name, panda.age, panda.is_hungry


class Animal(object):
    """Makes cute animals."""
    is_alive = True
    def __init__(self, name, age):
        self.name = name
        self.age = age

zebra = Animal("Jeffrey", 2)
giraffe = Animal("Bruce", 1)
panda = Animal("Chad", 7)

print zebra.name, zebra.age, zebra.is_alive
print giraffe.name, giraffe.age, giraffe.is_alive
print panda.name, panda.age, panda.is_alive


class Animal(object):
    """Makes cute animals."""
    is_alive = True
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def description(self):
        print self.name
        print self.age
hippo = Animal("Arpit", 25)
print hippo.age


class Animal(object):
    """Makes cute animals."""
    is_alive = True
    health = "good"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def description(self):
        print self.name
        print self.age
hippo = Animal("Arpit", 25)
sloth = Animal("sonu", 35)
ocelot = Animal("atif", 34)
print hippo.age
print hippo.health
print sloth.health


class ShoppingCart(object):
    """Creates shopping cart objects
    for users of our fine website."""
    items_in_cart = {}
    def __init__(self, customer_name):
        self.customer_name = customer_name

    def add_item(self, product, price):
        """Add product to the cart."""
        if not product in self.items_in_cart:
            self.items_in_cart[product] = price
            print product + " added."
        else:
            print product + " is already in the cart."

    def remove_item(self, product):
        """Remove product from the cart."""
        if product in self.items_in_cart:
            del self.items_in_cart[product]
            print product + " removed."
        else:
            print product + " is not in the cart."

my_cart = ShoppingCart("Vivek")
my_cart.add_item("shoes", 10)


#Inheritance is the process by which one class takes on the attributes
#and methods of another, and it's used to express an is-a relationship.

class Customer(object):
    """Produces objects that represent customers."""
    def __init__(self, customer_id):
        self.customer_id = customer_id

    def display_cart(self):
        print "I'm a string that stands in for the contents of your shopping cart!"

class ReturningCustomer(Customer):
    """For customers of the repeat variety."""
    def display_order_history(self):
        print "I'm a string that stands in for your order history!"

monty_python = ReturningCustomer("ID: 12345")
monty_python.display_cart()
monty_python.display_order_history()

#superclass
class Employee(object):
    """Models real-life employees!"""
    def __init__(self, employee_name):
        self.employee_name = employee_name

    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 20.00

class PartTimeEmployee(Employee):
    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 12.00# Add your code below!
    def full_time_wage(self, hours):
            return super(PartTimeEmployee, self).calculate_wage( hours)

milton = PartTimeEmployee("Milton Hardy")
print milton.full_time_wage(10)


class Triangle():
    number_of_sides = 3
    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3

    def check_angles(self, angle1, angle2, angle3):
        if self.angle1 + self.angle2 + self.angle3 == 180:
            return True
        else:
            return False
my_triangle = Triangle(90, 30, 60)
print (my_triangle.number_of_sides)
print (my_triangle.check_angles(90, 30, 60))

class Equilateral(Triangle):
    angle = 60
    def __init__(self):
        self.angle1 = self.angle
        self.angle2 = self.angle
        self.angle3 = self.angle
my_equi_triangle = Equilateral()
print (my_equi_triangle.check_angles(60, 60, 60))



class Car(object):
    condition = "new"
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg = mpg

my_car = Car("DeLorean", "silver", 88)
print my_car.model
print my_car.color
print my_car.mpg


class Car(object):
    condition = "new"
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg   = mpg
    def display_car(self):
        return "This is a " + self.color + " " + self.model + " with" + " " + str(self.mpg) + " MPG."
my_car = Car("DeLorean", "silver", 88)
print my_car.condition
print my_car.model
print my_car.color
print my_car.mpg
print my_car.display_car()



class Car(object):
    condition = "new"
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg   = mpg
    def display_car(self):
        return "This is a " + self.color + " " + self.model + " with" + " " + str(self.mpg) + " MPG."
    def drive_car(self):
        self.condition = "used"
my_car = Car("DeLorean", "silver", 88)
print my_car.condition
print my_car.model
print my_car.color
print my_car.mpg
my_car.drive_car()
print my_car.condition

class ElectricCar(Car):  #inhertance of baseclass
    def __init__(self, battery_type, model, color, mpg):
        self.battery_type = battery_type
        self.model = model
        self.color = color
        self.mpg = mpg
my_car = ElectricCar("molten salt", "Xperia", "Navy blue", 75)
print my_car.condition
print my_car.drive_car()
print my_car.condition


class Point3D(object):
    def __init__(self,x ,y,z):
        self.x = x
        self.y = y
        self.z = z
    def __repr__(self):   #__repr__() method, which is short for representation; by providing a return value in this method,
        return "(%d, %d, %d)" %(self.x,self.y,self.z)
my_point = Point3D(1, 2, 3)
print my_point




#Iterators for Dictionaries
my_dict = {"Vivek" : 9993602730, "atul" : 8769472749, "viraj" : 9089827398}
print (my_dict.items())

my_dict = {"Vivek" : 9993602730, "atul" : 8769472749, "viraj" : 9089827398}
print my_dict.keys()
print my_dict.values()

#The 'in' Operator
#For iterating over lists, tuples, dictionaries, and strings,
#Python also includes a special keyword: in.
# You can use in very intuitively, like so:

my_dict = {"Vivek" : 9993602730, "atul" : 8769472749, "viraj" : 9089827398}
for key in my_dict:
    print key, my_dict[key]

evens_to_50 = [i for i in range(51) if i % 2 == 0]
print evens_to_50

#List Comprehension Syntax
doubles_by_3 = [x*2 for x in range(1,6) if (x*2) % 3 == 0]
# Complete the following line. Use the line above for help.
even_squares = [x**2 for x in range(2,12) if (x**2) % 2 == 0]
print even_squares


cubes_by_four = [x**3 for x in range(1, 11) if (x**3) % 4 == 0 ]
print cubes_by_four

l = [i ** 2 for i in range(1, 11)]
# Should be [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print l[2:9:2]

my_list = range(1, 11) # List of numbers 1 - 10

print my_list[::2]# Add your code below!


my_list = range(1, 11)
backwards = my_list[::-1]
print backwards# Add your code below!

to_one_hundred = range(101)
backwards_by_tens = to_one_hundred[100::-10]# Add your code below!
print backwards_by_tens

to_21 = list(range(1, 22))
odds = to_21[::2]
middle_third = to_21[7:14]

my_list = range(16)
print filter(lambda x: x % 3 == 0, my_list)

languages = ["HTML", "JavaScript", "Python", "Ruby"]
print filter(lambda x: x =='Python', languages)

squares = [x**2 for x in range(1, 11)]
print filter(lambda x: x>30 and x<70, squares

movies = {
	"Monty Python and the Holy Grail": "Great",
	"Monty Python's Life of Brian": "Good",
	"Monty Python's Meaning of Life": "Okay"
}
print movies.items()


threes_and_fives = [x for x in range(1, 16) if x % 3==0 or x % 5 == 0]

garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"
first = garbled[::2]
message = first[::-1]
print message


garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"
message = filter(lambda x:x!= 'X', garbled)
print message



#Class

class Car(object):
    condition = "new"
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg   = mpg
    def display_car(self):
        return "This is a " + self.color + " " + self.model + " with" + " " + str(self.mpg) + " MPG."
my_car = Car("DeLorean", "silver", 88)
print my_car.condition
print my_car.model
print my_car.color
print my_car.mpg
print my_car.display_car()



#file input output

my_list = [i**2 for i in range(1,11)]
# Generates a list of squares of the numbers 1 - 10

f = open("output.txt", "w")

for item in my_list:
    f.write(str(item) + "\n")
f.close() #always close the open document it will saved.

my_file = open("text.txt", "r")
print my_file.readline() #reads first line
print my_file.readline() #reads second line
print my_file.readline()# reads 3rd line
my_file.close()



with open("text.txt", "w") as textfile: #with as  keyword  don't need to close the file tectfile = any variable name you want to assign to your file
	textfile.write("Success!")

with open("text.txt", "r+") as my_file:
    my_file.write("suck my cock!")

#Bitwise operations are operations that directly manipulate bits
#In Python, you can write numbers in binary format by starting the number with 0b
print 0b1,    #1
print 0b10,   #2
print 0b11,   #3
print 0b100,  #4
print 0b101,  #5
print 0b110,  #6
print 0b111   #7
print "******"
print 0b1 + 0b11
print 0b11 * 0b11

print bin(1)
print bin(2)
print bin(3)
print bin(4)
print bin(5)


#int function actually has an optional second parameter.
#When given a string containing a number and the base that number is in,
#the function will return the value of that number converted to base ten.
print int("1",2)
print int("10",2)
print int("111",2)
print int("0b100",2)
print int(bin(5),2)
# Print out the decimal equivalent of the binary 11001001.
print int("11001001", 2)

#Slide to the Left! Slide to the Right!
shift_right = 0b1100
shift_left = 0b1
shift_right = shift_right >> 2
shift_left = shift_left << 2
print bin(shift_right)
print bin(shift_left)

# Left Bit Shift (<<)
0b000001 << 2 == 0b000100 (1 << 2 = 4)
0b000101 << 3 == 0b101000 (5 << 3 = 40)

# Right Bit Shift (>>)
0b0010100 >> 3 == 0b000010 (20 >> 3 = 2)
0b0000010 >> 2 == 0b000000

print bin(0b1110 & 0b101) #AND operator
print bin(0b1110 | 0b101) #OR operator
print bin(0b1110 ^ 0b101) #XOR operator

#The bitwise NOT operator (~) just flips all of the bits in a single number.
# it will add +1 with '-ve' sign.
print ~1
print ~2
print ~3
print ~42
print ~123

#A bit mask is just a variable that aids you with bitwise operations.
#A bit mask can help you turn specific bits on, turn others off,
#or just collect data from an integer about which bits are on or off.

mask = 0b1000

def check_bit4(input):
    desired = input & mask
    if desired > 0:
        return "on"
    else:
        return "off"
print check_bit4(0b1110)


a = 0b10111011
mask = 0b111
desired  = a | mask
print bin(desired)

a = 0b11101110
mask = 0b11111111
desired = a ^ mask
print bin(desired)

def flip_bit(number,n):
    mask = 0b1 << (n-1)
    result = number ^ mask
    return bin(result)
print flip_bit(32, 3)

#Exam statistics
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades):
    for grade in grades:
        print grade

def grades_sum(grades):
    total = 0
    for grade in grades:
        total += grade
    return total

def grades_average(grades):
    sum_of_grades = grades_sum(grades)
    average = sum_of_grades / float(len(grades))
    return average

def grades_variance(scores):
    average = grades_average(scores)
    variance = 0
    for score in scores:
        variance = variance + (average - score) ** 2
    variance = variance / len(scores)
    return variance
print grades_variance(grades)

def grades_std_deviation(variance):
    return variance ** 0.5
variance = grades_variance(grades)
print grades_std_deviation(variance)


#Employee class

class Employee:

    num_of_employees = 0
    raise_amount = 1.3
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        Employee.num_of_employees += 1
        
    @property
    def fullname(self):
        return "{} {}".format(self.first, self.last)

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

     def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())



class Developer(Employee):
    def __init__(self, first, last, pay, prog_lang):
    super().__init__(first, last, pay)
    self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self, first, last, pay, employees = None):
        super().__init__(first, last, pay)
        if employees is none:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def rem_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    def print_emp(self):
        for employee in self.employees:
            print ("-->", emp.fullname())


#emp_str_1 = 'John-Doe-70000'
# emp_str_2 = 'Steve-Smith-30000'
# emp_str_3 = 'Jane-Doe-90000'

first, last, pay = emp_str_1.split('-')

#new_emp_1 = Employee(first, last, pay)
# new_emp_1 = Employee.from_string(emp_str_1)

#print(new_emp_1.email)
# print(new_emp_1.pay)

mgr_1 = Manager('Amit', 'Gotmare', 90000, [dev_1])

dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = Developer('Test', 'Employee', 60000, 'Java')


emp1 = Employee("vivek", "vishwakarma", 500)
emp2 = Employee("shrijan", "sharma", 1300)
emp3 = Employee("Nitesh kumar", "singh", 1400)
emp1.raise_amount = 1.5
emp2.raise_amount = 1.1
emp3.raise_amount = 1.1
emp1.apply_raise()
print (emp1.__dict__)
print ("\n")
print (emp2.__dict__)
print ("\n")
print (emp3.__dict__)
print (Employee.num_of_employees)

mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_1)

mgr_1.print_emps()
# print(emp_1 + emp_2)

print(len(emp_1))




#decorators

import time
def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(func.__name__ +" took " + str((end-start)*1000) + "mil sec")
        return result
    return wrapper

@time_it
def calc_square(numbers):
    result = []
    for number in numbers:
        result.append(number*number)
    return result

@time_it
def calc_cube(numbers):
    result = []
    for number in numbers:
        result.append(number*number*number)
    return result

array = range(1,100000)
out_square = calc_square(array)
out_cube = calc_cube(array)
