"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    count = 0
    max = 100
    min = 1
    for i in range(min,max):
        for j in range(min,i): 
            if (i % j == 0)and(j!=1):
                    break
            elif i-1==j:
                list.append(i)
                count+=1
                if (count<number_of_primes):
                    break
                else:
                    return list


    return list  