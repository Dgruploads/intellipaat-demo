### Dev 1 changes
my_list = [1,2,3,4,5]

for num in my_list:
	print (num)

	
### Dev 2 changes
strings = ["one","two","three"]

for str in strings:
	print (str)

### Reading data from python.txt file
filename = "python.txt"
fread = open(filename,"r")
print (fread.read())
