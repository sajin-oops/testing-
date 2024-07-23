'''
Question -str_ip = "34,5,2,8, 9". Given a string of numbers and comma, add the numbers
delimited by comma to a list. Use continue.
'''

str_ip = "34,5,2,8,9"
num_list = []
elements = str_ip.split(",")
#  OUTPUT 34,5,2,8,9
for elements in elements:
    elements = elements.strip()
    if elements == "":
        continue
    num_list.append(int(elements))
print(num_list)

# output [34, 5, 2, 8, 9] final output