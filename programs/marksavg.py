sub1=input("Enter the marks of the first subject is:")
sub2=int(input("Enter the marks of the secound subject is:"))
sub3=int(input("Enter the marks of the third subject is:"))
sub4=int(input("Enter the marks of the fourth subject is:"))
sub5=int(input("Enter the marks of the fifth subject is:"))

avg=(sub1+sub2+sub3+sub4+sub5)/5

if(avg>=90):
	print("Grade A")
elif(avg>80 & avg<70):
	print("Grade B")
elif(avg>70 & avg<60):
	print("Grade C")
elif(avg>60 & avg<50):
	print("Grade D")
else:
	print("Grade: F")	
