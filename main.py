from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
import argparse
import time
from csv_writer import write_to_csv_lead, write_to_csv_account


CINCOBOT = "Cincobot"

class WebDriverFactory:

    def __init__(self, profile_path=None):
        self.profile_path = profile_path
        self.driver = None

    def create_driver(self):
        try:
            options = webdriver.FirefoxOptions()
            options.add_argument("--headless")

            options.set_preference("general.useragent.override", CINCOBOT)
            if self.profile_path:
                options.profile = self.profile_path
            self.driver = webdriver.Firefox(options=options)

        except ValueError as ve:
            print(f"get_lead_cards error : {ve}")
        except Exception as e:
            print(f"get_lead_cards error : {e}")
            self.driver = None

        return self.driver
    
    def get_account_cards(self):
        try:
            WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, "//div[@data-sn-view-name='account-search-results']"))
            )

            ol_list = driver.find_element(By.CLASS_NAME, "artdeco-list.background-color-white._border-search-results_1igybl")
            cards = ol_list.find_elements(By.XPATH, "//div[@data-x-search-result='ACCOUNT']")

            company_info_list = []

            for card in cards:
                # Company URL
                try:
                    image_tag = card.find_element(By.XPATH, ".//a[@data-control-name='view_company_via_result_image']")
                    image_link = image_tag.get_attribute("href")
                except NoSuchElementException as e:
                    image_link = ""

                # Company Name and Link
                try:
                    name_tag = card.find_element(By.XPATH, ".//a[@data-control-name='view_company_via_result_name']")
                    name_link = name_tag.get_attribute("href")
                    name = name_tag.text
                except NoSuchElementException as e:
                    name_link = ""
                    name = ""
                     
                # Company Industry
                try:
                    industry = card.find_element(By.XPATH, ".//span[@data-anonymize='industry']").text
                except NoSuchElementException as e:
                    industry = ""

                # Company About
                try:                    
                    see_more_button = card.find_element(By.CLASS_NAME, "t-12.button--unstyled.inline-block.t-bold.t-black--light")
                    see_more_button.click()
                    about  = card.find_element(By.CLASS_NAME, 'inline-flex.align-items-baseline').text
                except NoSuchElementException as e:
                    try:
                        about  = card.find_element(By.CLASS_NAME, 'inline-flex.align-items-baseline').text
                    except NoSuchElementException as e:
                        about = ""

                company_info = {
                    'Image URL': image_link,
                    'URL': name_link,
                    'Name': name,
                    'Industry': industry,
                    'About': about,
                }

                company_info_list.append(company_info)

        except NoSuchElementException as e:
            print(f"get_account_cards error : {e}")
            driver.refresh()
            time.sleep(10)
            self.get_account_cards()

        return company_info_list
        

    def get_lead_cards(self):
        try:
            WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.CLASS_NAME, "artdeco-list.background-color-white._border-search-results_1igybl"))
            )

            ol_list = driver.find_element(By.CLASS_NAME, "artdeco-list.background-color-white._border-search-results_1igybl")
            cards = ol_list.find_elements(By.XPATH, "//div[@data-x-search-result='LEAD']")
            
            user_info_list = []
        
            for card in cards:
                # Name & Profile Link
                try:
                    name_tag = card.find_element(By.XPATH, ".//a[@data-control-name='view_lead_panel_via_search_lead_name']")
                    profile_link = name_tag.get_attribute("href")
                    name = name_tag.text
                except NoSuchElementException as e:
                    name = ""
                    profile_link = ""

                # Designation
                try:
                    designation = card.find_element(By.XPATH, ".//span[@data-anonymize='title']").text
                except NoSuchElementException as e:
                    try:
                        designation = card.find_element(By.CLASS_NAME, "artdeco-entity-lockup__subtitle.ember-view.t-14").text
                    except NoSuchElementException as e:
                        designation = ""

                # Company Name and Link
                try:
                    company_tag = card.find_element(By.XPATH, ".//a[@data-anonymize='company-name']")
                    company_link = company_tag.get_attribute("href")
                    company = company_tag.text
                except NoSuchElementException as e:
                    try:
                        company = card.find_element(By.CLASS_NAME, "artdeco-entity-lockup__subtitle.ember-view.t-14").text
                        company_link = ""
                    except NoSuchElementException as e:
                        company = ""
                        company_link = ""


                # Location
                try:
                    location = card.find_element(By.XPATH, ".//span[@data-anonymize='location']").text
                except NoSuchElementException as e:
                    location = ""

                    
                # Time in company and role
                try:
                    time_in_company_role = card.find_element(By.XPATH, ".//div[@data-anonymize='job-title']").text
                except NoSuchElementException as e:
                    time_in_company_role = ""
                    
                # About
                try:                    
                    see_more_button = card.find_element(By.CLASS_NAME, "t-12.button--unstyled.inline-block.t-bold.t-black--light")
                    see_more_button.click()
                    about  = card.find_element(By.CLASS_NAME, 'inline-flex.align-items-baseline').text
                except NoSuchElementException as e:
                    try:
                        about  = card.find_element(By.CLASS_NAME, 'inline-flex.align-items-baseline').text
                    except NoSuchElementException as e:
                        about = ""

                user_info = {
                    'Name': name,
                    'Profile Link': profile_link,
                    'Designation': designation,
                    'Company': company,
                    'Company Link': company_link,
                    'Location': location,
                    'Time in Company and Role': time_in_company_role,
                    'About': about,
                }

                user_info_list.append(user_info)

        except NoSuchElementException as e:
            print(f"get_lead_cards error : {e}")
            driver.refresh()
            time.sleep(10)
            self.get_lead_cards()

        return user_info_list
        

    def scroll_till_end(self, max_scroll_attempts=15, max_retries=3):
        for retry in range(max_retries):
            try:
                scrollable_element = driver.find_element(By.XPATH, "//div[@data-x--search-results-container='']")
                scroll_amount = 400

                i = 1
                while i <= max_scroll_attempts:
                    driver.execute_script("arguments[0].scrollBy(0, arguments[1]);", scrollable_element, scroll_amount)
                    if driver.execute_script("return arguments[0].scrollTop + arguments[0].clientHeight >= arguments[0].scrollHeight;", scrollable_element):
                        return  # Exit the function if scroll is successful
                    i += 1
                    time.sleep(0.5)
            
            except Exception as e:
                print(f"scroll_till_end error: {e}")
                
                if retry < max_retries - 1:
                    print("Retrying after page reload...")
                    driver.refresh()
                    time.sleep(10)
                else:
                    print("Max retries reached. Exiting.")
                    break  

    def close_driver(self):
        if self.driver:
            self.driver.quit()


def parse_arguments():
    parser = argparse.ArgumentParser(description="Selenium WebDriver Factory")
    parser.add_argument("--profile_path", help="Path to a custom profile directory")
    parser.add_argument("--lead_path", help="Path to a linkedin sale navigator leads")
    parser.add_argument("--account_path", help="Path to a linkedin sale navigator accounts")
    return parser.parse_args()

def scrape_lead(driver, webDriver, lead_url):
    try:
        driver.get(lead_url)

        time.sleep(5)

        page = 1 

        webDriver.scroll_till_end()

        user_details = webDriver.get_lead_cards()
        write_to_csv_lead(user_details)

        print(f"Lead - Scraped Page : {page}")

        while True:
            try:
                next_button = driver.find_element(By.XPATH, "//button[@aria-label='Next']")
                if next_button.is_enabled():
                    next_button.click()

                    time.sleep(2)

                    webDriver.scroll_till_end()

                    user_details = webDriver.get_lead_cards()
                    write_to_csv_lead(user_details)

                    page += 1
                    print(f"Lead - Scraped Page : {page}")

                    WebDriverWait(driver, 10).until(EC.staleness_of(next_button))

                else:
                    print("Next button is no longer clickable, pagination finished.")
                    break
                    
            except Exception as e:
                print("No more 'Next' button is clickable or another error occurred:", e)
                driver.refresh()
                time.sleep(25)
                
    except Exception as e:
        print("scrape_lead: driver error: ", e)

    scraping_message = "Lead scraping completed"
    print_decorated_message(scraping_message)

    
def scrape_accounts(driver, webDriver, account_url):
    try:
        driver.get(account_url)

        time.sleep(10)

        page = 1

        webDriver.scroll_till_end()

        company_details = webDriver.get_account_cards()
        write_to_csv_account(company_details)

        print(f"Account - Scraped Page : {page}")

        while True:
            try:
                next_button = driver.find_element(By.XPATH, "//button[@aria-label='Next']")
                if next_button.is_enabled():
                    next_button.click()

                    time.sleep(5)

                    webDriver.scroll_till_end()

                    company_details = webDriver.get_account_cards()
                    write_to_csv_account(company_details)

                    page += 1
                    print(f"Account - Scraped Page : {page}")

                    WebDriverWait(driver, 10).until(EC.staleness_of(next_button))

                else:
                    print("Next button is no longer clickable, pagination finished.")
                    break

            except Exception as e:
                print("No more 'Next' button is clickable or another error occurred:", e)
                driver.refresh()
                time.sleep(25)
        
    except Exception as e:
        print("main: driver error: ", e)

    scraping_message = "Account scraping completed"
    print_decorated_message(scraping_message)

def print_decorated_message(message):
    line = "-" * (len(message) + 4)
    decorated_message = f"\n{line}\n| {message} |\n{line}"
    print(decorated_message)

if __name__ == "__main__":
    args = parse_arguments()

    webDriver = WebDriverFactory(args.profile_path)

    driver = webDriver.create_driver()
    lead_path = args.lead_path
    account_path = args.account_path

    if driver:
        scrape_lead(driver, webDriver, args.lead_path)
        scrape_accounts(driver, webDriver, args.account_path)

    webDriver.close_driver()
