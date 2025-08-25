from seleniumbase import BaseCase

class TestExample(BaseCase):
    def test_basic_example(self):
        self.open("https://www.hko.gov.hk/tc/index.html")
        self.assert_text("天氣隨筆")