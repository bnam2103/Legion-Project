from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import undetected_chromedriver as uc

import time


# Map site names to their URLs
SITE_URLS = {
    "youtube": "https://www.youtube.com",
    "soundcloud": "https://www.soundcloud.com",
    "google": "https://www.google.com",
    "facebook": "https://www.facebook.com",
    "google docs": "https://docs.google.com/document/u/0/",
    "gmail": "https://mail.google.com/mail/u/0/#inbox"
}

# def login_google(driver, email, password):
#     driver.get("https://accounts.google.com/signin")

#     wait = WebDriverWait(driver, 15)

#     try:
#         # Enter email
#         email_input = wait.until(EC.presence_of_element_located((By.ID, "identifierId")))
#         email_input.send_keys(email)
#         driver.find_element(By.ID, "identifierNext").click()

#         # Wait for password input (can take time!)
#         password_input = wait.until(EC.presence_of_element_located((By.NAME, "password")))
#         password_input.send_keys(password)
#         driver.find_element(By.ID, "passwordNext").click()
#         print("Submitted login.")

#     except Exception as e:
#         print("Login failed:", e)

def open_website_or_search(site_name):
    site_name = site_name.lower().strip()

    chrome_driver_path = r"C:\Users\Nam\Desktop\Legion 1.0\chromedriver-win64\chromedriver.exe"  
    """Can't sign in"""
    options = uc.ChromeOptions()

    # options.add_argument(r"user-data-dir=C:\Users\Nam\AppData\Local\Google\Chrome\User Data")
    # options.add_argument(r"profile-directory=Profile 1")

    # options.add_argument("--disable-blink-features=AutomationControlled")
    # options.add_experimental_option("excludeSwitches", ["enable-automation"])
    # options.add_experimental_option('useAutomationExtension', False)

    service = Service(chrome_driver_path)
    driver = uc.Chrome(service=service, options=options)
    # login_google(driver, "nedvip2004@gmail.com", "0938469537a")
    url = SITE_URLS.get(site_name)

    if url:
        # Open the direct URL
        driver.get(url)
        print(f"Opening {site_name}...")
    else:
        # Open Google and search the site_name
        driver.get("https://www.google.com")
        print(f"Searching for '{site_name}' on Google...")

        # Find the search box, enter query, press Enter
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys(site_name + Keys.RETURN)

    print("Waiting for you to close the browser...")
    
    try:
        while True:
            driver.title  # Try accessing the browser — will raise error if closed
            time.sleep(1)
    except WebDriverException:
        print("Browser was closed. Exiting.")

# open_website_or_search("attack on titan")