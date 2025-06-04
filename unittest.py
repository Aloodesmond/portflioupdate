from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup Chrome options
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
# options.add_argument('--headless')  # Uncomment for headless mode

# Initialize the browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Replace this with your deployed URL
base_url = "https://wondrous-naiad-b131ab.netlify.app/"
print("Starting tests...\n")

try:
    # --- Test Home Page ---
    driver.get(base_url)
    print("Visited Home Page")
    WebDriverWait(driver, 10).until(EC.title_contains("Desmond Portfolio"))
    assert "Desmond Portfolio" in driver.title, "Home page title is incorrect!"

    # --- Test Navigation to About Page ---
    about_link = driver.find_element(By.LINK_TEXT, "About")
    about_link.click()
    print("Navigated to About Page")
    WebDriverWait(driver, 10).until(EC.title_contains("About Me - Desmond"))
    assert "About" in driver.title, "About page title is incorrect!"

    # --- Test Navigation to Experience Page ---
    experience_link = driver.find_element(By.LINK_TEXT, "Experience")
    experience_link.click()
    print("Navigated to Experience Page")
    WebDriverWait(driver, 10).until(EC.title_contains("Job Experience - Desmond"))
    assert "Experience" in driver.title, "Experience page title is incorrect!"

    # --- Test Navigation to Contact Page ---
    contact_link = driver.find_element(By.LINK_TEXT, "Contact")
    contact_link.click()
    print("Navigated to Contact Page")
    WebDriverWait(driver, 10).until(EC.title_contains("Contact Me - Desmond"))
    assert "Contact" in driver.title, "Contact page title is incorrect!"

    # --- Download functionality ---
    download_link = driver.find_element(By.LINK_TEXT, "Download My Resume")
    download_link.click()
    time.sleep(2)  # Allow time for download to start

    # --- Links ---
    linkedin_link = driver.find_element(By.XPATH, '//a[contains(@href, "linkedin.com")]')
    linkedin_link.click()

    # Switch to new tab
    driver.switch_to.window(driver.window_handles[1])
    assert "www.linkedin.com/in/desmond-owiso-792590b8 " in driver.current_url

    # --- Optional: Fill Contact Form ---
    name_field = driver.find_element(By.NAME, "Mary")
    email_field = driver.find_element(By.NAME, "mary jane @gmail.com")
    message_field = driver.find_element(By.NAME, "message me today for more infromation")
    submit_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Send Message')]")

    name_field.send_keys("Test User")
    email_field.send_keys("test@example.com")
    message_field.send_keys("This is a test message from Selenium.")
    print("Filled contact form")

    submit_button.click()
    print("Submitted contact form")

    time.sleep(3)  # Wait for submission feedback if any

    print("\n✅ All tests passed successfully!")

except Exception as e:
    print(f"\n[ERROR] Test failed: {e}")

finally:
    driver.quit()
    print("Browser closed.")