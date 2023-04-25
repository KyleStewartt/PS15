class Car:
    def __init__(self, make, model, stickerPrice):
        self.make = make
        self.model = model
        self.stickerPrice = stickerPrice
    def discountPrice(self):
        return self.stickerPrice * 0.9
class Sport(Car):
    def __init__(self, make, model, stickerPrice):
        super().__init__(make, model, stickerPrice)
        self.sportWheels = 'N'
        self.sportEngine = 'N'
        self.sportInterior = 'N'
    def setSportWheels(self, option):
        self.sportWheels = option
    def setSportEngine(self, option):
        self.sportEngine = option
    def setSportInterior(self, option):
        self.sportInterior = option
    def priceWithOptions(self):
        price = self.discountPrice()
        if self.sportWheels == 'Y':
            price += 1000
        if self.sportEngine == 'Y':
            price += 3000
        if self.sportInterior == 'Y':
            price += 2000
        return price
def main():
    sportCar = Sport("Ford", "Mustang", 30000)
    sportCar.setSportWheels('Y')
    sportCar.setSportEngine('Y')
    sportCar.setSportInterior('Y')
    price = sportCar.priceWithOptions()
    print("Price with options: ", price)
if __name__ == "__main__":
    main()