#------------------------#
#  String Method part (2)
#------------------------#

# split() => return List type
# split("any separator")
# split("any separator", option => maxsplit = number)
# rsplit() == split() But only from the right direction

a = "i love dart and flutter and php"
print(a.split())  # ['i', 'love', 'dart', 'and', 'flutter', 'and', 'php']
print(a.split("a"))  # ['i love d', 'rt ', 'nd flutter ', 'nd php']
print(a.split(" ", 3))  # ['i', 'love', 'dart', 'and flutter and php']
# ===============================
b = "i love dart and flutter and php and larvel "
# ['i', 'love', 'dart', 'and', 'flutter', 'and', 'php', 'and', 'larvel']
print(b.rsplit())
# ['i ', 'ove dart and f', 'utter and php and ', 'arve', ' ']
print(b.rsplit("l"))
# ['i love dart and flutter and php and ', 'arve', ' ']
print(b.rsplit("l", 2))
# =====================================

# center() => return string
# that method take two arguments the first required and second optional
# first argument = The number you want to add to the number of characters in the text string
# second argument = The character that you will add before and after to the text string
# second argument => default value = space

c = "shamss"
print(c.center(10))
print(c.center(10, "#"))

# count() => return int
# that method take three arguments the first required and second, third optional
# first argument  = the word, you know how many times the sentence was repeated
# second argument = start index
# third argument  = end index


d = "i love python and php because python and php is easy learning"
print(d.count("php"))
print(d.count("php", 15))
print(d.count("php", 15, 30))
w = d.count("is", 15, 25)
if w == 1:
    print("is found")
else:
    print('not found')

# swapcase() => return string
# the method is doing The case of the text string characters
# is switched from case to inverted

e = "i LoVe PyTHon"
f = "I LOVE PHP"

print(e.swapcase())
print(f.swapcase())

# startswith() -> return bool

g = "i love python and php because python and php is easy learning"

print(g.startswith("i"))  # True
print(g.startswith("p", 15))  # False
print(g.startswith('b', 15, 30))  # False

# endswith() -> return bool

g = "i love python and php because python and php is easy learning"

print(g.endswith("g"))  # True
print(g.endswith("p", 20))  # False
print(g.endswith('p', 15, 31))  # True
