def mystery(limit):
	nums = []
	for n in range(2, limit):
		# print("n:",n)
		for x in range(2, n):
			# print("x:",x)
			# print("n%x=", n%x)
			if n % x == 0:
				# print("achou:", n, x)
				break
		else:
			# print("não achou..., dá append ")
			nums.append(n)
	return nums	



nums = mystery(100)
print(nums)
print(len(nums))