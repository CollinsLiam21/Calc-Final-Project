#Liam Collins
#inputting polynomial function and outputting LRAM, RRAM and Trapezoid approximations

print('f(x) = ax^b + cx^d + e   [x1,x2]')
a = float(input('Enter value for a: '))
b = float(input('Enter value for b: '))
c = float(input('Enter value for c: '))
d = float(input('Enter value for d: '))
e = float(input('Enter value for e: '))
x1 = float(input('Enter x1 in [x1,x2]: '))
x2 = float(input('Enter x2 in [x1,x2]: '))
n = int(input('Enter the number of boxes: '))
print('f(x) = ',a,'x^',b,' + ',c,'x^',d,' + ',e)
print('Interval = [',x1,',',x2,']')
print('number of boxes = ',n)

#LRAM
totalLRAM = 0
for i in range(0,n):
    area = (a*(i*(x2-x1)/n)**b + c*(i*(x2-x1)/n)**d + e)*(x2-x1)/n
    totalLRAM += area
print('LRAM =',totalLRAM)

#RRAM
totalRRAM = 0
for i in range(1,n+1):
    area = (a*(i*(x2-x1)/n)**b + c*(i*(x2-x1)/n)**d + e)*(x2-x1)/n
    totalRRAM += area
print('RRAM =',totalRRAM)

#Trap = LRAM+RRAM/2
trap = (totalLRAM+totalRRAM)/2
print('Trap =',trap)


    
    
    




