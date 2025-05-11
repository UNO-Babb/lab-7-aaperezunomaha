
from NumberTests import isPrime
from NumberTests import getFactors
from NumberTests import addNum

#def main():
 # number = 10001
  #factors = getFactors(number)
  #print(factors)
  
  #for f in factors:
   # if isPrime(f):
    #  prin

def main():


   knownPrimes = [3, 7, 11, 13, 17]
   count = len(knownPrimes)
   num = knownPrimes[1]
   while count < 10001:
       num = num + 1
       if isPrime(num):
           addNum(knownPrimes, num)
           count = count + 1
           print("the 10001 prime is:", knownPrimes[-1])

  
    


if __name__ == '__main__':
    main()

#Problem 7 - 10001st prime
#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10001st prime number?