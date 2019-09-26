import math

def list_mean(V):
	mean = None
	try:
		mean = sum(V) / len(V)
	except ZeroDivisionError as error:
		raise ZeroDivisionError('ZeroDivisionError: V has len 0')
	return mean

def list_stdev(V):
	mean = list_mean(V)
	stdev = None
	try:
		stdev = math.sqrt(sum([(mean-x)**2 for x in V]) / (len(V) - 1))
	except ZeroDivisionError as error:
		raise ZeroDivisionError('ZeroDivisionError: V has len 0')
	return stdev
