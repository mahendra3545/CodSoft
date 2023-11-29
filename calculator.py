'''Date:13 november 2023
   Author:Mahendra Pratap singh
   Programme: Calculator'''
def add(a, b) :
    return a+b
def subtract(a,b) :
    return a-b
def multiply(a,b) :
    return a*b
def divide(a,b) :
    return a/b
    #choosing operator
print("Select operator:\n" \
"1. Add\n"\
"2. Subtract\n"\
"3. Multiply\n"\
" 4. Divide\n")
#take operator input from user
select=int(input("select operator from 1,2,3,4:"))
#taking input from user
c=int(input("Enter first number:"))
d=int(input("Enter second number:"))
#printing responsedef add(a, b) :
if select==1:
     print(c, "+", d, "=", add(c, d))
elif select==2:
     print(c, "-", d, "=", subtract(c, d))
elif select==3:
     print(c, "*", d, "=", multiply(c, d))
elif select==4:
     print(c, "/", d, "=", divide (c, d))
else:
    print("Invalid! Input")