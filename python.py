### Dev 1 changes
my_list = [1,2,3,4,5]

for num in my_list:
	print (num)

	
### Dev 2 changes
strings = ["one","two","three"]

for str in strings:
	print (str)


#### Dev1 changes ######
str = "This is an example code and the code is written in python"

count = 0
str_split = str.split(" ")
for chars in str_split:
  if chars == "code":
    count += 1
print (count)
