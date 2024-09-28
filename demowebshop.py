import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class DemoWebShop(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_1_page_title_regist(self):
        driver = self.driver
        driver.get("https://demowebshop.tricentis.com/register")
        self.assertIn("Register", driver.title)

    def  test_2_chek_error_email_regist(self):
        driver = self.driver
        driver.get("https://demowebshop.tricentis.com/register")
     
        driver.find_element(By.XPATH, "//input[@id='FirstName']").send_keys('Akram')
        driver.find_element(By.XPATH, "//input[@id='LastName']").send_keys('Yahya')
        driver.find_element(By.XPATH, "//input[@id='Password']").send_keys('123456')
        driver.find_element(By.XPATH, "//input[@id='ConfirmPassword']").send_keys('123456')
        driver.find_element(By.XPATH, "//input[@id='register-button']").click()
        
        error_msg = driver.find_element(By.XPATH, "//span[@for='Email']").text
        self.assertIn("Email is required.", error_msg)

    def  test_3_chek_error_password_regist(self):
        driver = self.driver
        driver.get("https://demowebshop.tricentis.com/register")
     
        driver.find_element(By.XPATH, "//input[@id='FirstName']").send_keys('Akram')
        driver.find_element(By.XPATH, "//input[@id='LastName']").send_keys('Yahya')
        driver.find_element(By.XPATH, "//input[@id='Email']").send_keys('akram@yahoo.com')
        driver.find_element(By.XPATH, "//input[@id='register-button']").click()
        
        error_msg = driver.find_element(By.XPATH, "//span[@for='Password']").text
        self.assertIn("Password is required.", error_msg)

        error_msg = driver.find_element(By.XPATH, "//span[@for='ConfirmPassword']").text
        self.assertIn("Password is required.", error_msg)

    def test_4_check_success_login_registration(self):
        driver = self.driver
        driver.get("https://demowebshop.tricentis.com/register")

        first_name = 'Akram'
        last_name = 'Yahya'
        email = 'akram@yahoo.com'
        password = '123456'

        driver.find_element(By.XPATH, "//input[@id='FirstName']").send_keys(first_name)
        driver.find_element(By.XPATH, "//input[@id='LastName']").send_keys(last_name)
        driver.find_element(By.XPATH, "//input[@id='Email']").send_keys(email)
        driver.find_element(By.XPATH, "//input[@id='Password']").send_keys(password)
        driver.find_element(By.XPATH, "//input[@id='ConfirmPassword']").send_keys(password)
        driver.find_element(By.XPATH, "//input[@id='register-button']").click()

        success_message = "Your registration completed"
        driver.get("https://demowebshop.tricentis.com/registerresult/1")
        
        success_element = driver.find_element(By.XPATH, "//div[@class='result']")
        self.assertIn(success_message, success_element.text)

    def test_5_check_success_login(self):
        driver = self.driver
        driver.get("https://demowebshop.tricentis.com/login")

        email = 'akram@yahoo.com'
        password = '123456'

        driver.find_element(By.ID, "Email").send_keys(email)
        driver.find_element(By.ID, "Password").send_keys(password)
        driver.find_element(By.ID, "RememberMe").click()
        driver.find_element(By.XPATH, "//input[@value='Log in']").click()

        success_login=driver.find_element(By.XPATH, "//a[normalize-space()='akram@yahoo.com']").text
        self.assertIn("akram@yahoo.com", success_login)

        get_url=driver.current_url
        self.assertIn('https://demowebshop.tricentis.com/', get_url)

    def test_6_check_failed_login_wrong_password(self):
        driver = self.driver
        driver.get("https://demowebshop.tricentis.com/login")

        email = 'akram@yahoo.com'
        password = '12345'

        driver.find_element(By.ID, "Email").send_keys(email)
        driver.find_element(By.ID, "Password").send_keys(password)
        driver.find_element(By.ID, "RememberMe").click()
        driver.find_element(By.XPATH, "//input[@value='Log in']").click()

        error_msg = driver.find_element(By.CSS_SELECTOR, ".validation-summary-errors").text
        self.assertIn("Login was unsuccessful. Please correct the errors and try again.", error_msg)
        self.assertIn("The credentials provided are incorrect", error_msg)

    def test_7_check_failed_login_wrong_email(self):
        driver = self.driver
        driver.get("https://demowebshop.tricentis.com/login")

        email = 'akram1@yahoo.com'
        password = '123456'

        driver.find_element(By.ID, "Email").send_keys(email)
        driver.find_element(By.ID, "Password").send_keys(password)
        driver.find_element(By.ID, "RememberMe").click()
        driver.find_element(By.XPATH, "//input[@value='Log in']").click()

        error_msg = driver.find_element(By.CSS_SELECTOR, ".validation-summary-errors").text
        self.assertIn("Login was unsuccessful. Please correct the errors and try again.", error_msg)
        self.assertIn("No customer account found", error_msg)

    def test_8_chek_error_empty_email_password(self):
        driver = self.driver
        driver.get("https://demowebshop.tricentis.com/login")

        driver.find_element(By.ID, "RememberMe").click()
        driver.find_element(By.XPATH, "//input[@value='Log in']").click()

        error_msg = driver.find_element(By.CSS_SELECTOR, ".validation-summary-errors").text
        self.assertIn("Login was unsuccessful. Please correct the errors and try again.", error_msg)
        self.assertIn("No customer account found", error_msg)

    def test_9_Success_add_to_cart (self):
        driver = self.driver
        driver.get("https://demowebshop.tricentis.com/login")

        email = 'akram@yahoo.com'
        password = '123456'

        driver.find_element(By.ID, "Email").send_keys(email)
        driver.find_element(By.ID, "Password").send_keys(password)
        driver.find_element(By.ID, "RememberMe").click()
        driver.find_element(By.XPATH, "//input[@value='Log in']").click()
        driver.find_element(By.XPATH, "//div[@class='product-item']//img[@title='Show details for 14.1-inch Laptop']").click()
        
        get_url = driver.current_url
        self.assertIn('https://demowebshop.tricentis.com/141-inch-laptop', get_url)

        driver.find_element(By.XPATH, "//input[@id='add-to-cart-button-31']").click()
        driver.find_element(By.XPATH, "//li[@id='topcartlink']//a[@class='ico-cart']").click()

        get_url2 = driver.current_url
        self.assertIn('https://demowebshop.tricentis.com/cart', get_url2)

    def test_10_Success_add_to_cart (self):
        driver = self.driver
        driver.get("https://demowebshop.tricentis.com/login")

        email = 'akram@yahoo.com'
        password = '123456'

        driver.find_element(By.ID, "Email").send_keys(email)
        driver.find_element(By.ID, "Password").send_keys(password)
        driver.find_element(By.ID, "RememberMe").click()
        driver.find_element(By.XPATH, "//input[@value='Log in']").click()
        driver.find_element(By.XPATH, "//div[@class='product-grid home-page-product-grid']//div[3]//div[1]//div[2]//div[3]//div[2]//input[1]").click()
        
        get_url3 = driver.current_url
        self.assertIn('https://demowebshop.tricentis.com/', get_url3)

        driver.find_element(By.XPATH, "//span[normalize-space()='Shopping cart']").click()

        get_url4 = driver.current_url
        self.assertIn('https://demowebshop.tricentis.com/cart', get_url4)

    def test_11_Success_checkout(self):
        driver = self.driver
        driver.get("https://demowebshop.tricentis.com/login")

        email = 'akram@yahoo.com'
        password = '123456'

        driver.find_element(By.ID, "Email").send_keys(email)
        driver.find_element(By.ID, "Password").send_keys(password)
        driver.find_element(By.ID, "RememberMe").click()
        driver.find_element(By.XPATH, "//input[@value='Log in']").click()
        driver.find_element(By.XPATH, "//div[@class='product-grid home-page-product-grid']//div[3]//div[1]//div[2]//div[3]//div[2]//input[1]").click()
        driver.find_element(By.ID, "topcartlink").click() 
        
        get_url5 = driver.current_url
        self.assertIn('https://demowebshop.tricentis.com/cart', get_url5) 
        
        driver.find_element(By.ID, "termsofservice").click()
        driver.find_element(By.XPATH, "//button[@id='checkout']").click()

        
        get_url6 = driver.current_url
        self.assertIn('https://demowebshop.tricentis.com/onepagecheckout', get_url6)


    def test_12_success_checkout (self):
        driver = self.driver
        driver.get("https://demowebshop.tricentis.com/")
        driver.maximize_window()
        driver.find_element(By.XPATH, "//a[@class='ico-login']").click()
        driver.find_element(By.XPATH, "/html//input[@id='Email']").send_keys('akram@yahoo.com')
        driver.find_element(By.XPATH, "//input[@id='Password']").send_keys('123456')
        driver.find_element(By.XPATH, "//input[@value='Log in']").click()
        driver.find_element(By.XPATH, "//div[@class='product-grid home-page-product-grid']//div[3]//div[1]//div[2]//div[3]//div[2]//input[1]").click() 
        driver.find_element(By.XPATH, "//li[@id='topcartlink']//a[@class='ico-cart']").click()
        driver.find_element(By.CLASS_NAME, "qty-input").clear()
        driver.find_element(By.CLASS_NAME, "qty-input").send_keys(1)
        driver.find_element(By.XPATH, "//input[@name='updatecart']").click()
        driver.find_element(By.XPATH, "//input[@id='termsofservice']").click()
        driver.find_element(By.XPATH, "//button[@id='checkout']").click()
        driver.find_element(By.XPATH, "//input[@onclick='Billing.save()']").click()
        driver.implicitly_wait(3)
        driver.find_element(By.XPATH, "//input[@onclick='Shipping.save()']").click()
        driver.implicitly_wait(3)
        driver.find_element(By.XPATH, "//input[@class='button-1 shipping-method-next-step-button']").click()
        driver.implicitly_wait(3)
        driver.find_element(By.XPATH, "//input[@class='button-1 payment-method-next-step-button']").click()
        driver.implicitly_wait(3)
        driver.find_element(By.XPATH, "//input[@class='button-1 payment-info-next-step-button']").click() 
        driver.implicitly_wait(5)
        driver.find_element(By.XPATH, "//input[@value='Confirm']").click()
        time.sleep(5)


        
        thankyou_text = driver.find_element(By.XPATH,"/html/body/div[4]/div[1]/div[4]/div/div/div[1]/h1").text

        print(f"message yang diambil:{thankyou_text}")

        self.assertIn("Thank you", thankyou_text)

        time.sleep(5)





    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()