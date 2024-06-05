import sys
instance_type = sys.argv[1]
if instance_type == "t2.medium":
    print("t2.medium will cost you 2 dollars")

elif instance_type == "t2.micro":
    print("t2.micro will cost you 4 dollars")

elif instance_type == "t2.xlarge":
    print("t2.xlarge will cost you 8 dollars")

else:
    print("your instance type is invalid")

