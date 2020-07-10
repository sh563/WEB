class car:
    def __init__(self, model, make, purchase_price, sold_price, purchase_date, sold_date):
        self.model = model
        self.make = make
        self.purchase_price = purchase_price
        self.sold_price = sold_price
        self.purchase_date = purchase_date
        self.sold_date = sold_date

    def get_model(self):
        return self.model

    def set_model(self, model):
        if model is None:
            return self.model
        else:
            self.model = model

    def get_make(self):
        return self.make

    def set_make(self, make):
        if make is None:
            return self.make
        else:
            self.make = make

    def get_purchase_price(self):
        return self.purchase_price

    def set_purchase_price(self, purchase_price):
        if purchase_price is None:
            return self.purchase_price
        else:
            self.purchase_price = purchase_price

    def get_sold_price(self):
        return self.sold_price

    def set_sold_price(self, sold_price):
        if sold_price is None:
            return self.sold_price
        else:
            self.sold_price = sold_price

    def get_purchase_date(self):
        return self.purchase_date

    def set_purchase_date(self, purchase_date):
        if purchase_date is None:
            return self.purchase_date
        else:
            self.purchase_date = purchase_date


    def get_sold_date(self):
        return self.sold_date


    def set_sold_date(self, sold_date):
        if sold_date is None:
           return self.sold_date
        else:
           self.sold_date = sold_date
