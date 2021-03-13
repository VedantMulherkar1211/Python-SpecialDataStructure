#LIST...................................................................................
grocery=["vedant" , "sakshi" ," papa"  ,"mummy"]
print(grocery)
print(grocery[3])
number=[1 , 2 , 3 ,4 ,5 ,6 ,7 , 8]
print(number)
#SORT...............................................................................
number.sort()
print(number)
#REVERSE.................................................................................
number.reverse()
print(number)

number.reverse()
#SLICING...............................................................................
print(number[0:2])                #slissing
print(number[::2])                  #print(number[starting number:upto which number : number of gaps]
print(number[::3])
print(number[::-2])

#LENGTH.................................................................................
print(len(number))       #gives you length of list
#MAXIMUM..................................................................................
print(max(number))       #get maximum number
#MINIMUM..................................................................................
print(min(number))        #get minimum number
#APPEND...................................................................................
number.append(9)            #it will add the number at the end of the list
print(number)
number.append(10)
print(number)

#INSERT COMMAND.............................................................................

number.insert(3, 68)           #it will insert the value where you want in the list      number.insert(position,value)
print(number)

#REMOVE FUNCTION...............................................................................

number.remove(3)                #it will remove the selected number from the list
print(number)

#POP FUNCTION...................................................................................
number.pop()                    #it will remove the list element of the list
print(number)

#index function..................................................................................
new=[1,2,3,4,5,6,7,8,9,10,11,12]
print("index" ,new.index(4,1,7))
'''MUTABLE ----CAN BE CHANGE------LIST IS MUTABLE------LIST HAS SQUARE BRACKETS
    IMMUTABLE----CAN'T CHANGE------TUPLE IS IMMUTABLE-----TUPLE HAS PARANTESIS'''
#EXTENDE FUNCTION .................................................................................
new.extend(grocery)
print("Extende", new)

#CLEAR FUNCTION ...................................................................................
new.clear()
print("clear" , new)

#COPY FUNCTION.....................................................................................
list1=[1,2,3,4,5,6,7,8,9]
list2=list1
print("list2" , list2)
list2=list1.copy()
print("list2" , list2)

#TUPLE*************************************************************************************************
print("Its a tuple")
tp=(1,2,3,4,5)
print(tp)
'''tp[1]=8   #tp[1]=8 It does not change its value TypeError: 'tuple' object does not support item assignment
print(tp)'''

#LEN() IN TUPLE
print(len(tp))

'''#DELETE THE TUPLE
del tp  #Delete tuple completely
print("delete")'''

#CONVERTING TUPLE INTO LIST
new_tp=list(tp)    #........new variable=list(old tuple)
print(new_tp)

#CONVERTING LIST INTO TUPLE
new_tuple=tuple(new_tp)
print("new_tuple" , new_tuple)

'''so we can't directly changes the tuple to change the tuples vcalue we have 
to first convert the tuple into list and then change its value '''

#TO PRINT DATA TYPE OF THE TUPLE
my_tuple=("ved","sak" ,"papa" ,"mummy" ,1,2,3,4,5)
my_tuple1=("ved","sak" ,"papa" ,"mummy")
my_tuple2=(1,2,3,4,5,6)
print("data type of tuple",type(my_tuple))
print("data type of tuple", type(my_tuple1))
print("data type of tuple", type(my_tuple2))

#tuple constructor
new_my_tuple=tuple((my_tuple2))
print("constructor" ,new_my_tuple)

#ACCESS THE TUPLE
my_tuple2=(1,2,3,4,5,6)
print("access the tuple" ,my_tuple2[5])
print("access the tuple" , my_tuple2[-1] , my_tuple2[-2])    #the negative 1 gives last digit and negative 2 gives second last digit
print("Range of the tuple" , my_tuple2[2:4])
print(my_tuple2[:4])
print(my_tuple2[0:])
print("Negative sign from reverse tuple" , my_tuple2[-3:-1])
if 3 in my_tuple2:
    print("yes 3 is in tuple")
#UPDATE THE TUPLE
#update by converting tuple into list


#UNPACK THE TUPLE
table=(2,3,4,5)
(two , three , four ,five)=table
print("two", two)
print("Three",three)
print("four",four)
print("Five",five)

'''#LOOP TUPLE
t1=("apple" , "banana", "mango" ,"cheery" )
for i in t1:
    print("loop",t1[i])

for i in range(len(t1)):
    print("loop",t1[i])
'''
#TUPLE METHODE

'''NOTE: 
list[]---  this is list
tuple()--- this is tuple
dic{}--- this is dictionary'''
#DICTIONARY
dic={"ved": "pannier" , "sakshi":"roti"}
print("dic",dic)
print(dic["ved"])

dic2={"ved":"panner" , "sakshi":"roti" , "papa":{"wanga" , "laal baji", "usal"}, "mummy":{"wanga","laal baji", "manchurian"}}
print("vedant", dic2["ved"])
print("papa" ,dic2["papa"])
print("two at a time",dic2["papa"],dic2["mummy"])

#INSERT IN DICTIONARY
dic2["raj"]="junk"
dic2["balaji"]="veg"
print(dic2)

#CHANGING THE DICTIONARY NAME
dic2["1234"]="junk"
dic2["7658"]="veg"
print(dic2)

#DELETING THE ELEMENT FROM THE DICTIONARY
del dic2["1234"]
print("delete",dic2)

#COPY FUNCTION
dic3=dic2.copy()
print("new", dic3)
del dic3["sakshi"]
print("on deleting from dic3 what happen in dic 2", dic3)
print("dic2" , dic2)

#if we don't use copy fun and differectly do copy

dic3=dic2
del dic3["ved"]
print("without copy function", dic3)
print("without copy function", dic2)

#GET FUNCTION

print("get function", dic2.get("papa"))

#UPDATE FUNCTION
'''dic3.update("leela")
print("updated values", dic3)
'''
#KEYS  represent all the elements/keys of dictionaries
print(dic3.keys())


#ITEMS represents all the iteams
print(dic3.items())




#SETS*****************************************************************************************************8
s=set()
print("type",type(s))

new_set=set([1,2,3,4,5,6])
print("new_set", new_set)
print(type(new_set))
#OR

l=[1.2 ,1.3 ,1.4, 1.6, 1.7]
new_set=set(l)
print("new_set" , new_set)

#ADDING ELEMENTS IN SET
'''NOTE:set only add unique elements in the set that means set never enter 2 times any same value'''

new_set.add(7)
print("add new in set" ,new_set)

new_set.add(8)
new_set.add(8)
print("add new in set" ,new_set)

#UNION OF SET

v1=set([1,2,3])
v2=v1.union({1,2,3,4,5,6})
print("union" ,v1 ,v2)

#INTERSECTION
v1=set([1,2,3])
v2=v1.intersection({1,2,3,4,5,6})
print("Intersection", v1 , v2)

#LENGTH OF SET
print("Length",len(v2))

#MAX VALUE
print(max(v2))

#MIN VALUE
print(min(v2))

#ISDISJOINT FUNCTION

print("Disjoint" , v2.isdisjoint(v1))

#REMOVE VALUE
v2.remove(3)
print("remove",v2)

x=input("enter")