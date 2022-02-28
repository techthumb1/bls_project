# We need to import the unittest module to use it
import unittest
# We need to import the module we want to test
import bls_api.bls_api as bls_api


class TestBlsApi(unittest.TestCase):
    """
    This class contains all the tests for the bls_api module
    """

    def test_get_all_states(self):
        """
        This method tests the get_all_states method
        """
        # We need to get the states
        states = bls_api.get_all_states()
        # We need to check if the states are
        # not empty
        self.assertIsNotNone(states)
        # We need to check if the states are
        # not empty
        self.assertNotEqual(states, [])
        # We need to check if the states are a list
        self.assertIsInstance(states, list)


    def test_get_all_counties(self):
        """
        This method tests the get_all_counties method
        """
        # We need to get the counties
        counties = bls_api.get_all_counties()
        # We need to check if the counties are
        # not empty
        self.assertIsNotNone(counties)
        # We need to check if the counties are
        # not empty
        self.assertNotEqual(counties, [])
        # We need to check if the counties are a list
        self.assertIsInstance(counties, list)
        

    def test_get_all_cities(self):
        """
        This method tests the get_all_cities method
        """
        # We need to get the cities
        cities = bls_api.get_all_cities()
        # We need to check if the cities are
        # not empty
        self.assertIsNotNone(cities)
        # We need to check if the cities are
        # not empty
        self.assertNotEqual(cities, [])
        # We need to check if the cities are a list
        self.assertIsInstance(cities, list)


yield TestBlsApi # We need to yield the class
     
if __name__ == '__main__':
    unittest.main()


    
