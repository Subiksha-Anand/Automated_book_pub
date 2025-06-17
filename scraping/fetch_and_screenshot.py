from playwright.sync_api import sync_playwright
from pathlib import Path
import time

def fetch_and_screenshot(url, output_dir="outputs"):
    Path(output_dir).mkdir(exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url, wait_until="networkidle")
        time.sleep(3)
        page.screenshot(path=f"{output_dir}/chapter.png", full_page=True)
        content = page.inner_text("#mw-content-text")

        if "Page Not Found" in content or "broken link" in content:
            print("⚠️ Warning: Page content might be missing or invalid.")
            return None

        with open(f"{output_dir}/chapter.txt", "w", encoding='utf-8') as f:
            f.write(content)
        browser.close()
    return content

