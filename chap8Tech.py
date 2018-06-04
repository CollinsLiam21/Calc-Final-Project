#Liam Collins
#chap8Tech.py
#inputs polynomial function and interval, and outputs arc length using simpson's rule

from math import sqrt

def arcLength(a,b,c,d,e,x1,x2):
    print('f(x) = ',a,'x^',b,' + ',c,'x^',d,' + ',e)
    print('Interval = [',x1,',',x2,']')
    
    #Finding derivative
    print("f'(x) = ",a*b,'x^',b-1,' + ',c*d,'x^',d-1)
    
    n = 1000
    
    num = 1
    total = 0
    for i in range(1,n):
        if num%2 == 0:
            total += 4*sqrt(1+(a*b*(((x2-x1)/n)*i+x1)**(b-1)+c*d*(((x2-x1)/n)*i+x1)**(d-1))**2)
            num += 1
        else:
            total += 2*sqrt(1+(a*b*(((x2-x1)/n)*i+x1)**(b-1)+c*d*(((x2-x1)/n)*i+x1)**(d-1))**2)
            num += 1
    
    firstYValue = sqrt(1+(a*b*(x1)**(b-1)+c*d*(x1)**(d-1))**2)
    secondYValue = sqrt(1+(a*b*(x2)**(b-1)+c*d*(x2)**(d-1))**2)
    
    print((total+firstYValue+secondYValue)*(x2-x1)/n*(1/3))

arcLength(1/3,3,1/4,-1,0,1,3)
