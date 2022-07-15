from pyparsing import empty, java_style_comment
from traitlets import Instance


class Employee:
    Total_Employee = 0
    anual_raise = 1.04
    def __init__(self,FN,LN, exp,pay):
        self.first_name = FN
        self.last_name = LN
        self.pay = pay
        self.exp = exp
        Employee.Total_Employee +=1


    def anualRaise(self):
        return self.pay * self.anual_raise
    


    @property
    def full_name(self):
        return '{0} {1}'.format(self.first_name,self.last_name)

    @property
    def email(self):
        return'{0}.{1}@company.com'.format(self.first_name,self.last_name)
    
    @email.setter
    def email(self,line):
        FN ,LN = line.split('.',1)
        LN =LN.replace("@company.com", "")
        self.first_name = FN
        self.last_name = LN
    

    @staticmethod
    def work_day(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        else:
            return True

    @classmethod
    def get_employeeNumber(cls):
        return cls.Total_Employee 


    @classmethod
    def set_anualRaise(cls , amount):
     cls.anual_raise = amount


    @classmethod
    def from_string(cls, line):
        FN , LN, pay, exp = line.split('-')
        return  cls(FN, LN, pay,exp)


    
    

    def __len__(self):
        return self.exp

    def __add__(self, other):
        return self.exp + other.exp

    @classmethod
    @property
    def percent_employee(cls):
        return round(cls.Total_Employee/Employee.Total_Employee*100)






    



class Developer(Employee):
    Total_Employee = 0
    anual_raise = 1.10

    def __init__(self, FN , LN, exp,pay, program_lan):
        super().__init__(FN , LN, exp, pay) # or this works too Employee.__init__(self,FN,LN,pay,exp)
        self.pro_lang = program_lan
        Developer.Total_Employee +=1

 
    @classmethod
    def from_string(cls, line):
        FN , LN, exp,pay, program_lan= line.split('-')
        return  cls(FN, LN, int(exp),int(pay), program_lan)


    

    
    



# class Manager(Employee):
#     def __init__(self, FN , LN, exp,pay, emp = None):
#         super().__init__(FN,LN,exp,pay)
#         if emp is None:
#             self.emp = []
#         else:
#             self.emp = emp
    
#     def add_employee(self, employee):
#         if employee not in self.emp:
#             self.emp.append(employee)
    
#     def remove_employee(self, employee):
#         if employee in self.emp:
#             self.emp.remove(employee)
#     @property

#     def show_employee(self):
#         for employee in self.emp:
#             print("->" ,employee.full_name)




        






Emp1 = Employee("MD" , "Khan", 2, 200000)  
Dev1 = Developer("Md" , "green", 4,400000 ,"C++")
mg1 = Manager("TOM", "Holland", 10,3500000, [Dev1])



mg1.add_employee(Emp1)
mg1.remove_employee(Emp1)
print(mg1.show_employee)




# some helpful functions 
# print(class.__dict__) this show you all the variable of a class or a self aka Instance
# print(help(class)) this gives information about a class and it metord of resolution aka it inheritaner
# isinstance(dev1 , Developer) check if there is a var is an isatance of a class
# issubclass(Manager , Employee) check if the class is the subclass of a class






# line = "Jim-tom-3-500000-java"

# Dev2 =Developer.from_string(line)
# Dev2.email = "Tom.jimmy@company.com" 
# print(Dev2.email)
# print(Dev2.last_name)
# print(Dev2.pro_lang)
# print(len(Dev2))
# print(Dev2.percent_employee)


# # print(Emp1.email)
# # print(Dev1.email)
# # print(Dev1.pro_lang)
# # print(len(Dev1))
# # print(Dev1.percent_employee)


print(Developer.Total_Employee)
print(Employee.Total_Employee)


def sum(num , *number):

    f = num
    for numb in number:
        f  = numb + f

    return f 


def sum(**number):

    f = 0
    for key, value in number.items():
        f  = value + f

    return f 





# note: you see we can are not using dictionary or list. we using unique keys and it value for unlimited amount of time
g = sum( s1 = 1, s2 = 2, s3 = 3, s4 = 4) 
print(g)
