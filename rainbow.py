import hashlib
import sys 

# Open and print number of password in text file
with open(sys.argv[1],'r') as f:
    contents = f.read()
    words = contents.split()
# print('Number of words in text file: ', len(words))

# lets say first unused password is 10th, using MD5 Hash Function
# hv = MD5(10th)
# storing the list of passwords into list and calling the first element
words_list = words
first_element = words_list[0]
# hashing the first element using md5 hash and converting to hex
first_element_hex = hashlib.md5(first_element.encode('ascii')).hexdigest()
print(first_element_hex)

# convert the hex into long number
# without prefix 0x, need to specify the base explicity
first_element_int = int(first_element_hex, 16)
print(first_element_int)

# reduction of 1st unused, r = int(MD5(Password) mod number of password) + 1