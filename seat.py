class Seat:
    def __init__(self, number, occupied) -> None:
        self.number = number
        self.occupied = occupied

    def __str__(self) -> str:
        return f'Lugar {self.number}: {"Ocupado" if self.occupied else "Não Ocupado"}'


seat1 = Seat(1, True)
seat2 = Seat(2, False)
seat3 = Seat(3, True)

print(seat1)
print(seat2)
print(seat3)