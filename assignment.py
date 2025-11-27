marks=int(input("marks of the student(0-100) : "))
if marks>100:
    print("The marks entered by the User is Invalid, plz enter the marks in between (0-100) ")
elif marks>=90:
    print("The grade of the student is A")
elif marks>=75:
    print ("The grade of the student is B")
elif marks>=60:
    print ("The grade of the student is C")
elif marks>=40:
    print("The grade of the Student is D")
elif marks<=39:
    print("The grade of the student is Fail")

           