def checkRightAngle(a=1,b=1,c=1):
    # function for checking a^2+b^2==c^2
    (a,b,c)=sorted((a,b,c))
    while a+b<=c:
        print('Enter valid triangle')
        (a,b,c)=map(int, input('Enter side of triangle a b c:').split())
    if a*a+b*b==c*c:
        print('Triangle is Right Angle')
        return 1
    print('Triangle is not right angle')
    return 0
if __name__=="__main__":
    #taking input
    (a,b,c)=map(int, input('Enter side of triangle a b c:').split())
    checkRightAngle(a,b,c)