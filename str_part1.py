#------------------------#
#  String Method part (1)
#------------------------#

# len() Return The length of the text string
ex = "i love python"
print(len(ex))

# strip() = Ignore spaces or any characters you specify inside parentheses
# before and after input
# ===============================================
# rstrip() = Ignore spaces or any characters you specify inside parentheses
# to the right input
# ==============================================
# lstrip() = Ignore spaces or any characters you specify inside parentheses
# to the left input
ex = "   i love python     "
print(ex.strip())
print(ex.rstrip())
print(ex.lstrip())

ex2 = "####i love python#####"
print(ex2.strip("#"))
print(ex2.rstrip("#"))
print(ex2.lstrip("#"))

ex3 = "#@+#@+#@+#i love python#####"
print(ex3.strip("#@+"))
print(ex3.rstrip("#@+"))
print(ex3.lstrip("#@+"))

# ==================================================
# title()
# The first letter of every capital word
# and the first letter after each capital number
# ==================================================
ex4 = "i love 2d graphics and 3g technology and python"
print(ex4.title())
# ==================================================
# capitalize()
# Only the first letter of every capital word
# ==================================================

ex5 = "i love 2d graphics and 3g technology and python"
print(ex5.capitalize())

c, d, e = "1", "11", "111"

print(c.zfill(3))  # "1" => "001"
print(d.zfill(3))  # "11" => "011"
print(e.zfill(3))  # "111" => "111"

# upper
ex6 = "python"
print(ex6.upper())  # PYTHON

# lower
ex7 = "PYTHON"
print(ex7.lower())  # python

# Slicing =
# var[start:end] end not included in returned result
# var[start:ene:steps] default steps = 1

ex8 = "i love python"
print(ex8[5:9])  # e py
print(ex8[2:9:2])  # lv y
