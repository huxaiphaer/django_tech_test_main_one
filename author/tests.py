import json

from django.test import TestCase
from django.urls import reverse

from author.models import User


class AuthorListViewTestCase(TestCase):

    def setUp(self):
        self.url = reverse("authors-list")
        self.region_1 = User.objects.create(
            username='test1',
            email='test1@gmail.com',
            last_name='test1',
            first_name='test2',
        )

    def test_creates_new_user(self):
        payload = {
            "username": "test2",
            "email": "test2@gmail.com",
            "last_name": "test1",
            "first_name": "test2"
        }
        user = User.objects.last()
        response = self.client.post(
            self.url, data=json.dumps(payload), content_type="application/json"
        )
        self.assertEqual(response.status_code, 201)
        self.assertIsNotNone(user)


class UserViewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username='test1',
            email='test1@gmail.com',
            last_name='test1',
            first_name='test2',
        )
        self.url = reverse("author", kwargs={"author_id": self.user.id})

    def test_serializes_single_record_with_correct_data_shape_and_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertCountEqual(
            response.json(),
            {
                "id": self.user.id,
                "username": "test1",
                "email": "test1@gmail.com",
                "last_name": "test1",
                "first_name": "test2",
            },
        )

    def test_updates_user(self):
        payload = {
                "id": self.user.id,
                "username": "test1",
                "email": "test1@gmail.com",
                "last_name": "huzai",
                "first_name": "idris",
        }
        response = self.client.put(
            self.url, data=json.dumps(payload), content_type="application/json"
        )
        region = User.objects.get(id=self.user.id)
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(region)
        self.assertEqual(User.objects.count(), 1)
        self.assertDictEqual(
            {
                "id": self.user.id,
                "username": "test1",
                "email": "test1@gmail.com",
                "last_name": "huzai",
                "first_name": "idris",
            },
            response.json(),
        )

    def test_removes_user(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(User.objects.count(), 0)

