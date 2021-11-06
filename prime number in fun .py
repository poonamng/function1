# def primeorNot(num):     
#     if num > 100:
#         for i in range(2,num):
#             if (num % i) == 0:
#                 print(num,"not prime number")
#                 break
#             else:
#                 print(num,"is a prime number")
#     else:
#            print(num,"is not a prime number")
# # primeorNot(6)


# def prime(num):
#     if num>1:
#         for i in (2,num):
#             if num%i==0:
#                 print("prime not")
#             else:
#                 #    print("prime")
#     else:
#         print(" not prime")                
# prime(9)                   

def prime_number(num):
    i=1
    a=[]
    while i<1000:
        if num%i==0:
            print("prime number")
            a.append(i)
            print(a)
        else:
            print("not prime number")   
        i=i+1
prime_number()