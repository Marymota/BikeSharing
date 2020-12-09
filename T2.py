from T1 import Vehicle
from T1 import User
import time
import csv    



class Rent(Vehicle,User):
    ACTIVE_RENTS = []

    def __init__(self, nickname, vname, price):
        self.nickname = nickname
        self.vname = vname
        self.price = Vehicle.get_price(vname)
        self.set_start()


    def set_start(self):
#  self.verification()
        start = time.time()
        print(time.ctime(start))
        print("Your jorney has started... {:.2f}€ will be charged for each hour".format(self.price))
        Rent.ACTIVE_RENTS.append((int(start), self.nickname, self.vname, ("%.2f" % self.price)))
        
    @staticmethod
    def update(start, nickname, vname, price):
        end = time.time()
        elapsed_seconds = int(end) - int(start)
        if elapsed_seconds <= 3600:
            cost = price
        else: 
            cost = (float(price) / 3600) * elapsed_seconds
        print(f"{int(start)}, {nickname}, {vname}, {price}, {elapsed_seconds}, {cost}")
        print("{nickname} jorney has ended. A total of {cost}€ will be charged.")
        for rent in Rent.ACTIVE_RENTS:
            if nickname in rent:
                i = Rent.ACTIVE_RENTS.index(rent)
                list_active_rents = list(Rent.ACTIVE_RENTS[i])
                list_active_rents.append(elapsed_seconds)
                list_active_rents.append(cost)
                Rent.ACTIVE_RENTS[i] = tuple(list_active_rents)
                Rent.__write_file(Rent.ACTIVE_RENTS[i])
        Rent.end_rental(nickname)

    @staticmethod
    def end_rental(nickname):
        for rental in Rent.ACTIVE_RENTS:
            if nickname in rental:
                Rent.ACTIVE_RENTS.remove(rental)
                

#    def set_nickname(self, nickname):
#        self.nickname = User.get_nickname()
#
    def set_vname(self, vname):
        self.vname = vname

    def set_price(self, price):
        self.price = price

    def print_details(self, start):
        print(f"{start}, {self.nickname}, {self.name}, {self.price}")  


    @classmethod
    def __write_file(cls, index):
        with open("historic.csv", "a", newline='') as result:
            try:
                writer = csv.writer(result, delimiter=',')
                writer.writerow(index)
            finally:
                result.close()
        print(Rent.ACTIVE_RENTS)
    
    def verification(self):
        if Rent.ACTIVE_RENTS != []:
            for rental in Rent.ACTIVE_RENTS:
                if self.nickname in rental:
                    print(f"{self.nickname} is already biking!")
                    return 0
                elif self.vname in rental:
                    print(f"{self.vname} is already rolling!")
                    return 0





#rent = Rent('ghost', 'shiva', '0.50')
#rent = Rent('cloud', 'mizuki', '0.50')
##### TESTS

### List of stuff to do ###                                                                               
##### T2 RENT & Manager Object Class #####

# Create a temporary object type "Rent"         >>> V  
# Link the attributes from other classes
# (User nickname and name and price of vehicle) >>> X  
# Method that calculates usage time (time lib)  >>> V   
# Method "update" time and price of rent        >>> V            
# Add info to file historic.csv line by line    >>> V
# Formating info in historic file               >>> V