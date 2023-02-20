my_file = open('C:/Users/DIVERGENT/Desktop/text.txt')
# this read just a line in the txt file
print(my_file.readline())
# this set the cursor to 0
my_file.seek(0)
# this makes a the text into
a = my_file.readlines()
print(a[0])
# need to close the file so we can use it again
my_file.close()
