import os
import time
from playwright.sync_api import sync_playwright

def generate_perfect_pdf():
    with sync_playwright() as p:
        # Launch browser
        browser = p.chromium.launch(headless=True)
        
        # Set viewport to 1200px (your dashboard width)
        context = browser.new_context(
            viewport={'width': 1200, 'height': 1000},
            device_scale_factor=2
        )
        page = context.new_page()

        # Absolute file path
        file_path = "file://" + os.path.abspath("output4.html")
        print(f"Generating PDF for: {file_path}")

        # Load and wait
        page.goto(file_path, wait_until="networkidle")
        
        # Mandatory wait for CSS layout engine to settle
        time.sleep(5)
        
        # Emulate screen mode to keep Navy Background
        page.emulate_media(media="screen")

        # Generate PDF with 0.8 scale to fit A4 perfectly
        page.pdf(
            path="output.pdf",
            format="A4",
            print_background=True,
            scale=0.8, # THE MAGIC FIX
            margin={"top": "10mm", "bottom": "10mm", "left": "10mm", "right": "10mm"}
        )

        browser.close()
        print("Success! output.pdf is ready. Open it in Chrome or Edge.")

if __name__ == "__main__":
    generate_perfect_pdf()