#!/usr/bin/env python3
# Author ID: smucadaon

def append_file_string(file_name, string_of_lines):
	# Takes two strings, appends the string to the end of the file
	f = open(file_name, 'a')
	f.write(string_of_lines)
	f.close()

def read_file_string(file_name):
	# Takes two strings, appends the string to the end of the file
	f = open(file_name, 'r')
	context = f.read()
	f.close()
	return context

def write_file_list(file_name, list_of_lines):
	# Takes a string and list, writes all items from list to file where each item is one line
	f = open(file_name, 'w')
	for data in list_of_lines:
		f.write(data + '\n')
	f.close()

def write_file_list(file_name, list_of_lines):
	f = open(file_name, 'w')
	for items in list_of_lines:
		f.write(items + '\n')
	f.close()

def read_file_list(file_name):
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

def copy_file_add_line_numbers(file_name_read, file_name_write):
	# Takes two strings, reads data from first file, writes data to new file, adds line number to new file
	f_read = open(file_name_read, 'r')
	datax = f_read.readlines()
	f_read.close()

	f_write = open(file_name_write, 'w')
	count = 1
	for line_number in datax:
		data_with_number = str(count) + ':' + line_number
		f_write.write(data_with_number)
		count += 1
	f_write.close()


if __name__ == '__main__':
	file1 = 'seneca1.txt'
	file2 = 'seneca2.txt'
	file3 = 'seneca3.txt'
	string1 = 'First Line\nSecond Line\nThird Line\n'
	list1 = ['Line 1', 'Line 2', 'Line 3']
	append_file_string(file1, string1)
	print(read_file_string(file1))
	write_file_list(file2, list1)
	print(read_file_string(file2))
	copy_file_add_line_numbers(file2, file3)
	print(read_file_string(file3))
