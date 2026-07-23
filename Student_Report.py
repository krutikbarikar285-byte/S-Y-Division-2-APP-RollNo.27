#decorator
def format_report(func):
    def wrapper(self):
        print("*"*30)
        func(self)
        print("*"*30)
        print("\nEnd of Report")
    return wrapper

#constructor
class report:
    
    def __init__(self,author,data,marks,grade):
        self.author=author
        self.data=data
        self.marks=marks
        self.grade=grade
        
    @classmethod
    def student_report(cls):
        return cls("Krutik","23/7/2007",93,"A+")
    
    #magic method
    def __str__(self):
        return(
            "STUDENT REPORT\n\n"
            f"Author:{self.author}\n\n"
            f"Data:{self.data}\n\n"
            f"Marks:{self.marks}\n\n"
            f"Grade:{self.grade}"
        )    
    #Display Report
    @format_report
    def display(self):
        print(self)
        
report=report.student_report()
report.display()            
    
    