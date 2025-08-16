import logging
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


# Logging configuration
logging.basicConfig(
    filename="S003_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Starting test: S003 (Search Stock Book by item name)")

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

# Navigate to Stock Book
try:
    home_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[.//span[text()='Home']]")))
    home_button.click()
    logging.info("Clicked Home button")
    time.sleep(3)

    stock_book = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//a[@href='/en/stock']//span[text()='Stock Book']"))
    )
    stock_book.click()
    logging.info("Stock Book clicked successfully")
    time.sleep(5)
except (TimeoutException, NoSuchElementException):
    logging.error("Stock Book not found or not clickable")

# Value Enter in Search Box
try:
    wait = WebDriverWait(driver, 10)
    search_box = wait.until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='search']"))
    )
    search_box.clear()
    search_box.send_keys("2")
    logging.info("Value[2] entered in search box successfully")
    time.sleep(3)
except (TimeoutException, NoSuchElementException):
    logging.error("Search box not found")

# Extract product titles from table
try:
    wait = WebDriverWait(driver, 10)
    products = wait.until(
        EC.presence_of_all_elements_located((By.XPATH, "//table//tbody//tr//p[@title]"))
    )

    for product in products:
        logging.info(f"Found product: {product.get_attribute('title')}")

    logging.info("All product titles printed successfully")
except (TimeoutException, NoSuchElementException):
    logging.error("Products not found in the table")




driver.quit()
logging.info("Browser closed")
