# To Run the program, ensure password txt is inside the folder
# have python2.10
python3 rainbow.py Passwords.txt

# reduction function
# same as tutorial stated, reduction = MD5(password) mod sizeOfPasswordFile
# reduction function below, declare hash_words and total number of passwords in arguments
def reduce_hash(hash_words, total_passwords):
    # # convert the hex taken from previous hash_md5 function into long number
    # # without prefix 0x, need to specify the base explicity
    reduce_words = int(hash_words, 16)
    # reduction of 1st unused, r = int(MD5(Password) mod number of password) + 1
    # # int words % total passwords in Question 1
    reduce_value = reduce_words % total_passwords
    return reduce_value