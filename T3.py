from T1 import Vehicle
from T1 import User
from T2 import Rent

###################### ----- VEHICLE MANAGEMENT ---- #######################

class Manager():

    USER_LIST = []
#1. Verify if a vehicle with X name exists.
    def exists_vehicle(self, vname):
        if vname in Vehicle.VNAME_LIST:
            print("This vehicle already exists")
#        print(f"{vname} is not listed")

        
#2. Get the vehicle price by its name
    def get_price(self, vname):
        for vehicle in Vehicle.VEHICLES_LIST:
            if vehicle[0] == vname:
                print(f"{vehicle[3]}€")
            else:
                print("This vehicle does not exists")

#3. Add a new vehicle verifying if the choosen name is not already in use to avoid duplicates
    def add_vehicle(self, newobj):                             
        self.set_vehicle_name(newobj.name)                                 
        self.model = newobj.model                            
        self.set_electric(newobj.electric)                                                
        self.price = newobj.price
#        print(Vehicle.VNAME_LIST)
        Vehicle.VEHICLES_LIST.append((self.vname, self.model, self.electric, self.price))

#4. List existent vehicles and their correspondent details 
    def list_vehicles(self):
        for vehicle in Vehicle.VEHICLES_LIST:
            print(vehicle)

### SETTERS
    def set_vehicle_name(self, vname):
        if not(vname in Vehicle.VNAME_LIST):
            self.vname = vname 
            Vehicle.VNAME_LIST.append(vname)
        else:
            print(f"{vname} is not a valid name. Try other.")            

    def set_electric(self, electric):
        self.electric = bool(electric)

    

###################### ----- USER MANAGEMENT ---- #######################

#1. Verify if User with X nickname exists.
    def exists_user(self, nickname):
        if nickname in User.NICKNAME_LIST:
            print("Invalid nickname. Try other.")

#2. Add a new vehicle verifying if the choosen nickname is not already in use to avoid duplicates
    def add_user(self, newUser):
        self.nickname = newUser.nickname
        self.password = newUser.password
        self.name = newUser.name
        self.mail = newUser.mail                                                        
        self.course = newUser.course
        self.budget = newUser.budget                                 
        Manager.USER_LIST.append((self.nickname, self.password, self.name, self.mail, self. course, self.budget))

#3. List existent users and their correspondent details 
    @staticmethod
    def list_users():
        for user in Manager.USER_LIST:
            print(f"Nickname: {user[0]}\nPassword: {user[1]}\nName: {user[2]}\nE-mail: {user[3]}\nCourse: {user[4]}\nBudget: {user[5]}")
            print("---")

#4. Add budget to a specific User. This method recieves two parameters, the user nickname and the budget to be added.
    @staticmethod
    def add_budget(nickname, plus):
        for user in Manager.USER_LIST:
            if nickname in user:
                i = Manager.USER_LIST.index(user)
                user = list(Manager.USER_LIST[i])
                total = float(user[5]) + float(plus)
                user[5] += float(plus)
                Manager.USER_LIST[i] = tuple(user)
                print(f"{plus}€ was added to '{nickname}' budget. '{nickname}' has now a total of {total}€")

#5. Alter password of X user by its nickname
    @staticmethod
    def password_change(nickname):
        for user in Manager.USER_LIST:
            if nickname in user:
                i = Manager.USER_LIST.index(user)
                user = list(Manager.USER_LIST[i])
                user[2] = input("New password: ")
                Manager.USER_LIST[i] = tuple(user)                       

###################### ----- RENT MANAGEMENT ---- #######################

    @staticmethod
    def start_rental(nickname, vname):
        price = Vehicle.get_price(vname)
        Rent(nickname, vname, price)
        
    @staticmethod
    def end_rental(nickname):
        for rental in Rent.ACTIVE_RENTS:
            if nickname in rental:
                Rent.update(rental[0], rental[1], rental[2], rental[3])



###################### ----- TESTS MANAGER ---- #######################

g = Manager()

texto_utilizadores = ["ghost;rider;Pedro Mota;pedro@iscte-iul.pt;LCD;25.0",
                    "maria;itsme;Maria Mercedes;maria@iscte-iul.pt;LEI;40.0"]

for line in texto_utilizadores:
    info = line.split(";")
    u = User(info[0], info[1], info[2], info[3], info[4],eval(info[5]))
    if not g.exists_user(u.nickname):
        g.add_user(u)     
#print("=== Lista de utilizadores ===")
#g.list_users()

texto_viaturas = ["goat;Haibike Sduro All Mountain 7.0;False;0.50",
                  "mosca;BTwin Rockrider 5.2 S;False;0.50",
                  "melro;Bike Giant Sduro All Mountain 7.0;False;0.50",
                  "moscardo;Specialized Patanistic Speedo 1.2;True;0.75",
                  "cavalo;Specialized Fatboy;True;0.50"
                  ]

for line in texto_viaturas:
    info = line.split(";")
    v = Vehicle(info[0], info[1], eval(info[2]), eval(info[3]))
    if not g.exists_vehicle(v.name):
        g.add_vehicle(v)
        

#print("=== Lista de viaturas ===")
#g.list_vehicles()




##### Vehicle Management Methods
#  Verify if vehicle with X name exists        >>> V
# Get vehicle price by name                    >>> V
# Add new vehicle (verify name before adding)  >>> V 
# List all vehicle and its details             >>> V
# Record vehicle list                          >>> V

## User Management Methods
#  Verify if User with X nickname exists       >>> V
# Add new user (verify nickname before adding) >>> V
# List all user and its details                >>> V 
# Add budget to User by nickname               >>> V
# Alter User password by nickname              >>> V

## Rent Management
# See if a vehicle is not rented by its name   >>> X
# List available vehicles                      >>> X
# Make new rent by nickname and vehicle name   >>> X
# Add it to the active rent list (start time)  >>> X
# Get rent object from X User by nickname      >>> X
# List active rents                            >>> X
# finish rent by user nickname                 >>> X
    # update historic file                     >>> X
    # remove rent from system memory           >>> X
    # update user budget                       >>> X

## info to display on screen
    # vehicle number registered
    # number of users regitered 
    # sum of all users budget
    # top 5 users tih more budget
    # list all courses and number of users in each
    # number of active rents 
