# 📧 Email Scraper (Python + Selenium)

This is a Python-based email scraping tool that extracts valid email addresses from dynamic websites using Selenium. The script supports multiple pages (basic crawling) and saves results into a clean CSV file for marketing, research, or lead generation purposes.

---

## 🚀 Features

- ✅ Scrapes emails from dynamic websites using Selenium
- ✅ Supports multiple pages (list of URLs)
- ✅ Automatically removes duplicate emails
- ✅ Saves output to a structured CSV file
- ✅ Easy to modify and extend

---

## 🧰 Technologies Used

- Python 3.10
- Selenium
- ChromeDriver
- Regular Expressions (`re`)
- CSV module

---


---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/scrap-email.git
cd scrap-email

2. Install Dependencies
pip install -r requirements.txt


3. Download ChromeDriver
Download ChromeDriver matching your Chrome version and place it in the project directory or set it in your system PATH.

🧪 How to Use

- Edit the urls list in main.py with the websites you want to scrape.
- Run the script:
    python main.py
- Found emails will be saved in scrap_emails.csv.


📝 Output Format

Email,Source URL
admin@example.com,https://example.com
contact@domain.org,https://domain.org


⚠️ Disclaimer

This tool is intended for educational and ethical use only. Please ensure that the websites you are scraping allow data collection and that your use complies with relevant data protection regulations such as GDPR or CCPA.

🤝 Contributing

Feel free to fork this project and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

