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