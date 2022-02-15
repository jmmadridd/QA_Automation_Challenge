from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from src.testproject.classes import DriverStepSettings, StepSettings
from src.testproject.decorator import report_assertion_errors
from src.testproject.enums import SleepTimingType
from src.testproject.sdk.drivers import webdriver
import pytest


"""
    Project: QA Automation Challenge
    Test: Comprar camiseta
    Author: Javier Martinez (jmmadridd@gmail.com)
"""


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(token="mMSlzTkBQJ8CEKkRB8AtftI9NhxgoAHZXi9YSfDTDTg1",
                              project_name="My first Project",
                              job_name="Comprar camiseta")
    step_settings = StepSettings(timeout=15000,
                                 sleep_time=500,
                                 sleep_timing_type=SleepTimingType.Before)
    with DriverStepSettings(driver, step_settings):
        yield driver
    driver.quit()


@report_assertion_errors
def test_main(driver):
    """Comprar camiseta"""
    # Test Parameters
    # Auto generated application URL parameter
    ApplicationURL = "https://salvajerealbrand.com"

    # 1. Navigate to '{ApplicationURL}'
    # Navigates the specified URL (Auto-generated)
    driver.get(f'{ApplicationURL}')

    # 2. Click 'TIENDA'
    tienda = driver.find_element(By.XPATH,
                                 "//section[1]/div/div[2]/div/div/div/nav[1]//a[. = 'Tienda']")
    tienda.click()

    # 3. Scroll window by ('0','65')
    driver.execute_script("window.scrollBy(0,65)")

    # 4. Click 'Camiseta Thinking Eyes'
    camiseta_thinking_eyes = driver.find_element(By.XPATH,
                                                 "//h2[. = 'Camiseta Thinking Eyes']")
    camiseta_thinking_eyes.click()

    # 5. Click 'attribute_pa_talla'
    attribute_pa_talla = driver.find_element(By.CSS_SELECTOR,
                                             "#pa_talla")
    attribute_pa_talla.click()

    # 6. Select the 'xl' option in 'attribute_pa_talla'
    attribute_pa_talla = driver.find_element(By.CSS_SELECTOR,
                                             "#pa_talla")
    Select(attribute_pa_talla).select_by_value("xl")

    # 7. Click 'attribute_pa_talla'
    attribute_pa_talla = driver.find_element(By.CSS_SELECTOR,
                                             "#pa_talla")
    attribute_pa_talla.click()

    # 8. Click 'Añadir al carrito'
    a_adir_al_carrito = driver.find_element(By.XPATH,
                                            "//button[. = 'Añadir al carrito']")
    a_adir_al_carrito.click()

    # 9. Click 'Ver carrito'
    ver_carrito = driver.find_element(By.XPATH,
                                      "//a[. = 'Ver carrito']")
    ver_carrito.click()

    # 10. Click 'billing_first_name'
    billing_first_name = driver.find_element(By.CSS_SELECTOR,
                                             "#billing_first_name")
    billing_first_name.click()

    # 11. Type 'Javier ' in 'billing_first_name'
    billing_first_name = driver.find_element(By.CSS_SELECTOR,
                                             "#billing_first_name")
    billing_first_name.send_keys("Javier ")

    # 12. Type 'Martinez Miro' in 'billing_last_name'
    billing_last_name = driver.find_element(By.CSS_SELECTOR,
                                            "#billing_last_name")
    billing_last_name.send_keys("Martinez Miro")

    # 13. Click 'España'
    espa_a = driver.find_element(By.CSS_SELECTOR,
                                 "#select2-billing_country-container")
    espa_a.click()

    # 14. Click 'billing_address_1'
    billing_address_1 = driver.find_element(By.CSS_SELECTOR,
                                            "#billing_address_1")
    billing_address_1.click()

    # 15. Type 'Calle Venius 16' in 'billing_address_1'
    billing_address_1 = driver.find_element(By.CSS_SELECTOR,
                                            "#billing_address_1")
    billing_address_1.send_keys("Calle Venius 16")

    # 16. Click 'billing_postcode'
    billing_postcode = driver.find_element(By.CSS_SELECTOR,
                                           "#billing_postcode")
    billing_postcode.click()

    # 17. Type '28224' in 'billing_postcode'
    billing_postcode = driver.find_element(By.CSS_SELECTOR,
                                           "#billing_postcode")
    billing_postcode.send_keys("28224")

    # 18. Click 'billing_city'
    billing_city = driver.find_element(By.CSS_SELECTOR,
                                       "#billing_city")
    billing_city.click()

    # 19. Click 'billing_city'
    billing_city = driver.find_element(By.CSS_SELECTOR,
                                       "#billing_city")
    billing_city.click()

    # 20. Type 'Pozuelo de Alarcon ' in 'billing_city'
    billing_city = driver.find_element(By.CSS_SELECTOR,
                                       "#billing_city")
    billing_city.send_keys("Pozuelo de Alarcon ")

    # 21. Click 'billing_phone'
    billing_phone = driver.find_element(By.CSS_SELECTOR,
                                        "#billing_phone")
    billing_phone.click()

    # 22. Scroll window by ('0','485')
    driver.execute_script("window.scrollBy(0,485)")

    # 23. Type '666003948' in 'billing_phone'
    billing_phone = driver.find_element(By.CSS_SELECTOR,
                                        "#billing_phone")
    billing_phone.send_keys("666003948")

    # 24. Click 'billing_email'
    billing_email = driver.find_element(By.CSS_SELECTOR,
                                        "#billing_email")
    billing_email.click()

    # 25. Scroll window by ('0','260')
    driver.execute_script("window.scrollBy(0,260)")

    # 26. Scroll window by ('0','959')
    driver.execute_script("window.scrollBy(0,959)")

    # 27. Type 'jmmadriddgmail.com' in 'billing_email'
    billing_email = driver.find_element(By.CSS_SELECTOR,
                                        "#billing_email")
    billing_email.send_keys("jmmadriddgmail.com")

    # 28. Click 'number'
    # Step switches frame driver context.
    driver.switch_to.default_content()
    driver.switch_to.frame(
        driver.find_element(By.XPATH,
                            "//*[@name = '__privateStripeFrame41225']|/html/body/div[1]/div[4]/article/div/div/div/div/div/div[1]/div/section[2]/div/div/div/div/div/div/form/div[3]/div[1]/ul/li[1]/div/fieldset/div[1]/div/iframe"))
    number = driver.find_element(By.CSS_SELECTOR,
                                 "#Field-numberInput")
    number.click()

    # 29. Type '1234 1234 1234 1234' in 'number'
    # Step switches frame driver context.
    driver.switch_to.default_content()
    driver.switch_to.frame(
        driver.find_element(By.XPATH,
                            "//*[@name = '__privateStripeFrame41225']|/html/body/div[1]/div[4]/article/div/div/div/div/div/div[1]/div/section[2]/div/div/div/div/div/div/form/div[3]/div[1]/ul/li[1]/div/fieldset/div[1]/div/iframe"))
    number = driver.find_element(By.CSS_SELECTOR,
                                 "#Field-numberInput")
    number.send_keys("1234 1234 1234 1234")

    # 30. Click 'expiry'
    # Step switches frame driver context.
    driver.switch_to.default_content()
    driver.switch_to.frame(
        driver.find_element(By.XPATH,
                            "//*[@name = '__privateStripeFrame41225']|/html/body/div[1]/div[4]/article/div/div/div/div/div/div[1]/div/section[2]/div/div/div/div/div/div/form/div[3]/div[1]/ul/li[1]/div/fieldset/div[1]/div/iframe"))
    expiry = driver.find_element(By.CSS_SELECTOR,
                                 "#Field-expiryInput")
    expiry.click()

    # 31. Type '09 / 23' in 'expiry'
    # Step switches frame driver context.
    driver.switch_to.default_content()
    driver.switch_to.frame(
        driver.find_element(By.XPATH,
                            "//*[@name = '__privateStripeFrame41225']|/html/body/div[1]/div[4]/article/div/div/div/div/div/div[1]/div/section[2]/div/div/div/div/div/div/form/div[3]/div[1]/ul/li[1]/div/fieldset/div[1]/div/iframe"))
    expiry = driver.find_element(By.CSS_SELECTOR,
                                 "#Field-expiryInput")
    expiry.send_keys("09 / 23")

    # 32. Click 'cvc'
    # Step switches frame driver context.
    driver.switch_to.default_content()
    driver.switch_to.frame(
        driver.find_element(By.XPATH,
                            "//*[@name = '__privateStripeFrame41225']|/html/body/div[1]/div[4]/article/div/div/div/div/div/div[1]/div/section[2]/div/div/div/div/div/div/form/div[3]/div[1]/ul/li[1]/div/fieldset/div[1]/div/iframe"))
    cvc = driver.find_element(By.CSS_SELECTOR,
                              "#Field-cvcInput")
    cvc.click()

    # 33. Type '123' in 'cvc'
    # Step switches frame driver context.
    driver.switch_to.default_content()
    driver.switch_to.frame(
        driver.find_element(By.XPATH,
                            "//*[@name = '__privateStripeFrame41225']|/html/body/div[1]/div[4]/article/div/div/div/div/div/div[1]/div/section[2]/div/div/div/div/div/div/form/div[3]/div[1]/ul/li[1]/div/fieldset/div[1]/div/iframe"))
    cvc = driver.find_element(By.CSS_SELECTOR,
                              "#Field-cvcInput")
    cvc.send_keys("123")
