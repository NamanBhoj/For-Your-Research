# Web Scraper

## Overview

This web scraper extracts data from web pages and stores it in CSV files. The project consists of a backend, responsible for running the scraper, and a frontend for initiating the scraping process.

## Setup

1. Install project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Navigate to the backend folder:

   ```bash
   cd backend
   ```

3. Run the backend server:

   ```bash
   python3 manage.py runserver
   ```

4. Open another terminal, navigate to the frontend folder:

   ```bash
   cd frontend
   ```

5. Start the frontend:

   ```bash
   npm run dev
   ```

6. Access the webpage in your browser and click the button to initiate the scraping process.

## Data Storage

The scraped data is stored in the following CSV files:

- `articles.csv`: Contains information about the scraped articles.
- `citations.csv`: Contains data about the citations.
