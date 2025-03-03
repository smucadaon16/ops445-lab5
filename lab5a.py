#!/usr/bin/env python3
# Author ID: smucadaon

def read_file_string(file_name):
	# Takes file_name as string for a file name, returns its entire contents as a string
	f = open(file_name, 'r')
	context = f.read()
	f.close()
	return context

def read_file_list(file_name):
	# Takes file_name as string for a file name,
	# returns its entire contents as a list of lines without new-line characters
	f = open(file_name, 'r')
	r_data = f.read()
	f.close()
	r_data.split('\n')
	item_lines = r_data.split('\n')
	unempty_lines = []
	for line in item_lines:
		if line != '':
			unempty_lines.append(line)
	return unempty_lines

if __name__ == '__main__':
	file_name = 'data.txt'
	print(read_file_string(file_name))
	print(read_file_list(file_name))
