class Venue:
    def __init__(self, name: str, max_seats: int, seats: list =[]) -> None:
        self._name = name
        self._max_seats = max_seats
        self._seats = seats

    def __str__(self) -> str:
        return self._name + ": com " + str(len(self._seats)) + " lugares."

    def get_name(self) -> str:
        return self._name

    def get_seats(self) -> list:
        return self._seats

    def get_seat(self, number):
        if number - 1 < 0:
            print("Número de lugar inválido")
            return None
        return self._seats[number - 1]

    def set_seats(self, seats: int) -> None:
        self._seats = seats
        return None

    def add_seat(self, seat) -> str:
        if seat in self._seats:
            return "Lugar já existe"

        if len(self._seats) >= self._max_seats:
            return "Número de lugares excedido, o lugar não foi adicionado"

        self._seats.append(seat)
        return ""

    def cancel_occupied(self, number) -> str:
        for seat in self._seats:
            if seat._o_number == number:
                seat.cancel_occupied()
                return "Cancelado"
        return "Não foi possível achar a reserva"


    def get_occupied_seats(self) -> list:
        result = []
        for seat in self._seats:
            if seat.occupied:
                result.append(seat)
        return result
