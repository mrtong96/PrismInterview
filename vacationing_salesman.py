
import sys

def main(*args):
	destinations = ['Paris, France', 'New York City, USA', 'Nuuk, Greenland']

	distances = {}

	# how to add distacnes for arbitrary modes of transportation. Only doing crow's
	# flight because not possible to do it any of the other listed methods
	d = {}
	d[(destinations[0], destinations[1])] = 5844.0
	d[(destinations[1], destinations[0])] = 5844.0
	d[(destinations[0], destinations[2])] = 3585.0
	d[(destinations[2], destinations[0])] = 3585.0
	d[(destinations[1], destinations[2])] = 2984.0
	d[(destinations[2], destinations[1])] = 2984.0

	distances["crow's flight"] = d

	# get command line args, 1st arg is file name
	data = sys.stdin.read()
	data = filter(lambda x: x, data.split('\n'))
	data = map(lambda x: x.strip(), data)

	# output string
	out = ''

	# some args you can change via options in txt
	total_dist = 0
	dist_mode = 'km'
	optimized = True
	possible_modes = ["crow's flight"]
	trans_mode = "crow's flight"

	for line in data:
		# trying to find route to something
		if line in destinations:
			if out:
				raise Exception('Error: can only have one destination')

			dsts = filter(lambda x: x != line, destinations)
			d = distances[trans_mode]

			# picks longer or shorter distance based on distances and optimized flag
			if (d[line, dsts[0]] + d[dsts[0], dsts[1]] <\
				d[line, dsts[1]] + d[dsts[1], dsts[0]]) ^ (not optimized):
				out += '\t {} -> {}: {} {}\n'.format(line, dsts[0], d[line, dsts[0]], dist_mode)
				out += '\t {} -> {}: {} {}\n'.format(dsts[0], dsts[1], d[dsts[0], dsts[1]], dist_mode)
				total_dist = d[line, dsts[0]] + d[dsts[0], dsts[1]]
			else:
				out += '\t {} -> {}: {} {}\n'.format(line, dsts[1], d[line, dsts[1]], dist_mode)
				out += '\t {} -> {}: {} {}\n'.format(dsts[1], dsts[0], d[dsts[1], dsts[0]], dist_mode)
				total_dist = d[line, dsts[1]] + d[dsts[1], dsts[0]]
		else:
			try:
				if '--distance' == line[:len('--distance')] or 'd' == line[2:]:
					dist = line.split(' ')[1].lower()
					if dist == 'm' or dist == 'miles':
						dist_mode = 'miles'
						conv = 0.621371
						for mode in distances:
							for key in distances[mode]:
								distances[mode][key] = round(distances[mode][key] * 0.621371)
				elif '--optimize' == line[:len('--optimize')] or '-o' == line[2:]:
					data = line.split(' ')
					if len(data) == 2:
						result = data[1].lower()
						if result == 'false':
							optimized = False
				elif '--by' == line[:len('--by')] or '--trans_mode' == line[:len('--trans_mode')] or \
					'-b' == line[:2] or '-t' == line[:2]:
					method = line.split(' ')[1]
					if method not in possible_modes:
						raise Exception('Error: invalid transportation mode. Valid modes are: {}'.format(possible_modes))
					else:
						trans_mode = method
				elif '--help' == line[:len('--help')] or '-h' == line[:2]:
					help_file =\
"""
This is a program that finds the itinerary to visit three destinations:
Paris, New York City, and Nuuk. To run this program, run it in the form of:
'python vacationing_salesman.py < (input file)'. In the input file, please
write only one parameter per line with the destination in the last line.
Optional arguments are:
	--distance, -d: default is distance in kilometers, use 'm' or 'miles' for distance in miles
	--optimize, -o: default is to optimize, if flag is set to false, will return the longer path
	--by, -b, --trans_mode, -t: transportation mode, switch the transportation mode of the path
	--help, -h: display this help file
"""
					sys.stdout.write(help_file)
					return
			except Exception as e:
				raise Exception('Error: error parsing line: {}'.format(line))

	if not out:
		raise Exception('Error: no valid destination found\n')
	if optimized:
		out = 'Success! Your *optimized* vacation itinerary by {} is:\n\n'.format(trans_mode) + out
	else:
		out = 'Success! Your vacation itinerary by {} is:\n\n'.format(trans_mode) + out
	out += '\n Total distance covered in your trip: {} km\n'.format(total_dist)
	sys.stdout.write(out)

if __name__ == "__main__":
    main()
