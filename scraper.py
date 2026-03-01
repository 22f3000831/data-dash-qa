import asyncio
from playwright.async_api import async_playwright

async def compute_total_sum():
    total_sum = 0
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        # Loop through seeds 67 to 76
        for seed in range(67, 77):
            url = f"https://sanand0.github.io/tdsdata/js_table/?seed={seed}"
            print(f"Visiting {url}...")
            
            await page.goto(url)
            await page.wait_for_selector('td')
            
            # Extract text from all table data cells
            td_texts = await page.evaluate('''() => {
                const tds = Array.from(document.querySelectorAll('td'));
                return tds.map(td => td.innerText);
            }''')
            
            # Sum up valid numbers
            for text in td_texts:
                try:
                    clean_text = text.replace(',', '').strip()
                    if clean_text:
                        total_sum += float(clean_text)
                except ValueError:
                    pass
            
        await browser.close()
        print(f"\nFinal Total Sum of all tables: {total_sum}")

if __name__ == '__main__':
    asyncio.run(compute_total_sum())
