def perfect(number):
    sum=0
    i=1
    while i<number:
        if number%i==0:
            sum=sum+i
        i=i+1
    if  sum==number:
        print("perfect")
    else:
        print("not")
perfect(6)

# 