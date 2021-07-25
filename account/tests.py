from django.test import TestCase
from django.core import mail
from django.contrib.auth.models import User

class RegisterTest(TestCase):
    def setUp(self) -> None:
        #User.objects.create_user(username='user1',email='ex@ex.com',password='1234')
        pass

    def test_register_form(self):
        data = {
            'username': 'user1',
            'email': 'ex@ex.com',
            'password1': 'th1s 1s s00000 hard pa55word',
            'password2': 'th1s 1s s00000 hard pa55word'
        }
        res = self.client.post('/account/register/', data=data)
        user1 = User.objects.get(username='user1')
        print(res)
        print(user1)
        print(user1.profile.bio)
        print(mail.outbox[0].body)
