#Building_dev 
#Assingments


num = int(input("Enter a number:  "))



def asmt_1():
	print("\nAssignment 1\n")
	for i in range(num):
		print(" "*((num-i)//2) +"*"*(i+1))
	return ""		
print(asmt_1())
	
def asmt_2():
	print("".center(50,"_"))
	print("\nAssignment 2\n")
	for i in range(num):
			print("*"*(i+1))
	print()
	return ""		
print(asmt_2())

def asmt_3():
	print("".center(50,"_"))
	print("\nAssignment 3\n")
	#rows
	for i in range(num):
		#1st square
		#colums
		for j in range(num):
			#anti diagonal
			if j+i ==num-1:
				print("*",end= " ")
			else:
				print(" ", end= " ")
		#2nd square		
		for j in range(i):# rm j=0 column		
			if j==i-1:#new diagonal 
				print("*",end=" ")
			else:
				print(" ",end=" ")
		print()
	return ""	
print(asmt_3())

def asmt_4():
	print("".center(50,"_"))
	print("\nAssignment 4\n")
	for i in range(num):
		for j in range(num):
			if j+i==num-1:
				print("*",end=" ")		
			elif j==num-1:
				print(i,end=" ")
			else:
				print(" ",end=" ")
		for j in range(i): 
			if j==i-1:
				print("*",end=" ")
			else:
				print(" ",end=" ")
		print()
	return ""			
print(asmt_4())

def asmt_5():
	print("".center(50,"_"))
	print("\nAssignment 5\n")
	for i in range(num):
		for j in range(num):
			if j+i==num-1:
				print("*",end=" ")		
			elif j==num-1:
				print(((num+1)-i),end=" ")
			else:
				print(" ",end=" ")

		for j in range(i): 
			if j==i-1:
				print("*",end=" ")
			else:
				print(" ",end=" ")
		print()
    #runs the nxt iteration of main for loop on the next line
	return ""
print(asmt_5())
