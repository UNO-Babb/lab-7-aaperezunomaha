
from NumberTests import isPrime
from NumberTests import getFactors
from NumberTests import isEven


#Problem 10 - Summation of primesThe sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#Find the sum of all the primes below two million.

#Test your new functions in this main
def main():
  total = 0
#knownPrimes = [3, 7, 11, 13, 17]
#num = int(input("2000000: "))
  for num in range(1, 2000001):
    if isPrime(num):
       total = num + total 
       print("sum of all 2million primes:", total)
       #print("%d is a prime number" %(num))

  #if isEven(num):
    #print("%d is an even number" %(num))


if __name__ == '__main__':
    main()
