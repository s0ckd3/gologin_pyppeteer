from pyppeteer import launch
import asyncio



async def main():

    browser = await launch(
        {
        'executablePath': 'C:\\orbita-browser\\chrome.exe',
        'ignoreHTTPSErrors': True,
        'defaultViewport': None,
        'ignoreDefaultArgs': True,
        'headless': False,
        'args': [
            # '--lang=vi',
            # '--tz=Asia/Bangkok',
            '--no-first-run',
            # '--window-size=640,480'
            '--no-sandbox',
            '--font-masking-mode=2',
            '--origin-trial-disabled-features=ConditionalFocus',
            '--password-store=basic',
            '--disable-encryption',
            '--disable-blink-features=AutomationControlled',
            '--disable-infobars',
            '--disable-notifications',
            '--user-data-dir=F:\\7\\win_win_v99_1_5418',
            # '--disable-extensions-except=${pathToExtension}',
            # '--load-extension=${pathToExtension}',
            # '--remote-debugging-port=9922',
            ]
        }
    )

    page = await browser.newPage()
    await page.goto('https://google.com')
    await page.waitFor(999999);

asyncio.get_event_loop().run_until_complete(main())
