
name = input("Enter Your name: ")
marks =int (input("Enter youe marks: "))

def calculate_grade(name, marks):
    if marks <= 100:
        if marks >= 90:
            print(f"hi {name} our grade is A")
        elif marks >= 80:
            print("your grade is B")
        elif marks>= 70:
            print("youe grade is C")
        elif marks>= 60:
            print("youe grade is D") 
        elif marks< 60:
            print("Try again!")
        else:
            print("Invalid Name")
    else:
        print("invalid marks")
  
calculate_grade(name, marks)