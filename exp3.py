
class Employee:
    def __init__ (
            self,
            designation : str = 'Developer',
            frontend : bool = True,
            backend : bool = True
    ):
        self.designation = designation
        self.frontend = frontend
        self.backend = backend

    def __repr__ (self):
        return '{}'.format (self.designation, self.frontend, self.backend)
    
    ### Write the your method over here.
    def verifier (self):
       if self.frontend:
           self.designation="frontend developer"
       if self.backend:
           self.designation="backend developer" 
       if self.backend and self.backend:
           self.designation="fullstack developer"  

if __name__ == '__main__':
    firstEmployee = Employee ()
    firstEmployee.verifier()
    print(firstEmployee)
    # Call the method here to display output.    