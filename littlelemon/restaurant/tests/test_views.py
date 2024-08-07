from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setup(self):
        self.client = APIClient()
        self.menu1 = Menu.objects.create(menu_id=1, title="IceCream", price=80, inventory=100)
        self.menu1 = Menu.objects.create(menu_id=2, title="Cake", price=120, inventory=50)

    def test_getall(self):
        url = reverse('menuitem-list')

        response = self.client.get(url)

        menus = Menu.objects.all()

        serializer = MenuSerializer(menus, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.data, serializer.data)
