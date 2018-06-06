#Liam Collins
#chap8Tech.py
#inputs polynomial function and interval, outputs arc length approximated using simpson's rule

from math import sqrt

#defined function
def arcLength(a,b,c,d,e,x1,x2):
    #prints function and interval
    print('f(x) = ',a,'x^',b,' + ',c,'x^',d,' + ',e)
    print('Interval = [',x1,',',x2,']')
    
    #Finding derivative
    print("f'(x) = ",a*b,'x^',b-1,' + ',c*d,'x^',d-1)
    
    #number of boxes, after 1000 boxes the program runs very slowly
    n = 100
    
    #a loop multiplying every other y value by 4 and the other y values by 2 (Simpson's Rule)
    num = 1
    total = 0
    for i in range(1,n):
        if num%2 == 0:
            total += 4*sqrt(1+(a*b*(((x2-x1)/n)*i+x1)**(b-1)+c*d*(((x2-x1)/n)*i+x1)**(d-1))**2)
            num += 1
        else:
            total += 2*sqrt(1+(a*b*(((x2-x1)/n)*i+x1)**(b-1)+c*d*(((x2-x1)/n)*i+x1)**(d-1))**2)
            num += 1
    
    #first value yo and last value yn
    firstYValue = sqrt(1+(a*b*(x1)**(b-1)+c*d*(x1)**(d-1))**2)
    lastYValue = sqrt(1+(a*b*(x2)**(b-1)+c*d*(x2)**(d-1))**2)
    
    #prints arc length
    print('Arc Length:',(total+firstYValue+lastYValue)*(x2-x1)/n*(1/3))

#user input values for the function
#function(a,b,c,d,e,x1,x2)
arcLength(1/3,3,1/4,-1,0,1,3)