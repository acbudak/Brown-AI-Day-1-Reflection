class Student:
    def __init__(self, name, age, courses):
            self.name = name
            self.age = age
            self.courses = courses
           

    def myfunc(self):
            return("My name is"+self.name + "I am"+ self.name +"I take"+self.courses)

            
p1 = Student("Can",16, "Math")
var= p1.myfunc()
print(var)

p2 = Student ("Berna", 17, "Biology")
var= p2.myfunc()
print(var)


class course:
    def __init__(sch, teachers,no):
             sch.teachers = teachers
             sch.no = no
    def myfuncion(sch):
                return("Your teacher is", sch.teachers ,"There are", sch.no ,"students are in the course")

s1 = course("JDD",23)
var = s1.myfuncion()
print(var)
s2 = course("Miafushi", 15)
var = s2.myfuncion()
print(var)

