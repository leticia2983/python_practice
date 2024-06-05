count=0
while count< 10:
    print(count)
    count+=1

tuple1=('Apple','veg','fish',1,5,33,'banana',3,'kiwi')
for item in tuple1:
        if item == 'Apple':
            continue
        if item == 3:
          break
        print(item)

tuple2=('fig','carrot',"brocolli")

new_tuple=tuple1+tuple2
print("this is my new tuple",new_tuple)
print("this was my original tuple",tuple1)
print("tuples are immutable,you can concatanate two tuples to make a new tuple! but you cannot chande a contents of a tuple. ")


