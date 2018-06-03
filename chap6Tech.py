#Liam Collins
#inputting polynomial function and outputting LRAM, RRAM, and Trapezoidal approximations compared with actual integral

#polynomial function defined
def function(a,b,c,d,e,x1,x2,n):
    print('f(x) = ',a,'x^',b,' + ',c,'x^',d,' + ',e)
    print('Interval = [',x1,',',x2,']')
    print('number of boxes = ',n)
    
    #LRAM Approximation
    totalLRAM = 0
    for i in range(0,n):
        area = (a*((i*(x2-x1)/n)+x1)**b + c*((i*(x2-x1)/n)+x1)**d + e)*(x2-x1)/n
        totalLRAM += area
    print('LRAM =',totalLRAM)
    
    #RRAM Approximation
    totalRRAM = 0
    for i in range(1,n+1):
        area = (a*((i*(x2-x1)/n)+x1)**b + c*((i*(x2-x1)/n)+x1)**d + e)*(x2-x1)/n
        totalRRAM += area
    print('RRAM =',totalRRAM)
    
    #Trap = LRAM+RRAM/2
    trap = (totalLRAM+totalRRAM)/2
    print('Trap =',trap)
    
    #Actual using fundamental theorem of calculus
    print('Actual =',(a/(b+1))*(x2)**(b+1)+(c/(d+1))*(x2)**(d+1)+e*(x2)-((a/(b+1))*(x1)**(b+1)+(c/(d+1))*(x1)**(d+1)+e*(x1)))
    
#User input values
#function(a,b,c,d,e,x1,x2,n)
function(22,9,3,3,4,0,2,10)
    
    
    




