# -*- coding: utf-8 -*-

from users.models import User
from django.test import LiveServerTestCase
from selenium import webdriver


class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
        self.create_test_user()

    def tearDown(self):
        self.browser.quit()

    def create_test_user(self):
        user = self.get_saved_user_info()
        User.objects.create_user(
            email=user['email'],
            username=user['username'],
            password=user['password']
        )

    def get_saved_user_info(self):
        return {
            'email': 'func_tester@hanyang.ac.kr',
            'username': 'tester',
            'password': 'testtest',
        }

    def get_invalid_user_info(self):
        return {
            'email': 'invalid@invalid.com',
            'username': 'username@specialcharacter#!@#][]',
            'password': 't',
        }

    def get_temp_user_info(self):
        return {
            'email': 'test2@hanyang.ac.kr',
            'username': 'test',
            'password': 'testtest',
        }

    def test_root_url_response_signup_page(self):
        self.browser.get(self.live_server_url)
        self.assertIn(u'가입하기 | 한양중고장터', self.browser.title)
        email_input = self.browser.find_element_by_id('id_email')
        password_input = self.browser.find_element_by_id('id_password')
        username_input = self.browser.find_element_by_id('id_username')
        signup_button = self.browser.find_element_by_id('signup_forms_submit')
        self.assertEquals(
            email_input.get_attribute('placeholder'),
            u'이메일'
        )
        self.assertEquals(
            password_input.get_attribute('placeholder'),
            u'비밀번호'
        )
        self.assertEquals(
            username_input.get_attribute('placeholder'),
            u'사용자 이름'
        )
        self.assertEquals(
            signup_button.text,
            u'가입'
        )

    def test_invalid_user_signup_was_failed(self):
        self.browser.get(self.live_server_url)
        email_input = self.browser.find_element_by_id('id_email')
        password_input = self.browser.find_element_by_id('id_password')
        username_input = self.browser.find_element_by_id('id_username')
        signup_button = self.browser.find_element_by_id('signup_forms_submit')

        user = self.get_saved_user_info()
        signup_button.click()

        errors = self.browser.find_elements_by_class_name('errorlist')
        self.assertEquals(errors[0].text, u'이메일을 입력해주세요.')
        self.assertEquals(errors[1].text, u'사용자 이름을 입력해주세요.')
        self.assertEquals(errors[2].text, u'비밀번호를 입력해주세요.')

        email_input = self.browser.find_element_by_id('id_email')
        password_input = self.browser.find_element_by_id('id_password')
        username_input = self.browser.find_element_by_id('id_username')
        signup_button = self.browser.find_element_by_id('signup_forms_submit')

        user = self.get_invalid_user_info()
        email_input.send_keys(user['email'])
        password_input.send_keys(user['password'])
        username_input.send_keys(user['username'])
        signup_button.click()

        errors = self.browser.find_elements_by_class_name('errorlist')
        self.assertEquals(errors[0].text, u'올바르지 않은 이메일입니다.')
        self.assertEquals(errors[1].text, u'사용자 이름에는 알파벳 대소문자, 숫자만 사용 가능합니다.')
        self.assertEquals(errors[2].text, u'비밀번호의 길이가 너무 짧습니다.')

    def test_duplicate_user_signup_was_failed(self):
        self.browser.get(self.live_server_url)
        email_input = self.browser.find_element_by_id('id_email')
        password_input = self.browser.find_element_by_id('id_password')
        username_input = self.browser.find_element_by_id('id_username')
        signup_button = self.browser.find_element_by_id('signup_forms_submit')

        user = self.get_saved_user_info()
        email_input.send_keys(user['email'])
        password_input.send_keys(user['password'])
        username_input.send_keys(user['username'])
        signup_button.click()

        errors = self.browser.find_elements_by_class_name('errorlist')
        self.assertEquals(errors[0].text, u'이미 등록된 이메일입니다.')
        self.assertEquals(errors[1].text, u'이미 존재하는 사용자 이름입니다.')

    def test_valid_user_signup(self):
        self.browser.get(self.live_server_url)
        email_input = self.browser.find_element_by_id('id_email')
        password_input = self.browser.find_element_by_id('id_password')
        username_input = self.browser.find_element_by_id('id_username')
        signup_button = self.browser.find_element_by_id('signup_forms_submit')

        user = self.get_temp_user_info()
        email_input.send_keys(user['email'])
        password_input.send_keys(user['password'])
        username_input.send_keys(user['username'])
        signup_button.click()

        login_url = self.browser.current_url
        self.assertTrue(login_url.endswith('/login/'))

    def test_can_login_and_redirect_dashboard(self):
        self.browser.get(self.live_server_url + "/login")
        self.assertIn(u'로그인 | 한양중고장터', self.browser.title)

        user = self.get_saved_user_info()
        email_input = self.browser.find_element_by_id('id_email')
        password_input = self.browser.find_element_by_id('id_password')
        email_input.send_keys(user['email'])
        password_input.send_keys(user['password'])
        login_button = self.browser.find_element_by_id('login_forms_submit')
        login_button.click()
        dashboard_url = self.browser.current_url
        self.assertTrue(dashboard_url.endswith('/dashboard'))

    def test_dashboard_can_write_post(self):
        self.assertTrue(False)

    def test_dashboard_can_read_post(self):
        self.assertTrue(False)

    def test_dashboard_can_write_comment(self):
        self.assertTrue(False)

    def test_dashboard_can_read_comment(self):
        self.assertTrue(False)

    def test_dashboard_can_logout(self):
        self.assertTrue(False)
