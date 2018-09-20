def main():
	p = add_three(3,5,4)
	multipleTheAnswer(3,p)

def add_three(v1,v2,v3):
	"""do somthing 
	"""
	p = v1+ v2+v3
	print(p)
	return p
def multipleTheAnswer(v1, v2):
	"""multiply two numbers

	:param v1: number one
	:param v2: number two
	:returns: product number
	"""
	p = v1 *v2
	print(p)
	
	return p
if __name__ =="__main__":
	main()
