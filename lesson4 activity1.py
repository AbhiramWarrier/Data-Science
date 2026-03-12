import matplotlib as plt
students_names=["snajay","Rahul","karan","wasim","ramesh", "ajay","sartaj","priya"]

student_marks = [35, 50,20,45,25,40,25,40]

marks_perc = []
for x in student_marks:
    res =(x/50)*100
    marks_perc.append(res)

print(marks_perc)    

def marks_line_chart():
    plt.plot(students_names,student_marks)
    plt.title("Students Marks Graph")
    plt.xlabel("Students names")
    plt.ylabel("Students marks")
    plt.show()

    marks_line_chart()

    def percentage_bar_chart():
        plt.bar(students_names,marks_perc)
        plt.xlabel("Students Names")
        plt.ylabel("Student Percentage")
        plt.show()

        percentage_bar_chart()