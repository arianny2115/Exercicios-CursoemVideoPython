some = input('Enter something: ')
number = some.isnumeric()
letter = some.isalpha()
alnum = some.isalnum()
space = some.isspace()
lower = some.islower()
upper = some.isupper()
title = some.istitle()
printable = some.isprintable()

print(' The primitive type of this value is {}'.format(type(some)))
print(' Is "{}" made up only letters? {}'.format(some, letter))
print(' Is "{}" made up only numbers? {}'.format(some,number))
print(' Is "{}" made up only letters and numbers? {}' .format(some, alnum))
print(' Does "{}" contain only spaces {}'.format(some, space))
print(' Does "{}" contain only lowercase letters? {}'.format(some, lower))
print(' Does "{}" contain only lowercase letters? {} '. format(some, upper))
print(' is "{}" capitalized? {}'.format(some, title))
print(' Are the characters in"{}" printable? {}'.format(some, printable))