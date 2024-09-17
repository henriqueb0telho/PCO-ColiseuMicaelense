from time import time

class Seat:
    def __init__(self, number, occupied) -> None:
        self.number = number
        self.occupied = occupied
        self._o_name = ""   # Nome da Reserva
        self._o_number = "" # Código de Reserva

    def __str__(self) -> str:
        return f'Lugar {self.number}: {"Ocupado" if self.occupied else "Não Ocupado"}'

    def get_o_name(self) -> str:
        return self._o_name

    def get_o_number(self) -> str:
        return self._o_number

    def set_o_name(self, o_name: str) -> None:
        self._o_name = o_name

    def set_o_number(self, o_number: str) -> None:
        self._o_number = o_number

    def occupy_seat(self):
        if self.occupied:
            return "Lugar já se encontra reservado."

        self.occupied = True

        name = str(input("Introduza o seu nome: "))
        number = "VA-" + str(int(time()))

        self.set_o_name(name)
        self.set_o_number(number)
        print(f"\nO lugar {self.number} foi reservado no nome {self.get_o_name()} e com o número de reserva {self.get_o_number()}!")
        return None

    def cancel_occupied(self) -> None:
        self.occupied = False
        self._o_name = ""
        self._o_number = ""



for i in range(1, 2+1):
    print(i)