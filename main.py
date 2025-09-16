from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import re
import csv

# ======= Configurtion =======
urls = [
    "https://www.dpr.go.id/",
    "https://www.mpr.go.id/"
]
outputs_file = "scrap_emails.csv"
headless_mode = True

# ======= Selenium initialization =======
def start_driver():
    options = Options()
    if headless_mode:
        options.add_argument("--headless")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=options)
    return driver

# ======= Scraping emails =======
def extract_emails_from_page(driver, url):
    try:
        driver.get(url)
        time.sleep(3)

        page_text = driver.find_element(By.TAG_NAME, "body").text

        # Regex Search email
        email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
        emails = re.findall(email_pattern, page_text)
        return list(set(emails))
    except Exception as e:
        print(f"❌ Scraping failed {url}: {e}")
        return []
    
# ======= Save to CSV =======
def save_to_csv(email_data, filename):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Email", "Source URL"])
        for email, source_url in email_data:
            writer.writerow([email, source_url])

# ======= Running Program =======
if __name__ == '__main__':
    driver = start_driver()
    all_emails = []

    for url in urls:
        print(f"🔍 Scraping: {url}")
        emails = extract_emails_from_page(driver, url)
        for email in emails:
            all_emails.append((email, url))

    driver.quit()

    if all_emails:
        save_to_csv(all_emails, outputs_file)
        print(f"\n✅ {len(all_emails)} email successfully saved in {outputs_file}")
    else:
        print("\n⚠️ Not found email.")
