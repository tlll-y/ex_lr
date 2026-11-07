
class UndergroundSystem:
    def __init__(self):
        self.passengers = {}
        self.routes = {}

    def check_in(self, passenger_id, station, time):
        if passenger_id in self.passengers:
            raise ValueError("Пассажир уже зашел в метро")
        self.passengers[passenger_id] = (station, time)

    def check_out(self, passenger_id, station, time):
        if passenger_id not in self.passengers:
            raise ValueError("Пассажира не было в метро")

        start_station, start_time = self.passengers.pop(passenger_id)
        duration = time - start_time
        route = (start_station, station)

        if route not in self.routes:
            self.routes[route] = (duration, 1)
        else:
            total, count = self.routes[route]
            self.routes[route] = (total + duration, count + 1)

    def get_average_time(self, start_station, end_station):
        route = (start_station, end_station)

        if route not in self.routes:
            raise ValueError("Маршрута нет")

        total, count = self.routes[route]
        return total / count


metro = UndergroundSystem()

metro.check_in(1, "SOKOL", 5)
metro.check_out(1, "RS", 18)

metro.check_in(2, "SOKOL", 9)
metro.check_out(2, "RS", 33)

metro.check_in(3, "SOKOL", 17)
metro.check_out(3, "RS", 56)

print(metro.get_average_time("SOKOL", "RS"))
