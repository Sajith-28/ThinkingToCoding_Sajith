# The Data Thinker – The Average Student
## Logic Summary:
The main goal of this program is to collect the marks of 5 students, find their average score, and print which students scored above the average.
The program takes marks one by one from the user, stores them inside a list, calculates the total and then the average using Python’s sum() and len() functions.
Finally, it checks each student’s mark using simple if conditions to see who scored higher than the average and prints their marks.
This logic helps understand how to handle multiple data values, perform basic calculations, and apply decision-making in a sequential way.


## Python Code:
```Python
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
```

## Code Summary:
The program starts by asking the user to enter marks for 5 students.
Each mark is stored in separate variables (m1 to m5).
All the marks are then grouped together inside a list named marks.
The average is calculated using the formula:
```
average = sum(marks) / len(marks)
```
After finding the average, the program uses if statements to check which students scored more than the average. 
It then prints the names and marks of those students who scored above average.

## What I Learned:
From this task, I learned how to use lists in Python to store multiple values and process them easily.
I understood how to calculate the average using built-in functions like sum() and len().
This activity also showed the importance of using loops to go through list elements one by one.
Overall, I learned how data can be stored, processed, and analyzed logically.

## Execution Screenshot:
<img width="386" height="344" alt="image" src="https://github.com/user-attachments/assets/836fdb9a-457c-4f8c-bd59-160b4b2a3078" />
