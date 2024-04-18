from bs4 import BeautifulSoup
import requests


def find_jobs():
    html_text = requests.get(
        "https://www.naukri.com/machine-learning-engineer-jobs-in-india"
    )

    print(html_text.text)
    soup = BeautifulSoup(html_text, "html.parser")
    page_soup = soup.find_all("div", class_="srp-jobtuple-wrapper")


if __name__ == "__main__":
    find_jobs()
