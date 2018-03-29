import os
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
import time

MAX_WAIT = 10


class NewVisitorTest(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        staging_server = os.environ.get('STAGING_SERVER')
        if staging_server:
            self.live_server_url = 'http://' + staging_server


    def tearDown(self):
        self.browser.quit()


    def check_wait(self, correct_value):
        start_time = time.time()
        while True:
            try:
                actual_data = self.browser.find_elements_by_tag_name('some_tag')
                self.assertIn(correct_value, actual_data)
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)


    def test_can_start_a_list_for_one_user(self):
        self.browser.get(self.live_server_url)
        self.do_something()
        self.check_wait("Some generic text")
