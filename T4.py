from T3 import Manager

def menu():
    print("[1] List Users")
    print("[2] Add to user budget")
    print("[3] Alter user password")
    print("[4] Request a bike")
    print("[5] Return bike ")
#    print("[6] Listar alugueres ativos")
#    print("[7] Listar viaturas disponíveis")
#    print("[8] Informações do sistema")
#    print("[9] Actividade por hora e dia da semana")
    print("[0] Exit")


menu()
option = int(input("Enter your option: "))
while option != 0:
    if option == 1:
        print("=== List Users ===")
        Manager.list_users()
    elif option == 2:
        print("=== Add Budget ===")
        Manager.add_budget(input("Nickname: "), input("Euros: "))
    elif option == 3:
        print("=== Alter user Password ===")
        Manager.password_change(input("Nickname: "))
    elif option == 4:
        print("=== Request a Bike ===")    
        Manager.start_rental(input("Nickname: "), input("Vehicle name: "))
    elif option == 5:
        print("=== Return Bike ===")    
        Manager.end_rental(input("Nickname: "))
    elif option == 6:
        print("=== List Active Rentals ===")    
        Manager.end_rental(input("Nickname: "))
    else:
        print("Invalid option.")
    
    print()        
    menu()
    option = int(input("Enter your option: "))