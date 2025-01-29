class Rectangle:
    """Represents a rectangle with length and width."""
    
    def __init__(self, length: float, width: float):
        """Initialize a rectangle with length and width."""
        self.length = length
        self.width = width

    def area(self) -> float:
        """Calculate and return the area of the rectangle."""
        return self.length * self.width

    def __str__(self):
        return f"Rectangle(length={self.length}, width={self.width})"


class Square(Rectangle):
    """Represents a square, which is a special type of rectangle with equal sides."""
    
    def __init__(self, side: float):
        """Initialize a square with equal length and width."""
        super().__init__(side, side)

    def __str__(self):
        return f"Square(side={self.length})"


class Cube(Square):
    """Represents a cube, which extends the square by adding volume and surface area calculations."""
    
    def __init__(self, side: float):
        """Initialize a cube with equal side lengths."""
        super().__init__(side)

    def surface_area(self) -> float:
        """Calculate and return the surface area of the cube."""
        return 6 * super().area()  # 6 sides of a square

    def volume(self) -> float:
        """Calculate and return the volume of the cube."""
        return self.length ** 3  # length is the same as width and height

    def __str__(self):
        return f"Cube(side={self.length})"
    

# Base Employee Class
class Employee:
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name
    
    def calculate_payroll(self):
        """This method should be implemented in the subclass."""
        raise NotImplementedError("This method should be overridden in the subclass.")

    def work(self, hours):
        """This method should be implemented in the subclass to track work done."""
        raise NotImplementedError("This method should be overridden in the subclass.")

# SalaryEmployee Class (inherits from Employee)
class SalaryEmployee(Employee):
    def __init__(self, emp_id, name, weekly_salary):
        super().__init__(emp_id, name)
        self.weekly_salary = weekly_salary
    
    def calculate_payroll(self):
        """Returns the weekly salary for salaried employees."""
        return self.weekly_salary
    
    def work(self, hours):
        """Track work for salaried employees. (Work could be symbolic for managers or secretaries)."""
        print(f"{self.name} worked for {hours} hours (Salary-based).")

# Manager Class (inherits from SalaryEmployee)
class Manager(SalaryEmployee):
    def __init__(self, emp_id, name, weekly_salary):
        super().__init__(emp_id, name, weekly_salary)
    
    def work(self, hours):
        """Managers typically work and delegate tasks."""
        print(f"Manager {self.name} worked for {hours} hours, delegating tasks and overseeing operations.")

# Secretary Class (inherits from SalaryEmployee)
class Secretary(SalaryEmployee):
    def __init__(self, emp_id, name, weekly_salary):
        super().__init__(emp_id, name, weekly_salary)
    
    def work(self, hours):
        """Secretaries do the paperwork and ensure everything gets done."""
        print(f"Secretary {self.name} worked for {hours} hours, handling paperwork and administration.")

# SalesPerson Class (inherits from SalaryEmployee)
class SalesPerson(SalaryEmployee):
    def __init__(self, emp_id, name, weekly_salary, commission_rate):
        super().__init__(emp_id, name, weekly_salary)
        self.commission_rate = commission_rate  # Commission rate as a percentage
        self.sales_made = 0  # Track the sales made by the employee

    def work(self, hours, sales_made):
        """SalesPerson works and generates commission from sales."""
        self.sales_made += sales_made
        commission = sales_made * self.commission_rate
        total_pay = self.weekly_salary + commission
        print(f"SalesPerson {self.name} worked for {hours} hours and made ${sales_made} in sales. "
              f"Commission earned: ${commission}. Total Pay: ${total_pay:.2f}")

# HourlyEmployee Class (inherits from Employee)
class HourlyEmployee(Employee):
    def __init__(self, emp_id, name, hourly_rate, hours_worked):
        super().__init__(emp_id, name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
    
    def calculate_payroll(self):
        """Returns the payroll for hourly employees, based on hours worked."""
        return self.hourly_rate * self.hours_worked
    
    def work(self, hours):
        """Factory workers are paid hourly based on how many hours they worked."""
        self.hours_worked += hours
        total_pay = self.calculate_payroll()
        print(f"Factory Worker {self.name} worked for {hours} hours. Total Pay: ${total_pay:.2f}")


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