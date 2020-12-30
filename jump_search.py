#Searching Algorithm
#Jump Search.

'''
Pre-requistic :
			- Data must be sorted.
			

How it works ?

// Sort data
// Search for 50.

step 1 : Find length Of data. //  10 ,20 ,30 ,40 , 50 ,60 ,70 ,80 , 90 
step 2 : Find Squre Root Of length. // length = 9. Sqrt=3.
step 3 : Divide data into phase as per square root. // 10 20 30 | 40 50 60 | 70 80 90.
step 4 : Check searched element is less then last element of phase. 
		// Now Jump 10 to 30 ,
			then 40 to 60. 
			Now 50 is less then 60.
step 5 : Backtracking. Simply go back. You will find your search element. // 50.
step 6 : EXIT.
'''

import math

#For Sorting data using python default function.
def sort_data(data):
	data.sort()


#Actual Logic of Jump search	
def jump_search(data,search):
	if search in data:
		index = 0 #Variable for store searching element Index.
		length = len(data) 
		sqrt_length = int(math.sqrt(length))
	
		#Loop for making blocks as per sqrt_lenght.
		for i in range(sqrt_length-1,length,sqrt_length):
			print(data[i],end=" ")
		
			#If last element is greater then Start backtracking.
			if data[i] >= search:
				print("Yes , You are on right steps.")
			
				#Actual backtracking start from here.Using While Loop
				while(data[i] != search):
					#print("Inner if called")
					index = i
					#print("\n",data[i])
					i= i -1
				#While with else for if last element of block searched.
				else:
					#print("While else Called")
					index = i
			else:
				continue;
		
			return i;	
	else:
		#print("\n-------------------------------\nSearched data not Exists in Data.");
		return -1;
	
if __name__ == "__main__":
	data = []
	size = int(input("How many elements you want to enter ? : "))
	print("\n--------------INITIALIZING-----------------")
	for i in range(size):
		temp = int(input(f"Enter element { i+1 } : "))
		data.append(temp)
	
	search = int(input(f"\nEnter element for search : "))
	sort_data(data)
	print(f"\nElements are : {data}")
	print("\n--------------Caling Jump Search function--------------")
	answer = jump_search(data,search)
	
	if answer==-1:
		print("\n-------------------------------\nSearched data not Exists in Data.");
	else:
		print(f"\nSERCHED ELEMENT : { data[answer] }\nINDEX OF SEARCHED ELEMENT : { answer }")
	
	
	
