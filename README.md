# Summary
This is the code for enriching the portfolio data that is available on EQT's web page with additional data from 
a reference data set. It contains of three components: 

- Data scraping to download the data from EQT's website in json format
- Data wrangling where two datasets are combined
- Data upload to save the final dataset in a google cloud storage bucket

# Setup
To execute the pipeline, you need to:
1) download the data for `interview-test-funding.json` and `interview-test-org.json`
and save them under `data/`
2) Set up a virtual environment under venv 
3) Install python dependencies with `pip install -r requirements.txt`

Then you can run the whole pipeline with `sh run.sh`

# Suggestions of improvement
- Fetch data from google cloud storage instead of manually download of
  - interview-test-funding.json
  - interview-test-org.json
- Extended testing
  - Mock data for requests in data scraping
  - Test data for merges in data wrangling
- Data schema definitions 
- Config files to make the data scraping code leaner
- Define airflow DAG instead of run.sh
- Dockerise code
- Add logs
- Add exception handling
