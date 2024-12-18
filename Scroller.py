from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time


def scroll_page(driver):
    # Scroll down partially
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight / 5);")  # Scroll down
    time.sleep(2)  # Pause for 2 seconds

    # Scroll down completely
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight / 5);")  # Scroll to the bottom
    time.sleep(2)  # Pause for 2 seconds

    # Scroll back up to the middle
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight / 5);")  # Scroll up
    time.sleep(2)  # Pause for 2 seconds

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight / 5);")  # Scroll to the top
    time.sleep(2)  # Pause for 2 seconds

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight / 5);")  # Scroll down
    time.sleep(2)  # Pause for 2 seconds


    # Scroll to the top for 30 seconds
    start_time = time.time()
    while time.time() - start_time < 30:  # Scroll for 30 seconds
        driver.execute_script("window.scrollTo(0, 0);")  # Scroll to the top
        time.sleep(1)  # Wait for 1 second

def monitor_with_selenium(url):
    # Initialize the WebDriver (make sure ChromeDriver is in your PATH)
    driver = webdriver.Chrome()
    
    try:
        driver.get(url)  # Open the specified URL
        
        # Call the scrolling function
        scroll_page(driver)
        
        print(f"{url} was stable and scrolled for 30 seconds.")
    
    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        driver.quit()  # Close the browser

# Example usage
monitor_with_selenium('https://example.com')