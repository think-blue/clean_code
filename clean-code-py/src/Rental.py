from src.Movie import Movie


class Rental:
    def __init__(self, movie, days_rented):
        self.__movie = movie
        self.__daysRented = days_rented

    def get_days_rented(self):
        return self.__daysRented

    def get_movie(self):
        return self.__movie

    def frequent_rental_points(self):
        frequent_renter_points = 1
        if self.get_movie().get_price_code() == Movie.NEW_RELEASE and self.get_days_rented() > 1:
            frequent_renter_points += 1
        return frequent_renter_points

    def amount(self):
        this_amount = 0
        price_code = self.get_movie().get_price_code()
        # Determine amount for each line
        if price_code == Movie.REGULAR:
            this_amount += 2
            if self.get_days_rented() > 2:
                this_amount += (self.get_days_rented() - 2) * 1.5

        elif price_code == Movie.NEW_RELEASE:
            this_amount += self.get_days_rented() * 3

        elif price_code == Movie.CHILDREN:
            this_amount += 1.5
            if self.get_days_rented() > 3:
                this_amount += (self.get_days_rented() - 3) * 1.5
        return this_amount
