import hashlib
import sys 

hash_table = []
rainbow_table = []
words_list = []

# Open and print number of password in text file
with open(sys.argv[1],'r') as f:
    for line in f:
        # remove empty passwords if needed
        if line == "":
            pass
        else:
            # add conditions so is easier to check if password is used
            # False = unused, hence it will look like (words, False)
            contents = line.strip('\n')
            words_list.append([contents, False])
            total_passwords = len(words_list)
    # print(words_list)
    print('Total number of passwords in Password.txt: ' + str(total_passwords))
    
def hash_md5(words):
    # # lets say first unused password is 10th, using MD5 Hash Function, hv = MD5(10th)
    # # storing the list of passwords into list and calling the first element
    # first_element = words_list[0]
    # # hashing the first element using md5 hash and converting to hex
    # first_element_hex = hashlib.md5(first_element.encode('ascii')).hexdigest()
    # print(first_element_hex)
    words_hash = hashlib.md5(words.encode('ascii')).hexdigest()
    return words_hash

def reduce_hash(hash_words, total_passwords):
    # # convert the hex into long number
    # # without prefix 0x, need to specify the base explicity
    # first_element_int = int(first_element_hex, 16)
    # print(first_element_int)
    reduce_words = int(hash_words, 16)
    # reduction of 1st unused, r = int(MD5(Password) mod number of password) + 1
    # # int words % total passwords in Question 1
    reduce_value = reduce_words % total_passwords
    return reduce_value

# check if hash inside the rainbow (step 2, 1)
def check_hash(hash_value):
    for k in rainbow_table:
        if hash_value == k[1]:
            print("The hashes in rainbow table exist")
            return(k, True)
    return(None, False)

def create_rainbow():
    rainbow_counter = 0
    # creating hash chain as same as lecture
    for words in words_list:
        last_hash = ""
        # double check if back is False from reading file function
        # (content[0], boolean[1])
        # print(words[1])
        if words[1] == False:
            words_hash = hash_md5(words[0])
            # print(words_hash)
            # change to condition to True when hashed
            words[1] = True
            # reduce 4 times, (step 1, 2c)
            for t in range(4):
                reduced_val = reduce_hash(words_hash, total_passwords)
                reduced_hash = hash_md5(words_list[reduced_val][0])
                last_hash = reduced_hash
                words_list[reduced_val][1] = True
            # (step 1, 2d)
            rainbow_table.append([words[0], last_hash])
            rainbow_counter += 1
    # sort the rainbow table by hash, (step 1, 3)
    rainbow_table.sort(key=lambda x:x[1])
    print("Total number in rainbow table: " + str(rainbow_counter))
    return rainbow_table

# create new rainbow file and write, (step 1, 4)
def write_rainbowfile(rainbow_table):
    j = open('Rainbow.txt','w')
    for i in rainbow_table:
        j.write(str(i[0]) + "|" + str(i[1]) + "\n")
    j.close
    
def find_hash(hash_value):
    # Check if hash is in rainbow table
    main_hash = hash_value
    result = check_hash(hash_value)
    if result[1] == True:
        # declaring preimage
        pre_image = hash_md5(result[0][0])
        # user hash value matches first of hash chain, (step 2, 2)
        if hash_value == pre_image:
            return "Pre-image has been found, the word is " + result[0]
        else:
            # reduce again for 4 times, (step 2, 2)
            for k in range(4):
                reduced_val = reduce_hash(pre_image, total_passwords)
                pre_image2 = hash_md5(words_list[reduced_val][0])
                # (step 2, 4)
                if hash_value == pre_image2:
                    return "Pre-image has been found, the word is " + words_list[reduced_val][0]
                    break
                else:
                    pre_image2 = pre_image2
    else:
        # if hash cant be found
        while result[1] != True:
            # reduce again, (step 2, 3)
            reduced_val = reduce_hash(pre_image, total_passwords)
            pre_image = hash_md5(words_list[reduced_val][0])
            result = check_hash(pre_image)
            hash_value = pre_image
            # when hash is found in the rainbow table
            starting_point =  rainbow_table.index(result[0])
            for r in rainbow_table[starting_point-1:]:
                    pre_image = hash_md5(r[0])
                    if pre_image == main_hash:
                        return "Pre-image has been found, the word is " + r[0]
                        break
                    else:
                        # reduce 4 times again, (step 2, 4)
                        for t in range(4):
                            reduced_val = reduce_hash(pre_image, total_passwords)
                            pre_image2 = hash_md5(words_list[reduced_val][0])
                            # if found in the chain
                            if pre_image2 == main_hash:
                                return "Pre-image has been found, the word is " + words_list[reduced_val][0]
                                break
                            else:
                                pre_image = pre_image2
        else:
            # return invalid message
            return "Matching hash value cant be found."

def main():
    # create rainbow table
    create_rainbow()
    # write into a new file
    write_rainbowfile(rainbow_table)
    # ask for user input to check hash and the length should be 32
    user_input = input("Enter the Hash value: ")
    if len(user_input) == 32:
        print(find_hash(user_input))
    else:
        print("Hash needs to be the length of 32, invalid input.")

if __name__ == "__main__":
    main()
