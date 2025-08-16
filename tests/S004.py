import logging
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException


# Logging configuration
logging.basicConfig(
    filename="S004_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Starting test: S004 (Update stock after a purchase)")

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
    wait = WebDriverWait(driver, 10)
    search_box = wait.until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='search']"))
    )
    search_box.clear()
    search_box.send_keys("product2")
    logging.info("Searched for 'product2' successfully")
except (TimeoutException, NoSuchElementException) as e:
    logging.error(f"Search box not found or interaction failed: {e}")

try:
    wait = WebDriverWait(driver, 10)
    # Find the row containing product2
    product_row = wait.until(
        EC.presence_of_element_located((By.XPATH, "//table//tbody//tr[td//p[@title='product2']]"))
    )

    # Now fetch the stock column
    stock_cell = product_row.find_element(By.XPATH, "./td[2]")
    stock_value = stock_cell.text.strip()
    logging.info(f"Current stock of product2: {stock_value}")

except (TimeoutException, NoSuchElementException) as e:
    logging.error(f"Failed to fetch current stock for product2: {e}")

try:
    time.sleep(5)
    purchase_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[span[text()='Purchase']]")))
    purchase_button.click()
    logging.info("Navigated to Purchase page")
    time.sleep(5)
except Exception as e:
    logging.error(f"Navigation to Purchase failed: {e}")
    driver.quit()
    raise

try:
    time.sleep(5)
    search_field = wait.until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='search']"))
    )
    logging.info("Search field located successfully.")

    # clear any old text and type "product2"
    search_field.clear()    
    search_field.send_keys("product2")
    logging.info("Entered 'product2' in the search field.")

except TimeoutException:
    logging.error("Search field not found within the given time.")

try:
    # Locate the product2 container
    product_container = wait.until(
        EC.presence_of_element_located((By.XPATH, "//p[@title='product2']/ancestor::div[@class='flex items-center gap-space12 justify-between py-space8 px-space8 shadow my-1.5']"))
    )
    logging.info("Located product2 container.")

    # Locate the Add button inside the same container
    add_button = product_container.find_element(By.XPATH, ".//button[contains(text(), 'Add')]")
    logging.info("Found Add button for product2.")

    # Click the Add button
    add_button.click()
    logging.info("Clicked the Add button for product2 successfully.")

except Exception as e:
    logging.error(f"Failed to click Add button for product2: {e}")

cash_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Cash']")))
cash_button.click()
logging.info("Clicked Cash button")

amount_received_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Amount Received']")))
amount_received_button.click()
logging.info("Clicked Amount Received button")

wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "div.flex.justify-center.items-center.fixed")))
logging.info("Overlay disappeared")

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
    wait = WebDriverWait(driver, 10)
    search_box = wait.until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='search']"))
    )
    search_box.clear()
    search_box.send_keys("product2")
    logging.info("Searched for 'product2' successfully")
except (TimeoutException, NoSuchElementException) as e:
    logging.error(f"Search box not found or interaction failed: {e}")

try:
    wait = WebDriverWait(driver, 10)
    # Find the row containing product2
    product_row = wait.until(
        EC.presence_of_element_located((By.XPATH, "//table//tbody//tr[td//p[@title='product2']]"))
    )

    # Now fetch the stock column (2nd <td>)
    stock_cell = product_row.find_element(By.XPATH, "./td[2]")
    stock_value = stock_cell.text.strip()
    logging.info(f"Current stock of product2: {stock_value}")

except (TimeoutException, NoSuchElementException) as e:
    logging.error(f"Failed to fetch current stock for product2: {e}")




driver.quit()
logging.info("Browser closed")