class collectionCar:
    def __init__(self):
        self.collectionCar = []
    def get_list_information(self, car):
        for i in self.collectionCar:
            if i.get_model() == car.get_model():
                model = i.get_model()
                make = i.get_make()
                purchase_price = i.get_purchase_price()
                sold_price = i.get_sold_price()
                purchase_date = i.get_purchase_date()
                sold_date = i.get_sold_date()
        return model, make, purchase_price, sold_price, purchase_date, sold_date

    def get_list_information_year(self, year):
        for i in self.collectionCar:
            if i.get_sold_date() == year:
                model = i.get_model()
                make = i.get_make()
                purchase_price = i.get_purchase_price()
                sold_price = i.get_sold_price()
                purchase_date = i.get_purchase_date()
                sold_date = i.get_sold_date()
                print(model, make, purchase_price, sold_price, purchase_date, sold_date)


    def get_list(self):
        return self.collectionCar

    def addCar(self, car):
        self.collectionCar.append(car)

    def removeCar(self, car):
        self.collectionCar.remove(car)

    def modify(self, cars, model, make, purchase, sold, puchase_date, sold_date):
        for i in self.collectionCar:
            if i.get_model() == cars.get_model():
                i.set_model(model)
                i.set_make(make)
                i.set_purchase_price(purchase)
                i.set_sold_price(sold)
                i.set_purchase_date(puchase_date)
                i.set_sold_date(sold_date)
