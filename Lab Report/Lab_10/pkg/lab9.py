
class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

#-------------

class Salary_employee(Employee):
    def __init__(self, id, name, weekly_salary):
        super().__init__(id, name)
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary

#-------------

class Hourly_employee(Employee):
    def __init__(self, id, name, hours_worked, hourly_rate):
        super().__init__(id, name)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_payroll(self):
        return self.hours_worked * self.hourly_rate

#-------------

class Commission_employee(Salary_employee):
    def __init__(self, id, name, weekly_salary, commission):
        super().__init__(id, name, weekly_salary)
        self.commission = commission

    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return fixed + self.commission

#-------------

class Manager(Salary_employee):
    def work(self, hours):
        print(f"{self.name} oversees and delegates tasks for {hours} hours.")

#-------------

class Secretary(Salary_employee):
    def work(self, hours):
        print(f"{self.name} efficiently organizes and manages documents for {hours} hours.")

#-------------

class SalesPerson(Commission_employee):
    def work(self, hours):
        print(f"{self.name} engages with clients and closes deals for {hours} hours.")

#-------------

class FactoryWorker(Hourly_employee):
    def work(self, hours):
        print(f"{self.name} diligently assembles products for {hours} hours.")

#-------------

class Productivity_system:
    def Track(self, employees, hours):
        print("Productivity System Tracking")
        print('-----------------------------')
        for employee in employees:
            employee.work(hours)
            print()



class Rectangle:
    def __init__(self, length, width, **kwargs):
        self.length = length
        self.width = width
        super().__init__(**kwargs)

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

#----------------

class Square(Rectangle):
    def __init__(self, length, **kwargs):
        super().__init__(length=length, width=length, **kwargs)

#----------------

class Triangle:
    def __init__(self, base, height, **kwargs):
        self.base = base
        self.height = height
        super().__init__(**kwargs)

    def tri_area(self):
        return 0.5 * self.base * self.height

#----------------

class RightPyramid(Square, Triangle):
    def __init__(self, base, slant_height, **kwargs):
        self.base = base
        self.slant_height = slant_height
        kwargs["height"] = slant_height
        kwargs["length"] = base
        super().__init__(base=base, **kwargs)

    def area(self):
        base_area = super().area()
        perimeter = super().perimeter()
        return 0.5 * perimeter * self.slant_height + base_area

    def area_2(self):
        base_area = super().area()
        triangle_area = super().tri_area()
        return triangle_area * 4 + base_area

#----------------

class SurfaceAreaMixin:
    def surface_area(self):
        surface_area = 0
        for surface in self.surfaces:
            surface_area += surface.area(self)

        return surface_area

#----------------

class Cube(Square, SurfaceAreaMixin):
    def __init__(self, length):
        super().__init__(length)
        self.surfaces = [Square, Square, Square, Square, Square, Square]

#----------------

class RightPyramid(Square, Triangle, SurfaceAreaMixin):
    def __init__(self, base, slant_height):
        self.base = base
        self.slant_height = slant_height
        self.height = slant_height
        self.length = base
        self.width = base

        self.surfaces = [Square, Triangle, Triangle, Triangle, Triangle]



class EEDJ_Employee:
    def __init__(self, id, name, position, workload, scale, b_pay):
        self.id = id
        self.name = name 
        self.position = position 
        self.workload = workload 
        self.scale = scale
        self.b_pay = b_pay

    def __str__(self):
        return f"Employee ID: {self.id}, Name: {self.name}, Position: {self.position}, Workload: {self.workload}-Hours, Scale: {self.scale}, Base Pay: {self.b_pay}"

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

class Faculty(EEDJ_Employee):
    def __init__(self, id, name, position, workload, scale, b_pay, research, subject, experiance, teach_mode):
        super().__init__(id, name, position, workload, scale, b_pay)
        self.research = research
        self.subject = subject
        self.experiance = experiance
        self.teach_mode = teach_mode

    def __str__(self):
        return super().__str__() + f", Research: {self.research}, Subject: {self.subject}, Experience: {self.experiance} years, Teach Mode: {self.teach_mode}"

class Professor(Faculty):
    def __init__(self, id, name, position, workload, scale, b_pay, research, subject, experiance, teach_mode):
        super().__init__(id, name, position, workload, scale, b_pay, research, subject, experiance, teach_mode)
    
    def __str__(self):
        return super().__str__()

class Associate_Prof(Faculty):
    def __init__(self, id, name, position, workload, scale, b_pay, research, subject, experiance, teach_mode):
        super().__init__(id, name, position, workload, scale, b_pay, research, subject, experiance, teach_mode)
    
    def __str__(self):
        return super().__str__()

class Assistant_Prof(Faculty):
    def __init__(self, id, name, position, workload, scale, b_pay, research, subject, experiance, teach_mode):
        super().__init__(id, name, position, workload, scale, b_pay, research, subject, experiance, teach_mode)
    
    def __str__(self):
        return super().__str__()

class Lecturer(Faculty):
    def __init__(self, id, name, position, workload, scale, b_pay, research, subject, experiance, teach_mode):
        super().__init__(id, name, position, workload, scale, b_pay, research, subject, experiance, teach_mode)
    
    def __str__(self):
        return super().__str__()
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------

class Admin(EEDJ_Employee):
    def __init__(self, id, name, position, workload, scale, b_pay, lab_name="", lab_capacity=0):
        super().__init__(id, name, position, workload, scale, b_pay)
        self.lab_name = lab_name
        self.lab_capacity = lab_capacity

    def __str__(self):
        return super().__str__() + f", Lab Name: {self.lab_name}, Lab Capacity: {self.lab_capacity}"

class Lab_Engr(Admin):
    def __init__(self, id, name, position, workload, scale, b_pay, lab_name, lab_capacity,lab_subject):
        super().__init__(id, name, position, workload, scale, b_pay, lab_name, lab_capacity)
        self.lab_subject = lab_subject
    
    def __str__(self):
        return super().__str__() + f", Lab Subject: {self.lab_subject}"

class Lab_Technician(Admin):
    def __init__(self, id, name, position, workload, scale, b_pay, lab_name, lab_capacity,basic_lab):
        super().__init__(id, name, position, workload, scale, b_pay, lab_name, lab_capacity)
        self.basic_lab = basic_lab
        
    def __str__(self):
        return super().__str__() + f", Basic Lab : {self.basic_lab}"

class Lab_Assistant(Admin):
    def __init__(self, id, name, position, workload, scale, b_pay, lab_name, lab_capacity,equipment_handle):
        super().__init__(id, name, position, workload, scale, b_pay, lab_name, lab_capacity)
        self.equipment_handle = equipment_handle

    def __str__(self):
        return super().__str__() + f", Equipment Handle: {self.equipment_handle}"

class Lab_Attendant(Admin):
    def __init__(self, id, name, position, workload, scale, b_pay, lab_name, lab_capacity):
        super().__init__(id, name, position, workload, scale, b_pay, lab_name, lab_capacity)

    def __str__(self):
        return super().__str__()
    
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------