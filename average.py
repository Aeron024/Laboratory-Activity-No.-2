print("Your Average Grade")
pre=int(input("Enter Prelim:  "))
mid=int(input("Enter Midterm:  "))
sem=int(input("Enter SemiFinal:  "))
fin=int(input("Enter Final:  "))

tots= pre+mid+sem+fin
ave=tots/4

print("The Average is ",ave)
if ave >= 75:
	print("You Passed!")
else:
	print("You Failed!")

if ave >=99 <=100:
	print("Your Grade is A")
elif ave >=90 <=99:
	print("Your Grade is B")
elif ave >=80 <=89:
	print("Your Grade is C")
elif ave >=71 <=79:
	print("Your Grade is D")
elif ave >=61 <=70:
	print("Your Grade is E")
elif ave >=60:
	print("Your Grade is F")
else:
	print("Invalid Input")