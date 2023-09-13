from django.test import TestCase, Client
from main.models import Item

class MainTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_main_url_is_exist(self):
        response = self.client.get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = self.client.get('/main/')
        self.assertTemplateUsed(response, 'main.html')

    def test_main_contains_expected_data(self):
        response = self.client.get('/main/')
        # Ensure that the rendered HTML contains data from your context
        self.assertContains(response, 'MARCARD')
        self.assertContains(response, 'Gamma Farrel')
        self.assertContains(response, 'PBP-E')
        self.assertContains(response, 'Celestials')
        self.assertContains(response, '100')
        self.assertContains(response, 'Zeus')

    def test_item_model(self):
        # Create a test Product instance
        product = Item.objects.create(
            name='Test Product',
            description='Test description',
            amount='20',
        )
        # Query the database to check if the product was created
        saved_product = Item.objects.get(id=product.id)
        self.assertEqual(saved_product.name, 'Test Product')

    def test_invalid_main_url_returns_404(self):
        response = self.client.get('/invalid_url/')
        self.assertEqual(response.status_code, 404)