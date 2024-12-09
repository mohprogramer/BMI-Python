# def check(cars: list):
#     cars.append("BMW")
#     print(cars)
# vehicles = ["audi", "volvo"]
# check(vehicles[:])  
# print(vehicles)  

 
def is_car_available(year: int ,*cars):
    cars_available = {2024: ["BMW", "Audi", "Tesla"],
                      2023: ["Volvo"]}

    models = cars_available.get(year)
    if not models:
        print(f"'{year}' Not faund")
        return
    models = [model.strip().lower() for model in models]    
    print(models, cars)
    for car in cars:
        if car.strip().lower() in models:
            print(f"{car.title()} is available")    
        else:
            print(f"Unfortunatley '{car.title()}' is not available")
is_car_available(2024,"audi","bMW")    