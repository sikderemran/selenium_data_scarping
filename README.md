# 📰 Google News Headline Scraper

A **simple Python scraper** using **Selenium** and **ChromeDriver** that fetches top headlines from [Google News](https://news.google.com/topstories?hl=en-BN&gl=BN&ceid=BN:en).  
It prints the latest headlines with timestamps every 10 minutes, running continuously.

---

## ✨ Features

- 🔍 Scrapes Google News top headlines 
- ⏰ Prints current time with each scrape  
- ♻️ Runs indefinitely, refreshing headlines every 10 minutes  
- 🚫 Basic exception handling to skip missing elements  
- 📈 Easy to modify for different news categories or intervals

---

## 🧩 Tech Stack

- Python 3.x  
- Selenium WebDriver  
- ChromeDriver  

---

## 🚀 Getting Started

### Prerequisites

- Install [Google Chrome](https://www.google.com/chrome/)  
- Download [ChromeDriver](https://sites.google.com/chromium.org/driver/) compatible with your Chrome version  
- Python 3 and `pip` installed  

### Installation

1. Clone the repo:

```bash
git clone https://github.com/sikderemran/selenium_data_scarping.git
cd google-news-scraper
pip install selenium
python selenium_data_scarping.py

