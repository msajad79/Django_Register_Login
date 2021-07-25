from django.test import TestCase
from django.core import mail
from django.contrib.auth.models import User
from bs4 import BeautifulSoup

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
        res_register = self.client.post('/accounts/register/', data=data)
        
        self.assertEqual(res_register.status_code, 302)
        self.assertEqual(res_register.url, '/accounts/register/activate/')

        self.assertTrue(User.objects.filter(username='user1').exists())
        user1 = User.objects.get(username='user1')
        self.assertFalse(user1.is_active)

        self.assertEqual(len(mail.outbox), 1)
        self.assertTrue(mail.outbox[0], 'Active your account')
        body = mail.outbox[0].body
        soup = BeautifulSoup(body, 'html.parser')
        link_activate = soup.find('a', id='activate_link')
        self.assertNotEqual(link_activate, None)
        link_activate = link_activate['href']

        res_activate = self.client.get(link_activate)

        self.assertEqual(res_activate.status_code, 200)

        self.assertTrue(User.objects.get(username='user1').is_active)

        res_login = self.client.login(username=data['username'], password=data['password1'])
        self.assertTrue(res_login)

