class Bus:
    
    def __init__(self, route, destination):
        
        routes = {50: ["Waverly Station", "Mars", "The Moon", ], 22: ["Waverly Station", "Leith", "Ocean Terminal"]}
        self.route_number = route
        self.destination = destination
        self.passengers = []
        self.route = routes[route]

    def drive(self):
        return "Brum brum"

    def passenger_count(self):
        return len(self.passengers)


    def pick_up(self, person):
        if self.destination == person.destination:
            self.passengers.append(person)

    def drop_off(self, person):
        self.passengers.remove(person)


    def empty(self):
        self.passengers = []

    def pick_up_from_stop(self, bus_stop):
        for person in bus_stop.queue:
            for place in self.route:
                if person.destination == place:
                    self.passengers.append(person)
                    bus_stop.queue.remove(person)
        
        
        # self.passengers.extend(bus_stop.queue)