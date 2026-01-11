# B 0 0 L E A N S and comparison operators

x = True
print(x) #true
print(type(x)) #bool

def can_vote (age):
    """
    check if a person is eligible to vote
    """
    return age>=18

print(can_vote(8)) #false
print(can_vote(89)) #true
print(can_vote(18)) #true

print(3==3) #true
print(3!=3) #true
print(3>3) #false
print(3<3) #false
print(3>=3) #true
print(3<=3) #true


# AND OR NOT

def can_be_a_us_president( is_natural_born_citizen ,age):

    return  is_natural_born_citizen and age>35

print(f" ANSWER : {can_be_a_us_president(True,38)}")



#boolean conversion
#Python treats empty values as False and non-empty values as True in conditions.
print(bool(0))
print(bool(1))
print(bool('name'))
print(bool(""))

#if elif else
n=7
if n == 0 :
    print("number is zero")
elif n>0:
    print("number is positive")
elif n<0:
    print("number is negative")
else:
    print("invalid input")




