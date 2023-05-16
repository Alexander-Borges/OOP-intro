#declare a class and give it name Shoe
class Shoe:
    def __init__(self, brand, shoe_type, price):
        self.brand = brand
        self.type = shoe_type
        self.price = price 
        self.in_stock = "True"
        # the status is set to True by default
    
skater_shoe = Shoe("Vans", "Low-top Trainers", 59.99)
dress_shoe = Shoe("Jack & Jill Bootery", "Ballet Flats", 29.99) 
print(skater_shoe.type)
print(dress_shoe.type)
