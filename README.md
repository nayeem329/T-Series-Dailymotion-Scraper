# T-Series Dailymotion Scraper

## Overview

**T-Series Dailymotion Scraper** is a Python-based web scraping project that collects the first 500 video URLs from the T-Series channel on Dailymotion. It extracts the video IDs from these URLs and determines the most frequently occurring character in the video IDs. This project uses Selenium for web scraping and is intended for educational purposes.

## Features

- Scrapes the first 500 video URLs from the T-Series Dailymotion channel.
- Extracts video IDs from the collected URLs.
- Counts the frequency of each character in the video IDs.
- Identifies and prints the most frequently occurring character.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed on your machine.
- Google Chrome and ChromeDriver installed.
- Required Python packages: `selenium`, `webdriver_manager`, `collections`.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/tseries-dailymotion-scraper.git
   cd tseries-dailymotion-scraper
   ```

2. Set up a virtual environment:
   ```sh
   python -m venv .venv
   source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
   ```

3. Install the required packages:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

1. Ensure the ChromeDriver is accessible via PATH or specify its location in the script.
2. Run the script:
   ```sh
   python main.py
   ```
3. The script will:
   - Open the T-Series channel on Dailymotion.
   - Collect the first 500 video URLs.
   - Extract and analyze the video IDs.
   - Print the most frequently occurring character and its count.

## Example Output

```
Page opened successfully
Found 25 elements
Collected 500 video URLs
Extracted 500 video IDs
Character frequencies: Counter({'x': 123, 'm': 98, 'a': 56, ...})
x:123
```

## Project Structure

```
tseries-dailymotion-scraper/
├── .venv/                   # Virtual environment directory
├── main.py                  # Main script for scraping and analysis
├── requirements.txt         # Python dependencies
└── README.md                # Project README file
```

## Troubleshooting

- If the script fails to load the page, ensure your internet connection is stable.
- If ChromeDriver is not found, ensure it is in your PATH or update the script with the correct path.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create your feature branch: `git checkout -b feature/your-feature`.
3. Commit your changes: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature/your-feature`.
5. Open a pull request.

## References
- Selenium Documentation
- WebDriver Manager for Python
- Dailymotion API
