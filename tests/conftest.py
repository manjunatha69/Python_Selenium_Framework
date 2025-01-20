import allure
import pytest
from base.selenium_driver import SeleniumDriver
from base.webdriverfactory import WebDriverFactory

@pytest.fixture(scope="class")
def setup(request):

    wdf = WebDriverFactory()

    driver = wdf.getWebDriverInstance()

    if request.cls is not None:
        request.cls.driver=driver

    print("Application is  up and running")

    yield driver

    driver.quit()

    print("Closing the browser")

@pytest.hookimpl(tryfirst=True,hookwrapper=True)
def pytest_runtest_makereport(item,call):

    outcome=yield

    report=outcome.get_result()

    if report.when=="call" and (report.failed or report.outcome=="broken"):

        if hasattr(item.instance,"driver"):
            driver=item.instance.driver

            selenium_driver=SeleniumDriver(driver)

            screenshot_path=selenium_driver.take_screenshot()

            with allure.step("Attach Screenshot On Failure/Broken"):
                    allure.attach.file(screenshot_path,name="Failure Screenshot",attachment_type=allure.attachment_type.PNG)

            with allure.step("Exception Details"):
                    allure.attach(str(call.excinfo),name="Exception Details",attachment_type=allure.attachment_type.TEXT)




