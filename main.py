from venue import Venue
from seat import Seat

def main() -> None:
    venue_name = str(input('Nome do Espaço? '))
    venue_seats = int(input('Número de lugares do Espaço? '))

    # Cria o espaço
    venue = Venue(venue_name, venue_seats)

    # Cria uma lista com o número máximo de lugares
    seats = [Seat(seat, False) for seat in range(1, venue_seats + 1)]

    print(venue)

    # Introduz os lugares no Espaço
    for seat in seats:
        print(venue.add_seat(seat))

    # Mostra os lugares
    for lugar in venue.get_seats():
        print(lugar)

    # Reserva os primeiros dois lugares para teste
    for i in range(1, 4+1):
        lugar = venue.get_seat(i)
        lugar.occupy_seat()

    for lugar in venue.get_seats():
        print(lugar)

    print(venue.cancel_occupied(str(input("Introduza o nr de reserva: "))))
    print(venue.cancel_occupied(str(input("Introduza o nr de reserva: "))))

    print('\n\nLugares Ocupados:')
    for lugar in venue.get_occupied_seats():
        print(f'{lugar.number}: {lugar.get_o_name()} - {lugar.get_o_number()}')

    for lugar in venue.get_seats():
        print(lugar)

    return None

if __name__ == '__main__':
    main()