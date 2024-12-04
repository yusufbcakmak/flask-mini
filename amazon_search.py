from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import sys

def search_amazon(search_term):
    # Initialize the Chrome driver
    driver = webdriver.Chrome()

    # Open Amazon website
    driver.get("https://www.amazon.com.tr")
    # Find the search box
    search_box = driver.find_element(By.ID, "twotabsearchtextbox")

    search_box.send_keys(search_term)

    # Submit the search
    search_box.send_keys(Keys.RETURN)

    # Wait for the results to load
    time.sleep(5)

    # Collect all products
    all_products = driver.find_elements(By.XPATH, "//div[@data-component-type='s-search-result']")
    sponsored_products = []
    regular_products = []

    products_result = []

    for product in all_products:
        try:
            product.find_element(By.XPATH, ".//span[contains(text(), 'Sponsorlu')]")
            sponsored_products.append(product)
        except:
            regular_products.append(product)

    for product in sponsored_products:
        try:
            product_link = product.find_element(By.XPATH, ".//a[@class='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal']").get_attribute("href")
            product_title = product.find_element(By.XPATH, ".//span[@class='a-size-base-plus a-color-base a-text-normal']").text
            products_result.append({"title": product_title, "link": product_link, "sponsored": True})
        except:
            continue

    for product in regular_products:
        try:
            product_title = product.find_element(By.XPATH, ".//span[@class='a-size-base-plus a-color-base a-text-normal']").text
            product_link = product.find_element(By.XPATH, ".//a[@class='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal']").get_attribute("href")
            products_result.append({"title": product_title, "link": product_link, "sponsored": False})
        except:
            continue

    # Close the browser
    driver.quit()
    return products_result

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python amazon_search.py <keyword>")
        sys.exit(1)
    
    keyword = sys.argv[1]
    search_amazon(keyword)
