import requests

url = "https://storage.googleapis.com/kagglesdsdata/datasets/1800580/2936818/data/data_by_genres.csv?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20240604%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20240604T041209Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=72d9aefe7c82bb5dc718936b7d618c61ef745d487bf5eace73950dd4f16e9c1d78e782b3d920aeab7b473df404dad54b77b4b23b14ff3f6953fa48b7816203425147d08a66dfb2af889372f8c41fe99bb183b2b2eb386ce97f7af558af694b907aa73ae8e149d5e7138bccf7f3f7791c821787f3bdf78f2cea524a7b68b02df305fa824cefdb145f095715c81d41cf8632d9c0377d9c80c0d20477c5b619939dae9dbeac984031d56558897c423e35c531ce9fb1dfa2d29aff8a7fc0137e4c5ef4b0c0e8695acb1cf98e0ced02dd916b11b1e3088b3e5fde7a0d094928543ab6de41583b072039609cc07184ba9c499b240e7ee2e5456335dd5f2d7eafdace7e"
#url = "https://storage.googleapis.com/kagglesdsdata/datasets/1800580/2936818/data/data_by_year.csv?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20240604%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20240604T041637Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=685a16d5dcfb44a5678643185994404a02d976aead32cc033289e1c457c451054bc912a490f48879086c9529cc6179206181ea57f36faf15606633fd825659f18d396f0ecb9d9c1153030fd163ca7214d0c229a54990a015851e13b94e1bcf233b09fe9e1c5d4cd213c86fca7293fa2904348db24b5d1ffcbda540e0ce92d47e9a6c29e98655f3a826ffb6d352c63b9ea1b455a91cb8b4523851f1c18d851385d8f17db7f17411a487fd937320a1d03432e1874d6a084c1d6a5998bebf27cd03bd8333a890feada26416d7f00619ab8df643ecb9876d541fe16a98a60a457a71b78f2ea4a2273ff30de01fcc61e4a6387dba49a0a146ec735315fe696602797a"
# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Save the response content to a file
    with open("data_by_genres.csv", "wb") as f:
        f.write(response.content)
    print("CSV file has been downloaded successfully.")
else:
    print("Failed to download the CSV file.")

