import time

def sievePrimes0(candidates):
	"""Removes every non-prime number from the ordered list l."""
	candidates = list(candidates)
	# print(type(candidates))
	# N = 121
	for i in range(0, int(len(candidates) ** 0.5 + 1)):   # O(sqrt(N)) i = [0, 11]
		currentPrime = candidates[i]
		if currentPrime != 0:
			for j in range(i + currentPrime, len(candidates), currentPrime): 
				if candidates[j] % candidates[i] == 0:
					candidates[j] = 0
	return filter(lambda x : x != 0, candidates)


def sievePrimes1(l):
	"""Removes every non-prime number from the ordered list l."""
	l = list(l)
	if (l[0] * l[0] <= l[len(l) - 1]):
		l[1:] = sievePrimes1(list(filter(lambda x: x % l[0] != 0, l)))
	return l


def timeSieve(maxPrime, numTimes, sieveFunc):
	"""Times the sieve implementations."""
	t0 = 0
	for numTries in list(range(0, numTimes)):
		# taux = time.clock()
		taux = time.perf_counter()
		primes0 = sieveFunc(range(2, maxPrime))
		# t0 = t0 + time.clock() - taux
		t0 = t0 + time.perf_counter() - taux
	print (t0 / numTimes*100)


if __name__ == "__main__":

	print("testing sievePrimes0:")
	for n in [ 10, 50, 100, 500, 1000,5000, 10000, 50000, 100_000, 500_000]:
		timeSieve(n, 5, sievePrimes0)

	print("testing sievePrimes1:")
	for n in [ 10, 50, 100, 500, 1000,5000, 10000, 50000, 100_000, 500_000]:
		timeSieve(n, 5, sievePrimes1)

"""
testing sievePrimes0:
0.0012574599804793252
0.0014058600027055945
0.0023799399878043914
0.011993999996775528
0.027536080006029806
0.118882400001894
0.23357688000032795
1.3799134799955937
3.0060895799942955
17.5175703000059

testing sievePrimes1:
0.001211119997606147
0.0025547999848640757
0.003993120008090045
0.021648740003001876
0.050393080000503694
0.38591552000070806
0.9339465800076141
5.820952900003249
14.981230500006859
190.11555498000234


"""