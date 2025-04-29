# YouTube Data Scraper

## Overview
The **YouTube Data Scraper** is a tool designed to extract data from YouTube, such as video details, channel information, comments, and more. This project is ideal for researchers, data analysts, and developers who need to gather insights from YouTube for various purposes like trend analysis, content strategy, or academic research.

## Features
- **Video Data Extraction**: Retrieve details like title, description, views, likes, dislikes, and upload date.
- **Channel Information**: Extract channel statistics, subscriber count, and video lists.
- **Comments Scraping**: Collect comments, usernames, and timestamps for sentiment analysis or engagement tracking.
- **Search Results**: Scrape search results for specific keywords or topics.
- **Customizable Filters**: Apply filters like date range, video category, or region.
- **Export Options**: Save the scraped data in formats like CSV, JSON, or Excel.

## Prerequisites
Before using this tool, ensure you have the following:
- Python 3.8 or higher installed on your system.
- A valid YouTube Data API key (required for accessing YouTube's data).
- Basic knowledge of Python and command-line tools.

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/Igboke/youtube-data-scraper.git
    ```
2. Navigate to the project directory:
    ```bash
    cd youtube-data-scraper
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. Obtain a YouTube Data API key from the [Google Cloud Console](https://console.cloud.google.com/).
2. Add your API key to the `config.py` file:
    ```python
    API_KEY = "your_api_key_here"
    ```
3. Run the scraper:
    ```bash
    python scraper.py
    ```
4. Follow the prompts to specify the type of data you want to scrape.

## Output
The scraped data will be saved in the `output` folder in the format you choose (XLSX etc.).
More to come.

## Example
Here’s an example of scraping video data for a specific keyword:
```bash
python scraper.py --type video --query "Python tutorials" --limit 10
```

## Contributing
Contributions are welcome! If you’d like to improve this project, please:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request with a detailed description of your changes.


## Disclaimer
This tool is intended for educational and research purposes only. Ensure you comply with YouTube's Terms of Service and API usage policies when using this scraper.

## Contact
For questions or support, feel free to reach out:
- Email: danieligboke669@gmail.com
- GitHub: [Igboke](https://github.com/Igboke)

Happy scraping!