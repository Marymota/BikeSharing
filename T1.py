class Vehicle():                          


    VNAME_LIST = []
    VEHICLES_LIST = []

# Initiator of objects 
    def __init__(self, name, model, electric, price):                               
        self.set_vname(name)                                 
        self.model = model                            
        self.set_electric(electric)                                                
        self.price = price

#       Vehicle.VNAME_LIST.append(self.name)
    def add_vehicle(self, newobj):                             
        self.set_vname(newobj.name)                                 
        self.model = newobj.model                            
        self.set_electric(newobj.electric)                                                
        self.price = newobj.price
        Vehicle.VEHICLES_LIST.append((self.name, self.model, self.electric, self.price))

## Getters
# Consult any individual attributes
    def get_vname(self):                                
        print(f"{self.name}") 

    def get_model(self):                                
        print(f"{self.model}")  

    def get_type(self):                                
        print(f"{self.electric}")    

    @staticmethod    
    def get_price(vname):
        for vehicle in Vehicle.VEHICLES_LIST:
            if vname == vehicle[0]:
                return vehicle[3]                            
 
 

##Setters 
# Ensure that names will not repeat
    def set_vname(self, name):
        if (name in Vehicle.VNAME_LIST):
            print("Invalid name. Try other.")
        else:
            self.name = name 

    def set_vehicle(self):       
        Vehicle.VEHICLES_LIST.append((self.name, self.model, self.electric, self.price))
        Vehicle.VNAME_LIST.append(self.name)


    def set_model(self, model):
        print("The vehicle model can't be altered.")
        
# Ensure that the the method "electric" only accepts 'yes' or 'no' as answers 
    def set_electric(self, electric):
        self.electric = bool(electric)

# Alter the base price of the vehicle
    def set_price(self, price):                                                 
        self.price = price                              

# Display details 
    def print_details(self):
        print(f"Name: {self.name}\nModel: {self.model}\nElectric: {self.electric}\nPrice: {self.price}€")                            

# Compare vehicles by type and price                                                                                                                                   
    def __eq__(self, other):
        if self.electric == other.electric and self.price == other.price:
            print("Same value")
            return True  
        else:
            print("Different value")                
            return False




#   Created Objects    
#shiva = Vehicle("Shiva", "cat", True, 15)
#mizuki = Vehicle("Mizuki", "cat", True, 20)
#tobias = Vehicle("Tobias", "bird", True, 10)
#print(Vehicle.VEHICLES_LIST)

##### TESTS #####
#compare = shiva == mizuki
#shiva.get_price()
#mizuki.get_price()
#print(compare)
#mizuki.get_type()
#shiva.save_vehicle()
#mizuki.print_details()
#shiva.print_details()
#shiva.__eq__(mizuki)
#shiva.set_price(20)
#shiva.print_details()
#shiva.__eq__(mizuki)
#mizuki.set_model("kurt")



#Object Class User
class User():
    
    NICKNAME_LIST = []
    UNAME_LIST = []
#prevent password read access
#   def password(self):
#      return self.password

    def __init__(self, nickname, password, name, mail, course, budget=0):         
        self.nickname = nickname                                                   
        self.password = password                                                
        self.name = name
        self.mail = mail                                                        
        self.course = course
        self.budget = budget                                                    
#       User.NICKNAME_LIST.append(nickname)
#    def save_user(self):
#        self.users.append(self)

# Consult any individual attributes
    def get_nickname(self):                                
        return self.nickname

    def get_password(self):                                
        return self.password

    def get_name(self):                                
        return self.name

    def get_mail(self):                                
        return self.mail

    def get_price(self):                                
        return self.course  
    
    def get_budget(self):                             
        return self.budget   

# Test password
    def __eq__(self, other):
        if(isinstance(other, User)):
            return self.password == other.password
        return False

# alter email and course

    def set_nickname(self, nickname):
        self.nickname = nickname

    def set_password(self, password):
        self.password = password

    def set_email(self):
        mail = input("E-email: ")
        self.mail = mail
        print("Your e-mail was successfully changed")

    def set_course(self, course):
        course = input("Course: ")
        self.course = course
        print("Your course was successfully changed")

# Change password giving the old one first
    def password_change(self):                                                  
        password = input("Old password: ")
        if password == self.password:
            password = input("New password: ")                                  
            self.password = password
            print("Your password was successfully changed")
        else:
            self.password_change()

# show details
    def print_details(self):
        print(f"Nickname: {self.nickname}\nName: {self.name}\nE-mail: {self.mail}\nCourse: {self.course}\nBudget: {self.budget}")
    
# Created Users
#marcia = User("marmota", "C10u6!", "Márcia", "marventrian@hotmail.com", "42", 5)   
#sergio = User("elTzimmy", "Kubos", "Sérgio", "sergio@hotmail.com", "home-studies")   

#TESTS
#marcia.print_details()
#marcia.password_change()
#marcia.password_change()
#marcia.set_email()
#marcia.save_user() 
#marcia.get_password()
#sergio.print_details()
#users = [marcia,sergio]
#print(users[1]._name,users[0]._name)
#users[0].print_details()


### List of stuff to do ###                                                                               
##### T1 VEHICLE & USER Object Classes #####

# Object Class Vehicle                          >>> \/   
# unique identifier                             >>> \/         
# only "yes" or "no"                            >>> \/
# consult attributes individualy                >>> \/    
# altering price                                >>> \/
# print details on screen                       >>> \/   
# compare vehicles                              >>> \/   

# Object Class User                             >>> \/
# Budget is optional                            >>> \/
# Budget defaults to 0 if not indicated         >>> \/       
# consult attributes individualy                >>> \/          
# except password                               >>> \/                      
# Test if user has correct password             >>> \/    
# Alter email and course                        >>> \/     
# alter password after confirming the old one   >>> \/
# print details on screen                       >>> \/