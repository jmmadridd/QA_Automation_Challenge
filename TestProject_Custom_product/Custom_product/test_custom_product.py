from selenium.webdriver.common.by import By
from src.testproject.classes import DriverStepSettings, StepSettings
from src.testproject.decorator import report_assertion_errors
from src.testproject.enums import SleepTimingType
from src.testproject.sdk.drivers import webdriver
import pytest


"""
    Project: QA Automation Challenge
    Test: Custom product Paypal
    Author: Javier Martinez (jmmadridd@gmail.com)
"""


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(token="mMSlzTkBQJ8CEKkRB8AtftI9NhxgoAHZXi9YSfDTDTg1",
                              project_name="My first Project",
                              job_name="Custom product")
    step_settings = StepSettings(timeout=15000,
                                 sleep_time=500,
                                 sleep_timing_type=SleepTimingType.Before)
    with DriverStepSettings(driver, step_settings):
        yield driver
    driver.quit()


@report_assertion_errors
def test_main(driver):
    """Custom product"""
    # Test Parameters
    # Auto generated application URL parameter
    ApplicationURL = "https://salvajerealbrand.com"

    # 1. Navigate to '{ApplicationURL}'
    # Navigates the specified URL (Auto-generated)
    driver.get(f'{ApplicationURL}')

    # 2. Click 'CUSTOMIZE'
    customize = driver.find_element(By.XPATH,
                                    "//section[1]/div/div[2]/div/div/div/nav[1]//a[. = 'Customize']")
    customize.click()

    # 3. Scroll window by ('0','1')
    driver.execute_script("window.scrollBy(0,1)")

    # 4. Scroll window by ('0','37')
    driver.execute_script("window.scrollBy(0,37)")

    # 5. Scroll window by ('0','121')
    driver.execute_script("window.scrollBy(0,121)")

    # 6. Scroll window by ('0','91')
    driver.execute_script("window.scrollBy(0,91)")

    # 7. Scroll window by ('0','492')
    driver.execute_script("window.scrollBy(0,492)")

    # 8. Click 'CAMISETA CUSTOM'
    camiseta_custom = driver.find_element(By.XPATH,
                                          "//a[. = '\n\t\t\t\t\t\t\n\t\t\t\t\t\tCAMISETA CUSTOM\n\t\t\n\t\t\t\t\t']")
    camiseta_custom.click()

    # 9. Click 'Agregar Arte'
    # Step switches frame driver context.
    driver.switch_to.default_content()
    driver.switch_to.frame(
        driver.find_element(By.XPATH,
                            "//*[@id = 'tshirtecommerce-designer']|/html/body/div[1]/div[4]/article/div/div/div/div/div/div[1]/div/section[1]/div/div/div/div/div/h4/div/iframe"))
    agregar_arte = driver.find_element(By.XPATH,
                                       "//span[. = 'Agregar Arte']")
    agregar_arte.click()

    # 10. Click 'IMG1'
    # Step switches frame driver context.
    driver.switch_to.default_content()
    driver.switch_to.frame(
        driver.find_element(By.XPATH,
                            "//*[@id = 'tshirtecommerce-designer']|/html/body/div[1]/div[4]/article/div/div/div/div/div/div[1]/div/section[1]/div/div/div/div/div/h4/div/iframe"))
    img1 = driver.find_element(By.XPATH,
                               "//div[1]/a/img")
    img1.click()

    # 11. Click 'black'
    # Step switches frame driver context.
    driver.switch_to.default_content()
    driver.switch_to.frame(
        driver.find_element(By.XPATH,
                            "//*[@id = 'tshirtecommerce-designer']|/html/body/div[1]/div[4]/article/div/div/div/div/div/div[1]/div/section[1]/div/div/div/div/div/h4/div/iframe"))
    black = driver.find_element(By.XPATH,
                                "//div[2]/div/div[1]/div[2]/div/span[2]")
    black.click()

    # 12. Click 'Elige colores'
    # Step switches frame driver context.
    driver.switch_to.default_content()
    driver.switch_to.frame(
        driver.find_element(By.XPATH,
                            "//*[@id = 'tshirtecommerce-designer']|/html/body/div[1]/div[4]/article/div/div/div/div/div/div[1]/div/section[1]/div/div/div/div/div/h4/div/iframe"))
    elige_colores = driver.find_element(By.XPATH,
                                        "//button[. = 'Elige colores']")
    elige_colores.click()

    # 13. Scroll window by ('0','1')
    driver.execute_script("window.scrollBy(0,1)")

    # 14. Scroll window by ('0','158')
    driver.execute_script("window.scrollBy(0,158)")

    # 15. Click 'Back'
    # Step switches frame driver context.
    driver.switch_to.default_content()
    driver.switch_to.frame(
        driver.find_element(By.XPATH,
                            "//*[@id = 'tshirtecommerce-designer']|/html/body/div[1]/div[4]/article/div/div/div/div/div/div[1]/div/section[1]/div/div/div/div/div/h4/div/iframe"))
    back = driver.find_element(By.XPATH,
                               "//span[. = 'Back']")
    back.click()

    # 16. Click 'Agregar texto1'
    # Step switches frame driver context.
    driver.switch_to.default_content()
    driver.switch_to.frame(
        driver.find_element(By.XPATH,
                            "//*[@id = 'tshirtecommerce-designer']|/html/body/div[1]/div[4]/article/div/div/div/div/div/div[1]/div/section[1]/div/div/div/div/div/h4/div/iframe"))
    agregar_texto1 = driver.find_element(By.XPATH,
                                         "//span[. = 'Agregar texto']")
    agregar_texto1.click()

    # 17. Click 'Comprar Ahora'
    # Step switches frame driver context.
    driver.switch_to.default_content()
    driver.switch_to.frame(
        driver.find_element(By.XPATH,
                            "//*[@id = 'tshirtecommerce-designer']|/html/body/div[1]/div[4]/article/div/div/div/div/div/div[1]/div/section[1]/div/div/div/div/div/h4/div/iframe"))
    comprar_ahora = driver.find_element(By.XPATH,
                                        "//button[. = 'Comprar Ahora']")
    comprar_ahora.click()

    # 18. Type 'Javier' in 'billing_first_name'
    billing_first_name = driver.find_element(By.CSS_SELECTOR,
                                             "#billing_first_name")
    billing_first_name.send_keys("Javier")

    # 19. Type 'Martinez Miro' in 'billing_last_name'
    billing_last_name = driver.find_element(By.CSS_SELECTOR,
                                            "#billing_last_name")
    billing_last_name.send_keys("Martinez Miro")

    # 20. Type '666003948' in 'billing_phone'
    billing_phone = driver.find_element(By.CSS_SELECTOR,
                                        "#billing_phone")
    billing_phone.send_keys("666003948")

    # 21. Scroll window by ('0','540')
    driver.execute_script("window.scrollBy(0,540)")

    # 22. Type 'jmmadriddgmail.com' in 'billing_email'
    billing_email = driver.find_element(By.CSS_SELECTOR,
                                        "#billing_email")
    billing_email.send_keys("jmmadriddgmail.com")

    # 23. Scroll window by ('0','-631')
    driver.execute_script("window.scrollBy(0,-631)")

    # 24. Type 'Talla XL ' in 'order_comments'
    order_comments = driver.find_element(By.CSS_SELECTOR,
                                         "#order_comments")
    order_comments.send_keys("Talla XL ")

    # 25. Click 'payment_method'
    payment_method = driver.find_element(By.CSS_SELECTOR,
                                         "#payment_method_ppcp-gateway")
    payment_method.click()
