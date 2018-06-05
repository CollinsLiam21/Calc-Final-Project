#Liam Collins
#chap10Tech.py
#input power series and center, output first four terms of taylor series, and integral of taylor series

def powerSeries(a,x,center):
    
    print('f(x) = '+str(a)+'/(1-'+x+') centered at x =',center)
    
    print(str(a)+'/(1-'+x+') = '+str(a)+'('+x+'-'+str(a)+')'+'^0 + '+str(a)+'('+x+'-'+str(a)+')'+'^1 + ')

powerSeries(3,'x',2)
