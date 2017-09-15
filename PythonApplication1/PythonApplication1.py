import sys
import operator
import time
import timeit
import numpy
import itertools
import math
from functools import reduce

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
    # runtime : 129.15s
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
    # runtime : 20.58595037460327
    # TODO: since 2 is a special case, reduce size of the sieve from 2m -> 1m
    #       also try using bit flipping
    # given a prime number, returns the next prime number in sequence
    def nextPrime(self, prime, primes):
        if prime < 2:
            return -1
        if prime == 2:
            return 3

        prime += 2
        # check in stepsize=2, since they will all be odd
        while not primes[prime] :
            prime += 2
        return prime
    
    def run(self):

        max = 2000000
        maxSqrt = int(max ** 0.5)

        print("max:", max, "; sqrt(max):", maxSqrt)

        # create sieve
        primes = [True] * (max+1)

        print("\"True\" size:      ", sys.getsizeof(True))
        print("sizeof(primes[0]):", sys.getsizeof(primes[0]))
        print("sizeof(primes):   ", sys.getsizeof(primes))

        # True = prime, False = not prime
        # prime[0] = 0, prime[1] = 1, etc.
        primes[0] = False
        primes[1] = False
        prime = 2

        while prime < maxSqrt :
            for i in range(prime*prime, max, prime) :
                primes[i] = False
            prime = self.nextPrime(prime, primes)

        sum = 2
        for i in range(3, len(primes), 2) :
            if primes[i]:
                sum += i
        
        print(sum)


class Euler11:
    # runtime : 0.01751232147216797
    size = 4    # number of items to multiply (4 in problem 11)

    def getLargest(self, matrix) :
        largest = 0
        for array in matrix :
            for i in range(0, len(array)-self.size) :
                product = reduce(operator.mul, array[i:i+4])
                if(product > largest) :
                    largest = product
        return largest

    def getLargestDiagonal(self, matrix) :
        largest = 0
        # diagonal product - top left to bottom right (\)
        for i in range(0, len(matrix)-self.size) :
            for j in range(0, len(matrix[i])-self.size) :
                product = 1
                for k in range(0,self.size) :
                    product *= matrix[i+k][j+k]
                if product > largest :
                    largest = product
        # diagonal product - top right to bottom left (/)
        for i in range(0, len(matrix)-self.size) :
            for j in range(len(matrix[i])-1, self.size-1, -1) :
                # print(j,' ','')
                product = 1
                for k in range(0,self.size) :
                    product *= matrix[i+k][j-k]
                if product > largest :
                    largest = product
        return largest

    def getLargestTotal(self, matrix) :
        hori = self.getLargest(matrix)
        vert = self.getLargest(zip(*matrix))
        diag = self.getLargestDiagonal(matrix)
        print(hori, vert, diag)
        return max(vert,hori,diag)
        
    def run(self) :
        text = """08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
                49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
                81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
                52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
                22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
                24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
                32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
                67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
                24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
                21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
                78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
                16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
                86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
                19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
                04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
                88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
                04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
                20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
                20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
                01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48"""

        mat = []
        for line in text.splitlines():
            mat.append(list(map(int, line.lstrip().split(" "))))

        largest = self.getLargestTotal(mat)
        print(largest)

class Euler12: 
    # answer  : 76576500
    # runtime : 140.14999842643738
    # TODO: use prime factorization to solve
    
    def getDivisors(self, n) :  # returns the number of divisors for a number
        divs = 0
        sqrt = int(n**0.5)
        if n % 2 == 0:  # if n is even, stepsize = 1; n is odd, stepsize = 2
            for i in range(1, sqrt+1, 1):
                if n % i == 0:
                    divs += 2  # if n is divisible by i, then it is also divisible by (n/i), hence the +2
        else:   
            for i in range(1, sqrt+1, 2):
                if n % i == 0:
                    divs += 2

        if (sqrt ^ 2 == n):  # in case n is a perfect square, only should count once
            divs -= 1
        return divs
    
    def run(self) :
        num = 1
        tri = 1
        longest = 0     # for debugging

        while longest < 500:
            num += 1
            tri += num
            length = self.getDivisors(tri)
            if(length > longest) : longest = length     # for debugging
        
        print("longest:", longest)
        print("answer  :", tri)

class Euler13: 
    # answer  : 5537376230
    # runtime : 0.0010006427764892578

    def run(self):
        text = """37107287533902102798797998220837590246510135740250
                46376937677490009712648124896970078050417018260538
                74324986199524741059474233309513058123726617309629
                91942213363574161572522430563301811072406154908250
                23067588207539346171171980310421047513778063246676
                89261670696623633820136378418383684178734361726757
                28112879812849979408065481931592621691275889832738
                44274228917432520321923589422876796487670272189318
                47451445736001306439091167216856844588711603153276
                70386486105843025439939619828917593665686757934951
                62176457141856560629502157223196586755079324193331
                64906352462741904929101432445813822663347944758178
                92575867718337217661963751590579239728245598838407
                58203565325359399008402633568948830189458628227828
                80181199384826282014278194139940567587151170094390
                35398664372827112653829987240784473053190104293586
                86515506006295864861532075273371959191420517255829
                71693888707715466499115593487603532921714970056938
                54370070576826684624621495650076471787294438377604
                53282654108756828443191190634694037855217779295145
                36123272525000296071075082563815656710885258350721
                45876576172410976447339110607218265236877223636045
                17423706905851860660448207621209813287860733969412
                81142660418086830619328460811191061556940512689692
                51934325451728388641918047049293215058642563049483
                62467221648435076201727918039944693004732956340691
                15732444386908125794514089057706229429197107928209
                55037687525678773091862540744969844508330393682126
                18336384825330154686196124348767681297534375946515
                80386287592878490201521685554828717201219257766954
                78182833757993103614740356856449095527097864797581
                16726320100436897842553539920931837441497806860984
                48403098129077791799088218795327364475675590848030
                87086987551392711854517078544161852424320693150332
                59959406895756536782107074926966537676326235447210
                69793950679652694742597709739166693763042633987085
                41052684708299085211399427365734116182760315001271
                65378607361501080857009149939512557028198746004375
                35829035317434717326932123578154982629742552737307
                94953759765105305946966067683156574377167401875275
                88902802571733229619176668713819931811048770190271
                25267680276078003013678680992525463401061632866526
                36270218540497705585629946580636237993140746255962
                24074486908231174977792365466257246923322810917141
                91430288197103288597806669760892938638285025333403
                34413065578016127815921815005561868836468420090470
                23053081172816430487623791969842487255036638784583
                11487696932154902810424020138335124462181441773470
                63783299490636259666498587618221225225512486764533
                67720186971698544312419572409913959008952310058822
                95548255300263520781532296796249481641953868218774
                76085327132285723110424803456124867697064507995236
                37774242535411291684276865538926205024910326572967
                23701913275725675285653248258265463092207058596522
                29798860272258331913126375147341994889534765745501
                18495701454879288984856827726077713721403798879715
                38298203783031473527721580348144513491373226651381
                34829543829199918180278916522431027392251122869539
                40957953066405232632538044100059654939159879593635
                29746152185502371307642255121183693803580388584903
                41698116222072977186158236678424689157993532961922
                62467957194401269043877107275048102390895523597457
                23189706772547915061505504953922979530901129967519
                86188088225875314529584099251203829009407770775672
                11306739708304724483816533873502340845647058077308
                82959174767140363198008187129011875491310547126581
                97623331044818386269515456334926366572897563400500
                42846280183517070527831839425882145521227251250327
                55121603546981200581762165212827652751691296897789
                32238195734329339946437501907836945765883352399886
                75506164965184775180738168837861091527357929701337
                62177842752192623401942399639168044983993173312731
                32924185707147349566916674687634660915035914677504
                99518671430235219628894890102423325116913619626622
                73267460800591547471830798392868535206946944540724
                76841822524674417161514036427982273348055556214818
                97142617910342598647204516893989422179826088076852
                87783646182799346313767754307809363333018982642090
                10848802521674670883215120185883543223812876952786
                71329612474782464538636993009049310363619763878039
                62184073572399794223406235393808339651327408011116
                66627891981488087797941876876144230030984490851411
                60661826293682836764744779239180335110989069790714
                85786944089552990653640447425576083659976645795096
                66024396409905389607120198219976047599490197230297
                64913982680032973156037120041377903785566085089252
                16730939319872750275468906903707539413042652315011
                94809377245048795150954100921645863754710598436791
                78639167021187492431995700641917969777599028300699
                15368713711936614952811305876380278410754449733078
                40789923115535562561142322423255033685442488917353
                44889911501440648020369068063960672322193204149535
                41503128880339536053299340368006977710650566631954
                81234880673210146739058568557934581403627822703280
                82616570773948327592232845941706525094512325230608
                22918802058777319719839450180888072429661980811197
                77158542502016545090413245809786882778948721859617
                72107838435069186155435662884062257473692284509516
                20849603980134001723930671666823555245252804609722
                53503534226472524250874054075591789781264330331690"""

        lst = list(map(int, text.splitlines()))
        num = sum(lst)
        print(str(num)[0:10])

class Euler14: 
    # answer  : 837799
    # runtime : 69.31155300140381
    # note: using bitwise operations did not affect runtime, nor did not using membership function for dict

    def run(self): 
        # use a dictionary to keep chain #s for numbers
        collatz = {1:1}
        longest = 1
        maxnum = 1000000

        for i in range(2, maxnum+1):
            count = 1
            n = i
            while n != 1:
                if n in collatz: 
                    count += collatz[n]
                    break
                if n % 2 == 0:    # if even, n = n/2
                    n /= 2 
                else:
                    n = (3*n)+1   # if odd, n = 3n+1
                count += 1      # increment count 
            collatz[i] = count  # add number into dictionary
            # if count > longest: 
            # print("num:", i, "; count:", count)
        
        maxchain = max(collatz, key=collatz.get)
        print("answer:", maxchain)

class Euler14_2:
    # answer  : 837799
    # runtime : 49.1329185962677
    # note: second try, using recursion to cache all path sizes for a number
    #       starting from 1,000,000 and going down to 2 did not change runtime
    collatz = {1:1}

    def colget(self, n):
        if n == 1:          # base case
            return 1
        if n in self.collatz:    # if in dictionary, return cached size
            return self.collatz[n]
        if n % 2 == 0:      # if n is even, n/2
            chainsize = self.colget(n/2)+1
            self.collatz[n] = chainsize
            return chainsize
        elif n % 2 == 1:    # if n is odd, 3n+1
            chainsize = self.colget(3*n+1)+1
            self.collatz[n] = chainsize
            return chainsize
        else:
            raise ValueError("you suck")

    def run(self): 
        # use a dictionary to keep chain #s for numbers
        longest = 1
        maxnum = 1000000

        for i in range(2, maxnum+1):
            self.colget(i)
        
        maxchain = max(self.collatz, key=self.collatz.get)
        print("answer:", maxchain)

class Euler15: 
    # answer  : 137846528820
    # runtime : 0.0005002021789550781

    pathcount = 0

    # recursively find all possible paths
    # path = current path in string format
    # r = right moves left to use
    # d = down moves left to use
    # TAKES TOO LONG!!! the problem is a "central binomial coefficient"
    def pathfind(self, r, d):
        # print("r:",r,"d:",d)
        if r == 0 and d == 0:   # base case; all moves are used up
            # self.paths.append(path)
            self.pathcount += 1
        else:
            if r > 0: self.pathfind(r-1, d)
                # self.pathfind(path+"R", r-1, d)
            if d > 0: self.pathfind(r, d-1)
                # self.pathfind(path+"D", r, d-1)
        return

    # use central binomial coefficient to calculate the number of paths
    def run(self):
        num = 20
        answer = 0

        answer = math.factorial(2*num) / (math.factorial(num)**2)
        print(answer)
        return

class Euler16:
    # answer  : 1366
    # runtime : 0.002086851509824238
    # TODO: probably some mathematical secrets behind this one as well
    def run(self):
        num = 2 ** 1000
        sum = 0

        while(num > 0):
            sum += num % 10
            num = num // 10  # need to use floor division to avoid float precision issue
            # print(num, num % 10)
        print(sum)
        return

    # answer  : 1366
    # runtime : 0.002156555771320417
    def run2(self):
        num = 0
        print(sum( int(n) for n in str(2**1000) ))


class Euler17:
    # answer  : 21124
    # runtime : 0.001244841136290647

    worddict = {1:"one", 2:"two", 3:"three", 4:"four", 5:"five"\
                , 6:"six", 7:"seven", 8:"eight", 9:"nine"\
                , 10:"ten", 11:"eleven", 12:"twelve", 13:"thirteen"\
                , 14:"fourteen", 15:"fifteen", 16:"sixteen", 17:"seventeen"\
                , 18:"eighteen", 19:"nineteen", 20:"twenty", 30:"thirty"\
                , 40:"forty", 50:"fifty", 60:"sixty", 70:"seventy"\
                , 80:"eighty", 90:"ninety", 100:"hundred", 1000:"thousand"}
    
    def run(self):
        num = 1000
        length = 0
        length100 = 0

        # create a dictionary of lengths since im too lazy to type them out again
        lendict = self.worddict.copy()
        for key in lendict.keys():
            lendict[key] = len(lendict[key])
        lendict['and'] = 3

        # calculate length of 1 ~ 99 first, then multiply it afterwards with hundreds added in
        for i in range(1, 99+1):
            if i in lendict:
                length100 += lendict[i]
            else: # twenty-one, thirty-one, forty-one etc. compound numbers
                length100 += lendict[(i//10)*10] + lendict[i%10]

        length += length100
            
        # calculate length of 100~1000 using the length of 1~99
        for i in range(1, 10):
            length += lendict[i] + lendict[100] # for the hundreds

            nHundredAnd = lendict[i] + lendict[100] + lendict['and'] 
            length += nHundredAnd * 99 + length100

        # add "one thousand"
        length += lendict[1] + lendict[1000]

        print(length)
        
        return


class Euler18: 
    # answer  : 1074
    # runtime : 0.0010836233044866023
    # note    : took me 2 minutes to do it by hand, by crossing out numbers below 10 
    #           and highlighting numbers higher than 80. just eyeing worked for this
    #           small triangle
    
    triangle = """75
                  95 64
                  17 47 82
                  18 35 87 10
                  20 04 82 47 65
                  19 01 23 75 03 34
                  88 02 77 73 07 63 67
                  99 65 04 28 06 16 70 92
                  41 41 26 56 83 40 80 70 33
                  41 48 72 33 47 32 37 16 94 29
                  53 71 44 65 25 43 91 52 97 51 14
                  70 11 33 28 77 73 17 78 39 68 17 57
                  91 71 52 38 17 14 91 43 58 50 27 29 48
                  63 66 04 68 89 53 67 30 73 16 69 87 40 31
                  04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""
    def run(self):
        triList = []
        # parse the triangle into list of lists
        for line in self.triangle.splitlines():
            temp = line.strip().split(' ')
            triList.append(list(map(int, temp)))

        # work up from the bottom to get the best solution
        for i in range(len(triList)-2, -1, -1):
            for j in range(0, len(triList[i])):
                triList[i][j] += max(triList[i+1][j], triList[i+1][j+1])

        print(triList[0][0])
        return


class Euler19: 
    # answer  : 171
    # runtime : 0.016649055293439973
    # note    : solved without using datetime libraries

    def run(self):
        firstSuns = 0
        year = 1900
        month = 1
        totalDays = 1   # use with mod 7 to get day of the week (mod7==0 means Sunday)
        
        # december is 0 for purposes of mod12
        daysofmonth = {1:31, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 0:31}

        # skip the first year
        totalDays += 365
        year = 1901

        # mod the daycount of every 1st day of the month??
        while year < 2001:
            monthmod = month % 12

            if totalDays % 7 == 0: firstSuns += 1

            if monthmod == 2:       # february
                if year % 4 == 0:   # leap year logic
                    if year % 100 != 0 or year % 400 == 0: 
                        totalDays += 29
                else: 
                    totalDays += 28    
            
            else:                   # all other months
                totalDays += daysofmonth[monthmod]

            if monthmod == 0: 
                year += 1 # december -> january: add a year
            
            month += 1

        print(firstSuns)
        return


class Euler20: 
    # answer  : 648
    # runtime : 0.0013709930205935467

    def run(self):
        num = math.factorial(100)
        print(sum(int(n) for n in str(num)))
        return

# main code starts here
t0 = timeit.default_timer()
euler = Euler20()
euler.run()
print(timeit.default_timer()-t0)