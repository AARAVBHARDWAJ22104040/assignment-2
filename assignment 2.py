# assignment 2
# question 1
input = "Python is a case sensitive language"

print("Length of the input string is",len(input))

Reverse_order = input[35::-1]
print( "the reverse order is'", Reverse_order ,"'")

phrase = input[10:26]
print('''the sliced string is "''', phrase,'''"''')

New_input = input.replace("a case sensitive","object oriented")
print('''Updated string is "''',New_input,'''"''')

index_of_a = input.find("a")
print("The index of 'a' is",index_of_a)

updated_input = input.replace(" ","")
print("The new string is '",updated_input,"'")



#question 2
name="Siddharth Srivastava"
sid=22104095
dept="Electrical Engineering"
cg=9.9
print(" Hey,",name,"Here!\n","My SID is",sid,"\n","I am from",dept,"department and my CGPA is",cg)



#question 3
a = 56
b = 10
print("the value of a&b is",a&b)
print("the value of a|b is",a|b)
print(" the value of a^b is",a^b)
print("a<<2 =",a<<2,"b<<2 =",b<<2)
print("a>>2 =",a>>2,"b>>4 =",b>>4)



#question 4
a = input("Enter a number here")
b = input("Enter a number here")
c = input("Enter a number here")

Listofthreenumbers = [a,b,c]
greatest_number = max(Listofthreenumbers)

print("The Greatest of three number is ",greatest_number)



#question 5
statement = input("Enter any statement here")
if 'name' in statement :
    print("Yes")
else :
    print("No")



#question 6
Length_1 = input("enter any Length here")
Length_2 = input("enter any Length here")
Length_3 = input("enter any Length here")

Length_1 =int(Length_1)
Length_2 =int(Length_2)
Length_3 =int(Length_3)

if 'Length_1 + Length_2 > Length_3' and 'Length_2 + Length_3 > Length_1' and 'Length_1 + Length_3 > Length_2' :
    print("Yes")
else :
    print("No")