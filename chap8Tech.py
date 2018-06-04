#Liam Collins
#chap8Tech.py
#inputting polynomial function and interval, and outputting arc length using simpson's rule

def arcLength(a,b,c,d,e,x1,x2):
    print('f(x) = ',a,'x^',b,' + ',c,'x^',d,' + ',e)
    print('Interval = [',x1,',',x2,']')
    
    #Finding derivative
    print("f'(x) = ",a*b,'x^',b-1,' + ',c*d,'x^',d-1)
    
    num = 1
    total = 0
    for i in range(x1,x2,.00002):
        if num%2 == 0:
            total += 4*(a*b*(i)**(b-1)+c*d*(i)**(d-1))
            num += 1
        else:
            total += 2*(a*b*(i)**(b-1)+c*d*(i)**(d-1))
            num += 1

arcLength(1,1,2,2,3,2,2)
