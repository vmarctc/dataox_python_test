from playwright.sync_api import sync_playwright
from sqlalchemy.orm import Session
from datetime import date
import re

from database import engine
from models import Apartment


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        date_pattern = r'^[0-3]?[0-9].[0-3]?[0-9].(?:[0-9]{2})?[0-9]{2}$'
        current_page = 1
        total_pages = 90

        while (current_page <= total_pages):
            page.goto(
                'https://www.kijiji.ca/b-apartments-condos/city-of-toronto'
                '/page-' + str(current_page) + '/c37l1700273', timeout=0)
            search_items = page.query_selector_all('.search-item')

            for item in search_items:
                with Session(bind=engine) as session:

                    if item.query_selector('.image img') is not None:
                        img_url = item.query_selector(
                            '.image img').get_attribute('data-src')
                    else:
                        img_url = 'no image'
                    if item.query_selector('.price') is not None:
                        price = item.query_selector('.price').inner_text()
                    else:
                        price = 'no price'
                    if item.query_selector('.title') is not None:
                        title = item.query_selector('.title').inner_text()
                    else:
                        title = 'no title'
                    if item.query_selector('.date-posted') is not None:
                        date_posted = item.query_selector(
                            '.date-posted').inner_text()
                    else:
                        date_posted = '00/00/0000'
                    if item.query_selector('.location span') is not None:
                        location = item.query_selector(
                            '.location span').inner_text()
                    else:
                        location = 'no information about location'
                    if item.query_selector('.description') is not None:
                        description = item.query_selector(
                            '.description').inner_text()
                    else:
                        description = 'no description'
                    if item.query_selector('.bedrooms') is not None:
                        bedrooms = item.query_selector(
                            '.bedrooms').inner_text()
                    else:
                        bedrooms = 'no information about beds'

                    if not re.match(date_pattern, date_posted):
                        date_posted = date.today().strftime(r'%d/%m/%Y')

                    current_apartment = Apartment(image_url=img_url,
                                                  title=title,
                                                  posted_date=date_posted,
                                                  location=location,
                                                  price=price,
                                                  description=description,
                                                  beds=bedrooms[6:]
                                                  )

                    session.add(current_apartment)
                    session.commit()

            # page.wait_for_timeout(10000)
            current_page += 1

        browser.close()


if __name__ == '__main__':
    main()
