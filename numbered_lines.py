#!/usr/bin/env python

def main():

	with open("small.txt", "r") as f:
		data = f.readlines()

	with open("small_results.txt", "w") as g:
		i = 1
		for line in data:
			g.write("{0} {1}".format(i, line))
			i += 1

if __name__ == '__main__':
    main()