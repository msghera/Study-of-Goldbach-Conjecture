class sieve :
	def __init__(self, __limit = 1000002):
		self.__limit = __limit 

		self.prime = [2]
		self.bs = [1]*__limit
		self.bs[0]=0
		self.bs[1]=0
		for i in range(4, __limit, 2) : self.bs[i] = 0
		for i in range(3, __limit, 2) : 
			if self.bs[i] == 1 :
				self.prime.append(i)
				for j in range(i*i, __limit, i) : self.bs[j] = 0

	def get_limit (self) : 
		return self.__limit 

	def __len__ (self) : 
		return len(self.prime) 

	def get_prime(self, n):
		try:
			return self.prime[n-1]
		except:
			print('Range out of bound.')
	
	def is_prime(self, num):
		if num <= self.__limit :
			return True if self.bs[num] == 1 else False
		else :
			for _prime in prime :
				if num%prime == 0 :
					return False
			return True

if __name__ == '__main__':
	s = sieve()
	print(s.bs[:10])
