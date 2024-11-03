import random


def get_user_numbers():
    user_numbers = []
    while len(user_numbers) < 6:
        user_input = input("Podaj liczbę (1-49): ")

        try:
            number = int(user_input)
            if number < 1 or number > 49:
                print("Liczba musi być w zakresie 1-49.")
                continue
            if number in user_numbers:
                print("Już wpisałeś tę liczbę. Wybierz inną.")
                continue

            user_numbers.append(number)
        except ValueError:
            print("To nie jest poprawna liczba!")

    return sorted(user_numbers)


def draw_lotto_numbers():
    return sorted(random.sample(range(1, 50), 6))  # Losujemy 6 unikalnych liczb


def count_hits(user_numbers, drawn_numbers):
    hits = 0
    for number in user_numbers:
        if number in drawn_numbers:
            hits += 1
    return hits


def main():
    print("Witaj w grze LOTTO!")
    user_numbers = get_user_numbers()
    print(f"Twoje typowane liczby: {user_numbers}")

    drawn_numbers = draw_lotto_numbers()
    print(f"Wylosowane liczby: {drawn_numbers}")

    hits = count_hits(user_numbers, drawn_numbers)
    print(f"Trafiłeś {hits} liczby(-y).")


if __name__ == "__main__":
    main()