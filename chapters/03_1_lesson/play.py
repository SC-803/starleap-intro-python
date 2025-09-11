
def print_lyrics():
    print('wow')
    print('WOWOW')

def repeat_lyrics():
    print_lyrics()
    print_lyrics()
    print_lyrics()

# repeat_lyrics()

def print_twice(input):
   print(input) 
   print(input)
   
print_twice('spam')

print_twice('spin'*10)

# print_twice('spaminacan')

def is_it_even(input):
    if input % 2 == 0:
     print(str(input) + 'is even')
    else:
       print(str(input) + 'is odd')
#is_it_even(4)
#is_it_even(5)

x =1000000
y = 2

def compare(x, y):
    if x < y:
        print('x is less than y')
    elif x > y:
        print('x is greater than y')
    else:
     print('x must equal y')

compare(1000000, 2)