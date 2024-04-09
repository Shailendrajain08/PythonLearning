# The conversion of one datatype into another datatype is known as typeCasting.

# Explicit typeCasting 
# The conversion of one datatype into another datatype, done via developer or programmer's intervention or manually as per the requirement is known as explicit conversion
# example :- 
a = "1"
b = "2"

print(a + b)          # without typeCasting it will concatinate 2 strings . It will pront 12.

print(int(a) + int(b)) # it will print 3 because int() will convert satring a and b to number and then + operator will add both the values. 


# Implicit typeCasting 
# Datatype in python do not have the same level i.e. ordering of data type is not same in Python. Some of the data types have higher-order, and some have lower order. While performing any operations on variables with different data type in python, one of the variable's data types will changed to the higher data type.
# example :-

c = 8;                    # this is integer 
d = 1.2;                  # this is float
e = c + d                 # here python interpreter will convert this to float.
print(e)                             
print(type(e))