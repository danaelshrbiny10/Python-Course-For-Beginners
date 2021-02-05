## Q1 :
# What will the following code produce?
# a = 2
# a = 4
# a = 6
# print(a + a + a)

# solution :
a = 6                
print(a + a + a)  
# print(6 + 6 +6)   

output ===>  18    

# --------------------------------------------------------------------

## Q2 :
# What's wrong with the following script?
# a = 1
# _a = 2
# _a2 = 3
# 2a = 4

output ===> 2a = 4           # python not start with num  (invalid syntax)

# ----------------------------------------------------------------------

## Q3 :
# Fix the last line so that it outputs the sum of 1 and 2
a = "1"
b = 2
print(a + b)

# Expected output: 3

# solution :
a = 1
b = 2
print (a+b)       # print(1+2) ===> 3

# -------------------------------------------------------------------------

## Q4 :
# Executing the code will throw an error. Can you explain why?
a = 1
b = 2
print(a == b)
print(b == c)

# solution :
print(a == b)    # not excute because a != b
print(b == c)    # not excute because variable c not found

# ----------------------------------------------------------------------------

## Q5 :
10 / 3 = ??
10 // 3 = ??
10 % 3 = ??

# solution :
10 / 3 = 3.3333333333333335             # always result in float
10 //3 = 3                              # result with right num
10 % 3 = 1                              # rest of division

# ----------------------------------------------------------------------------

## Q6 :
#  what's the output ?
x = 20
x +=20
print(x)

# solution :
x = 20
x +=20          ====> x = x + 20        ===> x = 20 + 20
print(x)        ====> 40

# -------------------------------------------------------------------------------

## Q7 :
# fix the error 
name = 'welcome in python"

#solution :
name = 'welcome in python'   OR   name = "welcome in python"

# -------------------------------------------------------------------------------

## Q8 :   

# what's the different between high level language & low level language ?
High Level Language :    1) It is programmer language
                         2) less memory efficient
                         3) easy to understand
                         4) It is simple to debug and maintain comparatively

low  Level Language :    1) It is a machine language
                         2) high memory efficient
                         3) It is Hard to understand
                         4) It is complex to debug and maintain comparatively

# python interpeted or compiled language ?
python is an interpreted Language

# can you use ; in python ?   explain your answer if true or false
yes , can i use semicolon in One situation :
     when i know type of two variables in one line use ; between the start and the end 
         ----> like :  x = 5
                       y = "python"
                       print(type(x)) ; print(type(y))

# what's bool type ?
bool is type of python variables and always take variables "true or false"

# tell me the different between :
#       1)  == and =
=  To Arithimatic Operators    ,   ==  To Comparison operators

#       2)  '' , "" and ''' '''
'' and "" when write str   , ''' ''' when write comment to  multi lines

#       3)  int , str and float
int ===> for integer (Right Num)  , str ===> for string and write in '' or "" , float ===> for fraction num

#       4)   /  , //  and  %
/ ===> result in float  , // ===> right num , % ===> rest of division

# what's meant by using !=
Mean 'Not Equal' in Comparison Operators

# steps of Operator Precedenc
         1)  ()
         2)  **
         3)  * /
         4)  + -

# answer this : (20+2**3)*2-(6+3*4)
            (20+8)*2-(6+12)
            (28)*2-(18)
            28*2-18
            56-18
            38

# how to write comment in python
# ====> for one line     , ''' ''' ====> for multi lines

# -----------------------------------------------------------------------------------
## Q9 : true or false

1) n = 20 , n2 = "20"  ====> n + n2 =40     # false   ===> int !+ str
2) name = 'python' or "python"              # true
3) x = 'what's python'                      # false   ===> "what's python"
4) addres = "egypt,street ahmed"arabi"      # false   ===> "egypt,street ahmed'arabi"
5) 20/5 = 4                                 # false   ===> 4.0
6) ?age = 20                                # false   ===> invalid syntax
7) float ====> double in memory             # true
8) /t ==> new line   ,  /n ===> tab         # false   ===> /t ==> tab , /n ==> new line

# -----------------------------------------------------------------------------------