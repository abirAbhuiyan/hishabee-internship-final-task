import logging
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


# Logging configuration
logging.basicConfig(
    filename="P002_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Starting test: P002 (Attempt to add a purchase entry with missing required fields)")

# Open Chrome
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 15)

# Go to login page
driver.get("https://web.hishabee.business/auth")
logging.info("Opened login page")
time.sleep(5)  # wait 4 page load

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

# Navigate to Purchase
try:
    home_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[.//span[text()='Home']]")))
    home_button.click()
    logging.info("Clicked Home button")

    purchase_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[span[text()='Purchase']]")))
    purchase_button.click()
    logging.info("Navigated to Purchase page")
except Exception as e:
    logging.error(f"Navigation to Purchase failed: {e}")
    driver.quit()
    raise

# Add a new product
time.sleep(10)
try:
    # Find the add product button
    add_button = driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='test'])[1]/following::*[name()='svg'][2]")
    
    # Scroll to the button
    driver.execute_script("arguments[0].scrollIntoView();", add_button)
    logging.info("Scrolled to add button")
    time.sleep(5)
    
    # Hover over the button
    actions = ActionChains(driver)
    actions.move_to_element(add_button).perform()
    logging.info("Hovered over add button")
    time.sleep(1)
    
    # Click the button
    add_button.click()
    logging.info("Clicked add button")
    time.sleep(3)  # Wait 4 form 2 appear
    
    
except Exception as e:
    logging.error(f"Failed to add product: {e}")
    driver.quit()
    exit()

try:
    product_input = driver.find_element(By.XPATH,"//input[@name='product_name']")
    product_input.clear()
    product_input.send_keys("product2")
    logging.info("Typed 'product2' into the product name field.")
except Exception as e:
    logging.error(f"Failed to enter product name: {e}")

try:
    stock_field = wait.until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Current Stock']")))
    stock_field.clear()
    stock_field.send_keys("0")
    logging.info("Entered '0' into Current Stock field successfully.")
except Exception as e:
    logging.error(f"Failed to enter '0' into Current Stock field: {e}")

try:
    purchase_price_field = driver.find_element(By.NAME, "purchase_price")
    purchase_price_field.clear()
    purchase_price_field.send_keys("50")
    logging.info("Successfully entered '50' into Purchase Price field.")
except Exception as e:
    logging.error(f"Failed to enter '50' into Purchase Price field: {e}")

# click "Add New Product" when enabled
try:
    logging.info("Waiting for 'Add New Product' button to be enabled...")
    add_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Add New Product']"))
    )
    add_btn.click()
    logging.info("'Add New Product' button clicked successfully.")
except Exception as e:
    logging.error(f"Failed to click 'Add New Product' button: {e}")


driver.quit()
logging.info("Browser closed")
