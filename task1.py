#Example 1.
import logging
logging.basicConfig(filename = "OOPs_Tasks_Logging.log",level = logging.INFO , format = '%(asctime)s:%(levelname)s:%(message)s')

class ineuron_classes:
    def __init__(self, subject, instructor, mode):
        self.subject = subject
        self._instructor = instructor
        self.__mode = mode
    def course(self):
        print("We all are FSDS Students")

class ineuron_instructors(ineuron_classes):
    pass

try:
    logging.info("Assigning the Values to class constructor")
    PC = ineuron_instructors("Python", "Sudhanshu Sir", "Online")
    ML = ineuron_instructors("Machine Learning", "Krish Sir", "Online")
    s = PC.course()
    logging.info("check the logging test %s", s)
    logging.info(PC.course())
    print(PC.subject)
    print(PC._instructor)   # Printing the private variable.
    print(PC._ineuron_classes__mode)  #printing protected variable.
    print(ML.subject)
    print(ML._instructor)
    print(ML._ineuron_classes__mode)
except Exception as e:
    logging.exception(e)


#Example 2.

class classmode:
    def PythonclassMode_(self):
        print("Python class mode is online.")
    def ML_Classmode_(self):
        print("Machine Learning class mode is online.")

class classtimings:
    def Python_classtimings_(self):
        print("Python Class timings is 3-4 months")
    def ML_classtimings_(self):
        print("Machine Learning Class timings is 2 months")

class ineuron_class_details(classmode, classtimings):
    pass

ct = ineuron_class_details()

ct.Python_classtimings_()
ct.ML_classtimings_()
ct.ML_Classmode_()
ct.ML_Classmode_()

#Example:3

class classmode:
    __Python = "4 months"
    _ML = "2 Months"

    def IN_classtimings(self):
        print("class timings for selected course is", classmode.__PythonclassMode)

cm = classmode()
print("Python Class timings", cm._classmode__Python)
print("ML Class timings", classmode._ML)

#Example 2.
class classmode1:
    __Python = "4 months"
    _ML = "2 Months"
    def classtimechange(self):
        self.__Python = "2 months"

cm = classmode1()
print("Python Class timings", cm._classmode1__Python)
print("ML Class timings", classmode1._ML)
cm.classtimechange()
print("Print Updated Python Class timings")
print("Python Class timings", cm._classmode1__Python)


#Example 2.
class classmode1:
    __Python = "4 months"
    _ML = "2 Months"
    def classtimechange(self):
        self.__Python = "2 months"
    def classtimechange1(self, new_value):
        self._ML = new_value

cm = classmode1()
print("Python Class timings", cm._classmode1__Python)
print("ML Class timings", cm._ML)
cm.classtimechange()
print("Print Updated Python Class timings")
print("Python Class timings", cm._classmode1__Python)
cm.classtimechange1("One month")
print("Machine Learning class timings after change : -- ", cm._ML)

#Polymorphism  Example:

class Python_Class:
    def intro(self):
        print("Python Class duration is 3-4 months")

    def ML_Class(self):
        print("ML Class duration is 2 months")

class SS(Python_Class):
    def instctr(self):
        print("Python by Sudhanshu_Sir")

class KS(Python_Class):
    def instctr(self):
        print("ML Class by Krish Sir")


obj_Python_Class = Python_Class()
obj_SS = SS()
obj_KS = KS()

obj_Python_Class.intro()
obj_Python_Class.ML_Class()

obj_SS.intro()
obj_SS.instctr()

obj_KS.intro()
obj_KS.instctr()









