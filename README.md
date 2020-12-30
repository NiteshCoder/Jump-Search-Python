# Jump-Search-Python
Data structure Searching Algorithm Using Python

Pre-requistic :
			- Data must be sorted.
			

How it works ?

// Sort data
// Search for 50.

step 1 : 
	Find length Of data. 
	//  10 ,20 ,30 ,40 , 50 ,60 ,70 ,80 , 90
	
step 2 :
	Find Squre Root Of length. 
	// length = 9. Sqrt=3.
	
step 3 : 
	Divide data into phase as per square root. 
	// 10 20 30 | 40 50 60 | 70 80 90.

step 4 : Check searched element is less then last element of phase. 
		// Now Jump 10 to 30 ,
			then 40 to 60. 
			Now 50 is less then 60.
			
			
step 5 : Backtracking. Simply go back. You will find your search element. // 50.

step 6 : EXIT.

THANK YOU.
