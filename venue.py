class Venue:
    def __init__(self, name: str, seats: list =[]) -> None:
        self._name = name
        self._seats = seats

    def __str__(self) -> str:
        return self._name + ": com " + str(self._seats) + "lugares."

    def get_name(self) -> str:
        return self._name

    def get_seats(self) -> list:
        return self._seats

    def set_seats(self, seats: int) -> None:
        self._seats = seats
        return None