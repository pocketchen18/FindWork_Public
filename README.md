# Yingjiesheng Job Application Automation

This project automates the process of applying for internships on the Yingjiesheng (应届生) website using Playwright for browser automation.

## Overview

The script automates the following tasks:
- Navigates to the Yingjiesheng internship search page
- Searches for specified positions
- Automatically clicks "立即申请" (Apply Now) buttons for multiple listings
- Handles different types of application popups and new windows
- Supports pagination for applying to more positions than fit on one page

## Features

- **Automated Job Search**: Fill in position requirements and automatically search
- **Bulk Application**: Apply to multiple positions in one run
- **Popup Handling**: Automatically handles different types of application popups
- **Pagination Support**: Automatically navigates to next pages when needed
- **Browser Automation**: Uses Firefox browser through Playwright

## Prerequisites

- Python 3.7+
- Playwright library
- Firefox browser

## Installation

1. Install the required dependencies:
   ```bash
   pip install playwright
   ```

2. Install Playwright's browser drivers:
   ```bash
   playwright install firefox
   ```

## Usage

1. Run the script:
   ```bash
   python -m core.mian
   ```

2. Follow the prompts:
   - Press Enter to continue through initialization steps
   - Enter the position you want to search for
   - Specify how many applications you want to submit

## How It Works

The automation script:

1. Opens Firefox browser in non-headless mode
2. Navigates to the Yingjiesheng internship search page
3. Waits for user input for position type
4. Fills the search field and submits the search
5. Counts and clicks "立即申请" (Apply Now) buttons
6. Handles both new window applications and popup modals
7. Automatically paginates to continue applying through multiple pages

## Important Notes

- This script is designed to run in non-headless mode so you can monitor the automation
- The script includes timeouts and error handling for robust operation
- Make sure you're logged in to Yingjiesheng before running the script if required
- Use responsibly and in accordance with the website's terms of service

## Project Structure

```
/workspace/
├── README.md
└── core/
    ├── __init__.py
    ├── mian.py          # Main entry point
    └── utils/
        ├── __init__.py
        └── yingjiesheng_findwork.py  # Core automation logic
```

## Customization

You can modify the `yingjiesheng_findwork.py` file to:
- Change the XPath selectors if the website layout changes
- Adjust wait times and timeouts
- Add additional application logic

## License

This project is available as-is without any warranty. Please use responsibly and in accordance with applicable terms of service.