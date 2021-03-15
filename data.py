#  open file ,'r' means read
my_file = open('data.txt', 'r')

# assign to a variable and go through the entire file with .read
file_content = my_file.read()

# make sure that you closed the file, avoid to have opened to many files at the same time
my_file.close()

print(file_content)
# Aleksandra

user_name = input("Enter your name: ")

#  open file for writing, 'w' means write, will rewrite all current in file
my_file_writing = open('data.txt', 'w')
my_file_writing.write(user_name)

my_file_writing.close()

