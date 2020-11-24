from src.person import Person

class BusStop:
    def __init__(self, name):
        self.name = name
        self.queue = []

    def add_to_queue(self, person):
        self.queue.append(person)

    def queue_length(self):
        return len(self.queue)

    def clear(self):
        self.queue = []

    def remove_from_queue(self, person):
        self.queue.remove(person)

    def add_people_to_queue(self, people):
        self.queue.extend(people)