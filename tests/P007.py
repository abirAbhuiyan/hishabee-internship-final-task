import logging
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException


# Logging configuration
logging.basicConfig(
    filename="P007_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Starting test: P007 (Edit an existing purchase entry)")

# Open Chrome
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 15)

# Go to login page
driver.get("https://web.hishabee.business/auth")
logging.info("Opened login page")
time.sleep(5)  # wait 4 page 2 load

# Login
try:
    driver.find_element(By.XPATH, "//input[@placeholder='01XXXXXXXXX (11 digits)']").send_keys("01965039054")
    logging.info("Entered phone number")
    time.sleep(2)

    driver.find_element(By.XPATH, "//button[text()='এগিয়ে যান']").click()
    logging.info("Clicked 'এগিয়ে যান'")
    time.sleep(5)

    driver.find_element(By.ID, "current_password").send_keys("12345")
    logging.info("Entered password")

    driver.find_element(By.XPATH, "//button[text()='লগইন করুন']").click()
    logging.info("Clicked 'লগইন করুন'")
    time.sleep(10)
except Exception as e:
    logging.error(f"Login failed: {e}")
    driver.quit()
    raise

# Select specified shop
try:
    shop_name = "test"
    shop_containers = driver.find_elements(By.XPATH, "//div[contains(@class, 'bg-white') and .//p[@title]]")
    for shop in shop_containers:
        name_element = shop.find_element(By.XPATH, ".//p[@title]")
        if name_element.text.strip() == shop_name:
            button = shop.find_element(By.XPATH, ".//button[p[text()='সিলেক্ট করুন']]")
            button.click()
            logging.info(f"Selected shop: {shop_name}")
            break
    time.sleep(20)
except Exception as e:
    logging.error(f"Shop selection failed: {e}")
    driver.quit()
    raise

# Set language to English
try:
    time.sleep(10)
    driver.find_element(By.XPATH, "//a[@href='/settings/lang']").click()
    time.sleep(2)
    language_dropdown = driver.find_element(By.XPATH, "//select")
    select = Select(language_dropdown)
    select.select_by_visible_text("English")
    driver.find_element(By.XPATH, "//button[text()='সেভ করুন']").click()
    logging.info("Language set to English")
except Exception as e:
    logging.error(f"Language selection failed: {e}")
    driver.quit()
    raise

# Navigate to Product List
try:
    home_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[.//span[text()='Home']]")))
    home_button.click()
    logging.info("Clicked Home button")

    purchase_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[span[text()='Product List']]")))
    purchase_button.click()
    logging.info("Navigated to Product List page")
except Exception as e:
    logging.error(f"Navigation to Product List failed: {e}")
    driver.quit()
    raise

try:
    # Wait for the row containing product1 to be clickable
    row = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//p[@title='product1']/ancestor::tr"))
    )
    
    # Scroll into view
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", row)
    
    # Click the row
    row.click()
    logging.info("Clicked the row for product1 successfully")
except Exception as e:
    logging.error(f"Failed to click the row for product1: {e}")
    driver.quit()
    raise

try:
    time.sleep(10)
    driver.find_element(By.XPATH, "//button[normalize-space(.)='Update Stock']").click()
    logging.info("Clicked 'Update Stock' button successfully")
except Exception as e:
    logging.error(f"Failed to click 'Update Stock' button: {e}")
    driver.quit()
    raise

try:
    # Locate the input field
    stock_input = wait.until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='number' and contains(@class,'text-center')]"))
    )
    
    # Read the initial value
    initial_value = stock_input.get_attribute("value")
    logging.info(f"Initial stock value: {initial_value}")

    # Clear the field and set new value
    stock_input.clear()
    stock_input.send_keys("11000")
    logging.info("Updated stock value to 11000")

except Exception as e:
    logging.error(f"Failed to read/update stock value: {e}")
    driver.quit()
    raise

try:
    driver.find_element(By.XPATH, "//button[normalize-space(.)='Update Stock']").click()
    logging.info("Clicked 'Update Stock' button successfully")
except Exception as e:
    logging.error(f"Failed to click 'Update Stock' button: {e}")
    driver.quit()
    raise

try:
    stock_input = wait.until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='number' and contains(@class,'text-center')]"))
    )
    current_value = stock_input.get_attribute("value")
    if current_value == "11000":
        logging.info("Stock value updated correctly to 11000")
    else:
        logging.error(f"Stock value is incorrect. Current value: {current_value}")
except Exception as e:
    logging.error(f"Failed to read or verify stock value: {e}")
    driver.quit()
    raise


driver.quit()
logging.info("Browser closed")
