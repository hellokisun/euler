from functools import reduce
import operator
import time

class Util:
    def isPrime(n):
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
            return True


class Euler4:
    def isPalindrome(n):
        return str(n) == str(n)[::-1]


class Euler5:
    def div20(n):
        for i in range(19, 3, -1):
            if (n % i != 0):
                return False
            return True
    
    def run():
        num = 20
        while not div20(num):
            num += 20

        print(num)


class Euler6:
    def run():
        sqsum = 0
        sumsq = 0

        for i in range(1,101):
            sqsum += i**2

        sumsq = sum(range(1,101))**2

        print(sumsq-sqsum)
    

class Euler7:
    def isPrime(n):
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
            return True
    
    def run():
        order = 1
        num = 2

        while order != 10001:
            num += 1
            if isPrime(num):
                order += 1

        print(num)


class Euler8:
        
    def prod(n):
        return reduce(operator.mul,n)
        #return reduce(lambda x, y: x*y, n)
    
    def run():
        str = "73167176531330624919225119674426574742355349194934"
        str += "96983520312774506326239578318016984801869478851843"
        str += "85861560789112949495459501737958331952853208805511"
        str += "12540698747158523863050715693290963295227443043557"
        str += "66896648950445244523161731856403098711121722383113"
        str += "62229893423380308135336276614282806444486645238749"
        str += "30358907296290491560440772390713810515859307960866"
        str += "70172427121883998797908792274921901699720888093776"
        str += "65727333001053367881220235421809751254540594752243"
        str += "52584907711670556013604839586446706324415722155397"
        str += "53697817977846174064955149290862569321978468622482"
        str += "83972241375657056057490261407972968652414535100474"
        str += "82166370484403199890008895243450658541227588666881"
        str += "16427171479924442928230863465674813919123162824586"
        str += "17866458359124566529476545682848912883142607690042"
        str += "24219022671055626321111109370544217506941658960408"
        str += "07198403850962455444362981230987879927244284909188"
        str += "84580156166097919133875499200524063689912560717606"
        str += "05886116467109405077541002256983155200055935729725"
        str += "71636269561882670428252483600823257530420752963450"

        largest = 0

        t0 = time.time()
        for i in range(0,len(str)-14):
            if(str[i:i+13].find("0") > -1):
                continue
            p = prod(list(int(j) for j in str[i:i+13]))
            if(p > largest):
                largest = p

        t1 = time.time()
        print("runtime for algo #2: ", t1-t0)
        print(largest)


class Euler9:
    # runtime: 129.15s
    def isPyTriplet(self, a, b, c):
        if(a**2 + b**2 == c**2):
            return True
        return False

    def run(self):
        for a in range(1,1001):
            for b in range(a+1, 1001):
                for c in range(b+1, 1001):
                    if(a+b+c < 1000):
                        continue
                    elif(a+b+c > 1000):
                        break
                    # a+b+c should be 1000 here; sanity check below
                    # print (a, b, c, a+b+c)
                    if(self.isPyTriplet(a,b,c)):
                        print("Found! ", a, b, c, "; sum = ", a+b+c, "; product = ", a*b*c)
                        return

class Euler10:
    # given a prime number, returns the next prime number in sequence
    def nextPrime(n, sieve):
        if n < 2:
            return -1
        # n > 3, get the next item in sieve
        index = list.index(n)
        return 
        

    
    
    def run(self):

        max = 2000000
        maxSqrt = int(max ** 0.5)

        print("max:", max, "; sqrt(max):", maxSqrt)

        # create sieve
        sieve = list(range(1,max,2))
        
        # remove 1 and add 2
        sieve[0] = 2
        
        # starting prime
        prime = 3
        
        while prime**2 < maxSqrt :
            #print("current prime:", prime, "  removed:", end='')
            for i in range(prime**2, maxSqrt, prime):
                try: 
                    sieve.remove(i)
                    #print(i, end=' ')
                except ValueError:
                    pass 
            prime = sieve[sieve.index(prime)+1] # should return the next prime
            #print()


        print(sum(sieve))

# main code starts here


t0 = time.time()
euler = Euler10()
euler.run()
t1 = time.time()
print("runtime:", t1-t0)
