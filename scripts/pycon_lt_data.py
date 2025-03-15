"""
Get some data from pycon.lt website.
https://pycon.lt/robots.txt suggests it is fine to scrape.
Will be an adhoc thing not something regular.
"""

import datetime

import httpx
import pandas as pd
from bs4 import BeautifulSoup

BASE_URL = "https://pycon.lt"


def get_talks_links() -> list[str]:
    response = httpx.get(f"{BASE_URL}/talks/", follow_redirects=True)
    soup = BeautifulSoup(response.text, "html.parser")
    talks_html = soup.find_all("div", class_="card-body p-4")
    links_to_talk_pages = []
    for talk in talks_html:
        link = talk.find("a", class_="btn btn-link btn-sm p-0 text-primary")
        href = link.get("href")
        links_to_talk_pages.append(href)
    print(f"links_to_talk_pages: {links_to_talk_pages}")
    return links_to_talk_pages


def get_title(talk_soup: BeautifulSoup) -> str:
    title = talk_soup.find("h1")
    if title:
        return title.text
    return ""


def get_section(talk_soup: BeautifulSoup, section_heading: str) -> str:
    text = ""
    heading = talk_soup.find("h3", string=section_heading)
    if heading:
        div = heading.find_next("div", class_="prose prose-lg")
        if div:
            para = div.find("p")
            if para:
                text = para.get_text(strip=True)
    return text


def get_talk_details() -> pd.DataFrame:
    talks = get_talks_links()
    talk_details = []
    for talk in talks:
        response = httpx.get(f"{BASE_URL}{talk}", follow_redirects=True)
        soup = BeautifulSoup(response.text, "html.parser")
        title = get_title(soup)
        abstract = get_section(soup, "Abstract")
        description = get_section(soup, "Description")
        prerequisities = get_section(soup, "Prerequisites")
        talk_details.append(
            {"title": title, "abstract": abstract, "description": description, "prerequisites": prerequisities}
        )
    return pd.DataFrame(talk_details)


if __name__ == "__main__":
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H%M%S-")
    filename = f"app/data/{timestamp}-pyconlt-talks.csv"
    talks_df = get_talk_details()
    talks_df.to_csv(filename, index=False)
    print(talks_df)
