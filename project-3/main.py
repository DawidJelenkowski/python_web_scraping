from playwright.sync_api import sync_playwright
URL = "https://store.steampowered.com/specials"

if __name__ == "__main__":
  TIMEOUT = 900000
  
  # launches browser
  with sync_playwright() as p:
    # change between headless True/False can give better result
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto(URL)
    
    # wait until some class pops up
    # page.wait_for_selector("div.some_class")
    
    # waits until the page loads
    page.wait_for_load_state("networkidle")
    
    # anonymous js function
    # scroll down to load page content
    page.evaluate("() => window.scroll(0, document.body.scrollHeight)")
 
    # takes screenshot
    # page.screenshot(path="steam#.png", full_page=True)
    
    html = page.inner_html("body")