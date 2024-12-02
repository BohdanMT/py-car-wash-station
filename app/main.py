class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand

class CarWashStation:
    def __init__(self, distance_from_city_center: float, clean_power: int, average_rating: float, count_of_ratings: int):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car):
        washing_price = round((car.comfort_class * (self.clean_power - car.clean_mark) * self.average_rating / self.distance_from_city_center), 1)
        return washing_price

    def serve_cars(self, cars: list[Car]):
        income = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
                print(self.calculate_washing_price(car))
                self.wash_single_car(car)
        return income

    def wash_single_car(self, car):
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def rate_service(self, rating):
        self.average_rating = round((self.average_rating * self.count_of_ratings + rating) / (self.count_of_ratings + 1), 1)
        self.count_of_ratings = self.count_of_ratings + 1
        return self.average_rating, self.count_of_ratings

bmw = Car(3, 3, "BMW")
audi = Car(4, 5, "Audi")
mers = Car(7, 1, "Mercedes")
cws = CarWashStation(6, 7, 3.9, 11)

price = cws.serve_cars([bmw, audi])
print(price)
