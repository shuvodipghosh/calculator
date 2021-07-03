

while True:



 print("what you want to do")
 print('1.add')
 print('2.subtract')
 print('3.multiply')
 print('4.devied')


 point=int(input('inpute number '))
 num1=int(input('type first number'))
 num2=int(input('type second number'))


 def add():
     a=(num1+num2)
     return a
 def subtract():
     b=(num1-num2)
     return b
 def multiply():
     c=(num1*num2)
     return c
 def devide():
     d=(num1/num2)
     return d


 if (point==1):
     print(num1,' +',num2,' = ',add())
 elif (point==2):
     print(num1," - ",num2," = ",subtract())
 elif (point==3):
     print(num1,' X ',num2,' = ',multiply())
 elif(point==4):
     print(num1,' % ',num2,' = ',devide())
 else:
     print('invelid number')
