# LibertyBooks Crawler  📚 🕷️ 

LibertyBooks Crawler is a Scrapy project designed to scrape data for over 400 Urdu books from the website [Liberty Books](https://www.libertybooks.com). The project collects book details, including book name, book link, author name, author link, and price, and saves the output in a CSV file named "libertybooks.csv."

## Getting Started

To run the LibertyBooks Crawler, follow these steps:

1. **Install Python:** Make sure you have Python installed on your system. You can download the latest version of Python from the [official website](https://www.python.org/downloads/).

2. **Virtual Python Environment (Optional):** This repository includes a virtual Python environment to isolate the project dependencies. If you prefer to work in a virtual environment, you can set it up using the following steps:

   - Install virtualenv (if not already installed):
     ```
     pip install virtualenv
     ```

   - Create a new virtual environment (replace "env_name" with your preferred name):
     ```
     virtualenv env_name
     ```

   - Activate the virtual environment:
     - On Windows:
       ```
       env_name\Scripts\activate
       ```
     - On macOS and Linux:
       ```
       source env_name/bin/activate
       ```

   - Once the virtual environment is activated, install the required packages using the provided `requirements.txt` file:
     ```
     pip install -r requirements.txt
     ```

3. **Clone the repository:** Clone this GitHub repository to your local machine.

4. **Navigate to the project folder:** Open your terminal or command prompt and go to the folder where you cloned the repository.

5. **Run the spider:** To start crawling the website and collecting data, use the following command:
On Windows:
```
       scrapy crawl books -o libertybooks.csv
```

This command will run the `books` spider, and the data will be saved to a CSV file named "libertybooks.csv" in the project folder.

## Spider Details

The spider used in this project is named `books`. It starts from the website's homepage ([Liberty Books](https://www.libertybooks.com)) and navigates through multiple pages to collect data for over 400 Urdu books. The spider uses try-except blocks for error handling to ensure smooth scraping even if certain attributes are missing on some pages.

## Output

The scraped data will be saved in CSV format as "libertybooks.csv" in the project folder. The CSV file will contain columns for book name, book link, author name, author link, and price.

## Important Notes

- **Respect Website Policies:** Ensure that you are adhering to the website's terms of service and robots.txt file while running the scraper. Avoid excessive requests and consider adding delays to be respectful of the website's server resources.

- **Data Usage:** Be mindful of how you use the scraped data, and make sure to follow any applicable laws and regulations regarding data usage and copyright.

- **Feedback and Improvements:** If you encounter any issues or have suggestions for improvements, feel free to open an issue or submit a pull request on the GitHub repository.

Happy crawling and data scraping with Scrapy! 🚀



## 🔗 Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/ocama-mohamed/)

