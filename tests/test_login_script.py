import os
import allure
import pytest
from base.selenium_driver import SeleniumDriver
from pages.homepage import HomePage
from pages.loginpage import LoginPage
from utilities.excel_utils import ExcelUtils

@pytest.mark.usefixtures("setup")
class TestLoginScenario:

    file_path = os.path.join(os.path.dirname(__file__), "..", "testdata", "testdata.xlsx")

    @pytest.mark.parametrize("email,password", ExcelUtils.get_excel_data(file_path, "login_credentials"))
    def test_login(self, email, password):
        login = LoginPage(self.driver)
        login.login_to_application(email, password)

        home = HomePage(self.driver)

        welcome_msg = home.get_welcome_text()

        print("Welcome msg is " ,welcome_msg)

        assert "Welcome" in welcome_msg

            # If the test passes, perform logout
        home.logout_from_application()

