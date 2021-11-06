def power(number):
    print(number)
power(2*2)


def power(a,b):
  if b == 1:
    return a
  else:
    return a*power(a,b-1)
print (power(6,2))
