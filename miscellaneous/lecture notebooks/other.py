from requests_html import HTMLSession
from selectolax.parser import HTMLParser

def show_me_the_money():
  url = "https://www.usaspending.gov/agency/department-of-defense?fy=2023"
  
  session = HTMLSession()
  
  response = session.get(url)
  response.html.render(sleep=1, scrolldown=1)
  
  if response.status_code == 200:
    tree = HTMLParser(response.text)
    budget = tree.css_first("div.visualization-section__data")
    return budget.text()
  else:
    return f"Could not get a successful response from the server: {response.status_code}"

if __name__ == "__main__":
  show_me_the_money()