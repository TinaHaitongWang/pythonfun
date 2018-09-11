def main():
	add_two(3,5)
	subtract_two(2,1)
	multiply_two(5,5)

def add_two(v1,v2):
	"""do somthing 
	"""
	p = v1+ v2
	print(p)
def subtract_two(v1,v2):
	"""do more
	"""
	p = v1 -v2
	print(p)
def multiply_two(v1, v2):
	"""multiply two numbers

	:param v1: number one
	:param v2: number two
	:returns: product number
	"""
	p = v1 *v2
	print(p)
	
	return p
if _name_ =="_main_":
	main()
