import json
import pandas as pd

# Output file
OUTPUT_FILENAME = "data/enriched_portfolio.json"

# Read data from files
DIVESTMENTS_PATH = "data/divestments.json"
FUNDS_PATH = "data/fund.json"
PORTFOLIO_PATH = "data/portfolio.json"
INTERVIEW_TEST_FUNDING_PATH = "data/interview-test-funding.json"
INTERVIEW_TEST_ORG_PATH = "data/interview-test-org.json"

divestments_df = pd.read_json(DIVESTMENTS_PATH)
funds_df = pd.read_json(FUNDS_PATH)
portfolio_df = pd.read_json(PORTFOLIO_PATH)
interview_test_funding_df = pd.read_json(INTERVIEW_TEST_FUNDING_PATH, lines=True)
interview_test_org_df = pd.read_json(INTERVIEW_TEST_ORG_PATH, lines=True)

# Add features to dataset
features = ['company_name', 'sector', 'country', 'entry_year', 'exit_year', 'company_page_path']

enriched_portfolio_df = pd.merge(portfolio_df[features],
                                 interview_test_org_df,
                                 how="left",
                                 left_on="company_name",
                                 right_on="company_name")

enriched_portfolio_dict = enriched_portfolio_df.to_dict('records')

with open(OUTPUT_FILENAME, "w") as output_file:
    json.dump(enriched_portfolio_dict, output_file)

