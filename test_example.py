from seleniumbase import BaseCase

class TestExample(BaseCase):
    def test_basic_example(self):
        opened_url = "https://www.hko.gov.hk/tc/index.html"

        self.driver.execute_cdp_cmd("Network.enable", {})
        self.driver.execute_cdp_cmd("Network.clearBrowserCache", {})

        self.open(opened_url)
        
        current_url = self.get_current_url()
        
        status_code = self.get_link_status_code(opened_url)

        assert opened_url == opened_url, f"Opened URL: {opened_url}\nCaptured URL: {current_url}\nStatus: {status_code}"
        
        assert status_code == 200, f"Expected status code 200, but got {status_code}"
        