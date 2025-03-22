import pandas as pd
from playwright.sync_api import sync_playwright

# Load the DataFrame
df = pd.read_csv("jobs.csv")  # Adjust this if your file is different

# Function to generate a custom cover letter based on job description
def generate_cover_letter(description):
    return f"Dear Hiring Manager,\n\nI am excited about the opportunity to apply for this role. {description[:200]}...\n\nBest regards,\nYour Name"


async def check_radio

# Start Playwright automation
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  # Change to True for headless mode
    page = browser.new_page()

    for index, row in df.iterrows():
        job_url = row["url"]
        job_description = row["description"]
        custom_cover_letter = generate_cover_letter(job_description)

        # Visit the job URL
        page.goto(job_url)

        # Find the cover letter input field (you may need to inspect the form structure)
        page.fill("textarea[name='cover_letter']", custom_cover_letter)  # Adjust selector

        # Submit the form (adjust the button selector)
        page.click("button[type='submit']")

        print(f"Applied to: {job_url}")

    browser.close()
