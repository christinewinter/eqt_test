source venv/bin/activate

echo "Starting data scraping"
python3 src/data_scraping.py
echo "Finished data scraping"

echo "Starting data wrangling"
python3 src/data_wrangling.py
echo "Finished data wrangling"

echo "Starting data upload"
python3 src/data_upload.py
echo "Finished data upload"
