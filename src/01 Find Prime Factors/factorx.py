def get_prime_factorsx(num):
	if type(num) != int:
		raise TypeError("Parameter type is wrong, should be an Integer")
	listfactors = []
	num = abs(num)
	if num > 1:
		dividend = int(num)
		divisor = 2
		while dividend > 1:
			if dividend % divisor == 0:
				listfactors.append(divisor)
				dividend = dividend / divisor
			else:
				divisor += 1				
	return listfactors

# for i in range(0,15):
# 	test = get_prime_factorsx(i)
# 	print(test)
# test = get_prime_factorsx(630)
# print(test)
# test = get_prime_factorsx(15)
# print(test)
# test = get_prime_factorsx('xxx')
# print(test)
# test = get_prime_factorsx(3.14)
# print(test)