# def greet(*names):
#     for name in names:
#         print("Hello", name)
# greet("sonu", "kartik", "umesh", "bijender")

# name=input("enter name")
# if "ing" and  "ly" in name:
#     print(name)
# else:
#     print(name+"lying")



def prime_number(num):
    i=1
    a=[]
    while i<1000:
        if num%i==0:
            print("prime number")
            a.append(num)
            print(a)
        else:
            print("not prime number")   
        i=i+1
prime_number()