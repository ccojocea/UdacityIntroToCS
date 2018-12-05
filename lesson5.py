#s == s[::-1]
#s.find(s[::-1])

x = 3.54
x = x + 0.5
s = str(x)
s = s[:s.find('.')]
print(s)

# Define a procedure, find_second, that takes
# two strings as its inputs: a search string
# and a target string. It should return a
# number that is the position of the second
# occurrence of the target string in the
# search string.

def find_second(s1, s2):
    return s1.find(s2, s1.find(s2)+1)

danton = "De l'audace, encore de l'audace, toujours de l'audace"
print (find_second(danton, 'audace'))
#>>> 25

twister = "she sells seashells by the seashore"
print (find_second(twister,'she'))
#>>> 13

print('hello' > '1')

# Define a procedure, bigger, that takes in
# two numbers as inputs, and returns the
# greater of the two inputs.


def bigger(x,y):
    return x if x > y else y

print(bigger(2,7))
#>>> 7

print(bigger(3,2))
#>>> 3

print(bigger(3,3))
#>>> 3