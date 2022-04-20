from django.test import TestCase

# Create your tests here.


class ViewsTestCaseBudgetHomes(TestCase):
    def test_url_loads_properly(self):
        """The url loads properly"""
        response = self.client.get('http://127.0.0.1:8000/user/get_budgetHomes/')
        self.assertEqual(response.status_code, 403)

class ViewsTestCaseSqftHomes(TestCase):  
    def test_url_loads_properly(self):
        """The url page loads properly"""
        response = self.client.get('http://127.0.0.1:8000/user/get_sqftHomes/')
        self.assertEqual(response.status_code, 403)

class ViewsTestCaseAgeHomes(TestCase):    
    def test_url_loads_properly(self):
        """The url page loads properly"""
        response = self.client.get('http://127.0.0.1:8000/user/get_ageHomes/')
        self.assertEqual(response.status_code, 403)

class ViewsTestCaseStandardPrices(TestCase):     
    def test_url_loads_properly(self):
        """The url page loads properly"""
        response = self.client.get('http://127.0.0.1:8000/user/get_standardPrices/')
        self.assertEqual(response.status_code, 403)