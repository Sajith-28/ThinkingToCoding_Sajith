print("Enter Marks of 5 students:\n")
marks=[]
m1=float(input("Enter mark of student 1:"))
m2=float(input("Enter mark of student 2:"))
m3=float(input("Enter mark of student 3:"))
m4=float(input("Enter mark of student 4:"))
m5=float(input("Enter mark of student 5:"))
marks=[m1,m2,m3,m4,m5]
average=sum(marks)/len(marks)
print("Average Mark=",average)
print("\nStudent with marks above average:\n")
if m1>average:
    print("Student 1:",m1)
if m2>average:
    print("Student 2:",m2)
if m3>average:
    print("Student 3:",m3)
if m4>average:
    print("Student 4:",m4)
if m5>average:
    print("Student 5:",m5)