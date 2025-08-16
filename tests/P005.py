import logging
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException


# Logging configuration
logging.basicConfig(
    filename="P005_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Starting test: P005 (Add large quantity purchase (e.g., 10,000 units))")

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

# Add product
try:
    add_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Add']")))
    add_button.click()
    logging.info("Clicked Add button")

    # Quantity
    quantity_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Quantity']")))
    quantity_input.clear()
    quantity_input.send_keys("10000")
    logging.info("Set Quantity to 10k")

    # Unit Price
    price_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Unit Price']")))
    price_input.clear()
    price_input.send_keys("10000")
    logging.info("Set Unit Price to 10k")

    # Cash button
    cash_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Cash']")))
    cash_button.click()
    logging.info("Clicked Cash button")

    # Amount Received
    amount_received_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Amount Received']")))
    amount_received_button.click()
    logging.info("Clicked Amount Received button")

    # Wait for overlay to disappear
    wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "div.flex.justify-center.items-center.fixed")))
    logging.info("Overlay disappeared")

    # Close button
    try:
        # Retry locating the button until it is clickable
        for attempt in range(3):
            try:
                close_button = wait.until(
                    EC.element_to_be_clickable((By.XPATH, "//button[./span[text()='Close']]"))
                )
                driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", close_button)
                close_button.click()
                logging.info("Clicked Close button successfully")
                break
            except StaleElementReferenceException:
                logging.warning(f"Stale element, retrying... attempt {attempt + 1}")
                time.sleep(1)
    except Exception as e:
        logging.error(f"Failed to click Close button: {e}")
        driver.quit()
        raise
except Exception as e:
    logging.error(f"Purchase test failed: {e}")
    driver.quit()
    raise

driver.quit()
logging.info("Browser closed")
