
def studentcount(): #student count
    n = int(input("enter student number: "))
    print ("number of students is: ", n)
    return n





def coursecount():
    k = int(input("enter course number: "))
    print ("number of course is: ", k)
    return k




def studentadd():

    #students
    n = studentcount()

    print ("student info\n")

    students = []
    for i in range (n):
        id = int(input("enter id of student: "))
        name = str(input("name: "))
        dob = str(input("dob: "))
        student = {
            "id": id,
            "name": name,
            "dob": dob,
        }
        students.append(student)
    print (students)
    return students




def courseadd():


    courses = []
    k = coursecount()


    for i in range (k):
        cid = int(input("enter id of course: "))
        cname = str(input("name: "))
        course = {
            "id": cid,
            "name": cname
        }

        courses.append(course)
    print (courses)
    return courses

def grading():

    gname = str(input("enter course name to grade: "))
    k = coursecount()
    courses = courseadd()
    n = studentcount()

    grades = []

    for i in range(k):
        if courses[i]["name"] == gname:
            break
    else:
        print("unavailable")
        return

    for m in range (n):
      stgrade = float(input("enter grades: "))

      grades.append(stgrade)
    print("grades:", grades)
    return





