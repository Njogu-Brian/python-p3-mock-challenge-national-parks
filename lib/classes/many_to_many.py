# lib/classes/many_to_many.py

class Visitor:
    _all = []

    def __init__(self, name):
        self.name = name
        Visitor._all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception("Name must be a string.")
        if not (1 <= len(value) <= 15):
            raise Exception("Name must be between 1 and 15 characters.")
        self._name = value

    def trips(self):
        return [trip for trip in Trip._all if trip.visitor == self]

    def national_parks(self):
        return list({trip.national_park for trip in self.trips()})

    def total_visits_at_park(self, park):
        return len([trip for trip in self.trips() if trip.national_park == park])


class NationalPark:
    _all = []
    all = _all

    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception("Name must be a string.")
        if len(name) < 3:
            raise Exception("Name must be at least 3 characters.")
        self._name = name
        NationalPark._all.append(self)

    @property
    def name(self):
        return self._name

    def trips(self):
        return [trip for trip in Trip._all if trip.national_park == self]

    def visitors(self):
        return list({trip.visitor for trip in self.trips()})

    def total_visits(self):
        return len(self.trips())

    def best_visitor(self):
        if not self.trips():
            return None
        return max(self.visitors(), key=lambda v: v.total_visits_at_park(self))

    @classmethod
    def most_visited(cls):
        if not cls._all:
            return None
        return max(cls._all, key=lambda park: park.total_visits())


class Trip:
    _all = []
    all = _all

    def __init__(self, visitor, national_park, start_date, end_date):
        if not isinstance(visitor, Visitor):
            raise Exception("visitor must be a Visitor instance.")
        if not isinstance(national_park, NationalPark):
            raise Exception("national_park must be a NationalPark instance.")
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        Trip._all.append(self)
        Trip.all = Trip._all  # Ensures compatibility with tests

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        if not isinstance(value, str) or len(value) < 7:
            raise Exception("start_date must be a string with at least 7 characters.")
        self._start_date = value

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        if not isinstance(value, str) or len(value) < 7:
            raise Exception("end_date must be a string with at least 7 characters.")
        self._end_date = value

    @classmethod
    def clear_all(cls):
        cls._all = []
        cls.all = cls._all
