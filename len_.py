#!/usr/bin/env python

def len_(object):

	i = 0
	length = 0
	for i in object:
		length += 1
		i += 1
	return length

def main():
	test_list = [1, 2, 3]
	test_tuple = (1,2)
	test_string = "hey"
	test_dict = {"Fish": "swim", "Cheetah": "run", "Elephant": "stomp"}

	print len(test_list)
	print len(test_tuple)
	print len(test_string)
	print len(test_dict)

if __name__ == '__main__':
	main()