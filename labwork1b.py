
def studentcount(): #student count
    n = int(input("enter student number: "))
    return n





def coursecount():
    k = int(input("enter course number: "))
    return k


def studentadd(n):

    #students
    print ("\nstudent info\n")

    students = []
    for i in range (n):
        id = (input("enter id of student: "))
        name = str(input("name: "))
        dob = str(input("dob: "))
        student = {
            "id": id,
            "name": name,
            "dob": dob,
            "grades": {}
        }
        students.append(student)
    return students




def courseadd(k):


    courses = []


    for i in range (k):
        cid = int(input("enter id of course: "))
        cname = str(input("name: "))
        course = {
            "id": cid,
            "name": cname
        }

        courses.append(course)
    return courses

def grading(k, students, courses, n):

    gname = str(input("enter course name to grade (type done if out): "))

    if gname == "done":
        return

    for i in range(k):
        if courses[i]["name"] == gname:
            break
    else:
        print("unavailable")
        return grading(k, students, courses, n)

    for m in range (n):
        grade = float(input("enter grades for " + students[m]["name"] + ": " ))

        students[m]["grades"][gname] = grade


    return grading(k, students, courses, n)

      
    
def grlist(students, n, courses, k):
    find = input("enter course name to view grades (type done if out): ")

    if find == "done":
        return
    
    i = 0
    for i in range (k):
        if courses[i]["name"] == find:
            break
    else:
        print("unavailable")
        return grlist(students, n, courses, k)

    print ("\n=grades for", find, "=\n")

 #listing 
    for i in range (n):
        print (students[i]["name"], ":", students[i]["grades"][find])
    return grlist(students, n, courses, k)


def stulist(n, students):
    print("\n--student list--\n")
    for i in range (n):
        print(i+1, ":", students[i])

    print("")
    return



def clist(k, courses):
    print("\n--course list--\n")
    for i in range (k):
        print(i+1, ":", courses[i])

    print("")
    return


n = studentcount()
students = studentadd(n)
stulist(n, students)
k = coursecount()
courses = courseadd(k)
clist(k, courses)
grading(k, students, courses, n)
grlist(students, n, courses, k)