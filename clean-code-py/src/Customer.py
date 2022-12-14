class Customer:
    def __init__(self, name):
        self.__name = name
        self.__rentals = []

    def add_rental(self, arg):
        self.__rentals.append(arg)

    def get_name(self):
        return self.__name

    # def convert_to_html(self, result):
    #     html_email = "<p> + "f"Dear {self.get_name()}" + "</p>" + \
    #                  "<p>" + result.replace("\n", " <br> ") + " </p> " + \
    #                  "<p>" + "Thank-you" + "</p>"
    #     return html_email

    def text_statement(self):
        result = "Rental Record for " + self.get_name() + "\n"
        for rental in self.__rentals:
            result += "\t" + rental.get_movie().get_title() + "\t" + str(rental.amount()) + "\n"

        result += "Amount owed is " + str(self.total_amount()) + "\n"
        result += "You earned " + str(self.total_frequent_renter_points()) + " frequent renter points"
        return result

    def html_statement(self):
        result = "<h1>" + "Rental Record for " + self.get_name() + "</h1><br><p>"

        for rental in self.__rentals:
            result += "\t" + rental.get_movie().get_title() + "\t" + str(rental.amount()) + "<br>"

        result += "Amount owed is " + str(self.total_amount()) + "<br>"
        result += "You earned " + str(self.total_frequent_renter_points()) + " frequent renter points</p>"
        return result

    def total_amount(self):
        total_amount = 0
        for rental in self.__rentals:
            total_amount += rental.amount()
        return total_amount

    def total_frequent_renter_points(self):
        total_frequent_renter_points = 0
        for rental in self.__rentals:
            total_frequent_renter_points += rental.frequent_rental_points()
        return total_frequent_renter_points
