# Implementing a rainbow table to a list of passwords with reduction function
To Run the program, ensure password txt is inside the folder, have python3.11 environment
python3 rainbow.py Passwords.txt

reduction function
same as tutorial stated, reduction = MD5(password) mod sizeOfPasswordFile -> MD5(password) % total number of passwords
reduction function below, declare hash_words and total number of passwords in arguments

