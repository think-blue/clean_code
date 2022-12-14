import unittest
from src.Customer import Customer
from src.Rental import Rental
from src.Movie import Movie


class TestCustomer(unittest.TestCase):
    # def runTest(self):
    #     customer = Customer("Random Name")
    #     self.assertTrue(True)

    # def test_should_generate_statement(self):
    #     customer = Customer("Chinmay Dhawan")
    #     customer.add_rental(Rental(Movie("Avatar", 0), 10))
    #     customer.add_rental(Rental(Movie("Home Alone", 2), 8))
    #     customer.add_rental(Rental(Movie("Avatar II", 1), 9))
    #     print(customer.statement())
    #     self.assertTrue(True)

    def test_should_generate_html_statement(self):
        customer = Customer("Chinmay Dhawan")
        customer.add_rental(Rental(Movie("Avatar", 0), 10))
        customer.add_rental(Rental(Movie("Home Alone", 2), 8))
        customer.add_rental(Rental(Movie("Avatar II", 1), 9))
        # print(customer.html_statement())
        self.assertEqual(customer.html_statement(),
                         "<h1>Rental Record for Chinmay Dhawan</h1><br>	Avatar	14.0<br>	Home Alone	9.0<br>	Avatar "
                         "II	27<br>Amount owed is 50.0<br>You earned 4 frequent renter points")


if __name__ == '__main__':
    unittest.main()
