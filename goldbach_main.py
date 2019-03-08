from sieve import sieve 
import pandas as pd
import matplotlib.pyplot as plt 
from scipy.interpolate import make_interp_spline, BSpline


if __name__ == '__main__':
	s = sieve()
	prime_count = s.bs[:]
	prime = s.prime
	for i in range(1, len(prime_count)): prime_count[i] += prime_count[i-1]

	g_count = []
	for i in range(4, 1000000, 2): 
		cur_prime_id = 0
		count = 0 
		while prime[cur_prime_id] <= (i/2):
			left = i - prime[cur_prime_id]
			if s.is_prime(left) : count+= (1 if left == prime[cur_prime_id] else 2)
			cur_prime_id += 1
		g_count.append((i, prime_count[i-1], count))

	df = pd.DataFrame()
	df['N'] = [i[0] for i in g_count]
	df['Prime Found'] = [i[1] for i in g_count]
	df['Sum Made'] = [i[2] for i in g_count]
	df['Probability'] = [i[2]/i[1] for i in g_count]
	df.to_csv('output.csv', index=False)

	plt.plot(df['N'], df['Probability'])
	plt.legend()
	plt.show()
