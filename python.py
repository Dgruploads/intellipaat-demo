### Dev 1 changes
my_list = [1,2,3,4,5]

for num in my_list:
	print (num)

	
### Dev 2 changes
strings = ["one","two","three"]

for str in strings:
	print (str)


# Read the contents of the file
filename = "python.txt"
f = open(filename,"r")
print (f.read())

# Write some data to the file
fwrite = open(filename,"w")
fwrite.write("adding some test data")

# Reading the file again
f = open(filename,"r")
print (f.read())
