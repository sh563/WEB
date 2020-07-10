from new_car import car
from Car_collection import collectionCar
from car import functionsdealer

if __name__ == "__main__":
    car1 = car('MV45', 'Lamboghini', '18840', '20000', '2019', '2020')
    car2 = car('MX545', 'Mazda', '13400', '25000', '2014', '2014')
    car3 = car('ES350', 'Lexus', '35700', '56000', '2018', '2020')
    car4 = car('ES352', 'Lexus', '21700', '25000', '2019', '2019')
    car5 = car('ES353', 'Lexus', '10700', '98000', '2017', '2019')
    car6 = car('MZ2018', 'Honda', '10700', '98000', '2015', '2020')
    car7 = car('MX620', 'Mazda', '13400', '28000', '2014', '2014')
    car8 = car('MX615', 'Honda', '13400', '25000', '2014', '2014')
    car9 = car('MX623', 'Feraty', '13400', '26000', '2014', '2014')
    coll = collectionCar()
    m = functionsdealer()

    # Add cars into the car list
    coll.addCar(car1)
    coll.addCar(car2)
    coll.addCar(car3)
    coll.addCar(car4)
    coll.addCar(car5)
    coll.addCar(car6)
    coll.addCar(car7)

    # Show all data relating to cars on the screen

    print("Display all of the objects that the user created in the list on the screen: ")
    count = 0
    for i in coll.get_list():
        model, make, purchase_price, sold_price, purchase_date, sold_date = coll.get_list_information(i)
        count += 1
        print("car " + str(count) + ": " , model, make, purchase_price, sold_price, purchase_date, sold_date)

    # Display on the screen the car was sold in a certain year

    print("----------------------------------------------------------------------")
    print("Search for certain car in a specific year: ")
    coll.get_list_information_year('2019')

    print("----------------------------------------------------------------------")
    print("Total car sales of a year: ")

    # Total Sale for a certain year
    total = m.saleyear('2019', coll.get_list())
    print("The total sale of this year: " + "$" + str(total))

    # Total net benefit for a certain year
    total1 = m.benefityear('2019', coll.get_list())
    print("The total net benefit of this year: " + "$" + str(total1))

    # Total number of cars sold for a specific make
    total2 = m.soldmake('Honda', coll.get_list())
    print("The number of this car: " +  str(total2))

    # Total number of cars purchased for a specific make
    total3 = m.purchase('Mazda', coll.get_list())
    print("The sale number of this kind of car: " + str(total3))



