from google.cloud import storage

# Credentials to get access google cloud storage
storage_client = storage.Client.from_service_account_json('.key/gcloud_private_key.json')

bucket_name = 'eqt-test-bucket'
BUCKET = storage_client.get_bucket(bucket_name)

filename = "enriched_portfolio.json"
local_filename_path = "data/" + filename


def upload_json_file(filename: str, local_filename_path: str) -> dict:
    """
    Create json file in google cloud storage
    """

    blob = BUCKET.blob(filename)
    blob.upload_from_filename(local_filename_path)
    result = filename + ' upload complete'
    return {'response': result}


# run the function and pass the json_object
upload_json_file(filename, local_filename_path)
