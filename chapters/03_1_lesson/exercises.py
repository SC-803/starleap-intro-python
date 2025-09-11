
##### Template for Chapter 3.14, Exercises 1 - 3 ######


def right_justify(input):
    length =len(input)
    print("length =", length)
    target = 70
    spaces = target - length
    space_string = ' '*spaces
    print(space_string + input)
#right_justify('monty')

#right_justify('Frogs are hopping all around me EHHE')
#right_justify('Im batman')





print("********** Ch 3 Exercise 2 **********")

def do_four(f):
    f()
    f()
    f()
    f()
def print_spam():
    print('spam')

#do_four(print_spam)



print("********** Ch 3 Exercise 3 **********")

def do_twice(f):
    f()
    f()

def do_four(f):
    do_twice(f)
    do_twice(f)

def print_beam():
    print('+ - - - -', end=' ')

def print_post():
    print('|        ', end=' ')

def print_beams():
    do_twice(print_beam)
    print('+')

def print_posts():
    do_twice(print_post)
    print('|')

def print_row():
    print_beams()
    do_four(print_posts)

def print_grid():
    do_twice(print_row)
    print_beams()

print_grid()

