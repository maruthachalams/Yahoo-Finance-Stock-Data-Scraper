# Yahoo Finance Stock Data Scraper

This project is a web scraping tool that fetches stock data from Yahoo Finance. It extracts information about the top gainers, losers, most active, and trending stocks, and saves the data into separate text files.

## Features

- Scrapes data for top gainers, losers, most active, and trending stocks.
- Cleans and processes HTML content.
- Writes data to separate text files.

## Requirements

- Python 3.x
- Selenium
- ChromeDriver
- Other Python libraries: `re`, `time`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/maruthachalams/Yahoo-Finance-Stock-Data-Scraper.git


## Run the script:
  python your_script_name.py

  - The output files (Gainer_Output.txt, Loser_Output.txt, Most_active_Output.txt, and Trending_Output.txt) will be generated in the same directory.

## Code Structure
  * data_clean(data): Cleans the HTML content.
  * single_regex(pattern, target_string): Extracts data using a regex pattern.
  * block_loop(loop_block): Extracts stock information from a block of HTML
## Main Script:
  * Sets up ChromeDriver options.
  * Fetches the Yahoo Finance webpage.
  * Processes and extracts data for different stock categories.
  * Writes data to respective files.
