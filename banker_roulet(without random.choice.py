import random
names = input("Enter the names seperated by comma: ")
seperate_name = names.split(", ")
length = len(seperate_name)

random_var = random.randint(0, length)
bill_payer = seperate_name[random_var]
print(bill_payer+" is going to pay bill")