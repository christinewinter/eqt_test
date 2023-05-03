import unittest
from src.data_scraping import get_company_list_from_url
from unittest.mock import patch, Mock, MagicMock


class TestDataScaper(unittest.TestCase):

    @patch('requests.get')
    def test_get_portfolio_list(self, mock_get):
        with open('test/test_data/current_portfolio.html', 'r') as file:
            response_data = file.read()

        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = response_data
        mock_get.return_value = mock_response

        result = get_company_list_from_url('https://eqtgroup.com/current-portfolio/')[0]
        del result['id']
        del result['timestamp']

        expected_result = {'company_name': 'Guardian Shanghai Hygiene Service Ltd.',
                           'sector': 'Services',
                           'country': 'China',
                           'fund': 'EQT Mid Market Asia III',
                           'entry_year': '2022',
                           'exit_year': '',
                           'company_page_path': '/current-portfolio/funds/eqt-mid-market-asia-iii/'}

        self.assertEqual(result, expected_result)