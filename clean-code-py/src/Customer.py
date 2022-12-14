from .Movie import Movie


class Customer:
    def __init__(self, name):
        self.__name = name
        self.__rentals = []

    def add_rental(self, arg):
        self.__rentals.append(arg)

    def get_name(self):
        return self.__name

    def convert_to_html(self, result):
        html_email = "<p> + "f"Dear {self.get_name()}" + "</p>" + \
                     "<p>" + result.replace("\n", " <br> ") + " </p> " + \
                     "<p>" + "Thank-you" + "</p>"
        return html_email

    def statement(self):
        total_amount = 0
        frequent_renter_points = 0
        result = "Rental Record for " + self.get_name() + "\n"
        for rental in self.__rentals:
            amount = rental.amount()

            frequent_renter_points += rental.frequent_rental_points()
            result += "\t" + rental.get_movie().get_title() + "\t" + str(amount) + "\n"
            total_amount += amount

        result += "Amount owed is " + str(total_amount) + "\n"
        result += "You earned " + str(frequent_renter_points) + " frequent renter points"
        return result

    def html_statement(self):
        total_amount = 0
        frequent_renter_points = 0
        result = "<h1>" + "Rental Record for " + self.get_name() + "</h1><br>"
        for rental in self.__rentals:
            amount = rental.amount()
            result += "\t" + rental.get_movie().get_title() + "\t" + str(amount) + "<br>"
            frequent_renter_points += rental.frequent_rental_points()
            total_amount += amount

        result += "Amount owed is " + str(total_amount) + "<br>"
        result += "You earned " + str(frequent_renter_points) + " frequent renter points"
        return result

