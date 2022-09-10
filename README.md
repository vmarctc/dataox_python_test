# dataox_python_test
Junior Python test for DATAOX company.

From the website, https://www.kijiji.ca/b-apartments-condos/city-of-toronto/c37l1700273 collected all ads, includes pagination. 
From each ad, I collected the following points:
- image url
- title
- posted date
- location
- number of beds
- description
- price

Information from the website was collected with the help of Playwright. The database structure and interaction with it is described using SQLAlchemy. Used PostgreSQL to store the parsed data.
