from bs4 import BeautifulSoup
from google.cloud import storage
from google.oauth2 import service_account
import requests
import csv

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

credentials_dict = {
    # Colocar suas credênciais
    "type": "service_account",
    "project_id": "hazel-lyceum-343617",
    "private_key_id": "dd813c37c851f21ce5b7cc02876da3ca2cb71141",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDdf7Yoe6n2akpj\nuWCpADiDChrxHw9s1Mn4kFGThefVR3rwLpSrP/xRjC0RWABiV86j3/EzpKLA1IrB\nb5W3A1qmrGSJZi2VdOIis6m8re9tQ1L+EnC3FBBEMaiKqM/zgzuT7vtsv3py6PU6\nINfg7PBkGMZ3NFpUxoOsF1COZTI7XMlGNUyTZLlAaLDWE4QinikId37ycFLcsJlP\nW3C/AM8JR+kC23ftO47wZiRjflIf15C6jejBwQyIxlonAJ0UNkUPqi0Co9XF59Ln\ni2VMC2iTHD0zO5VvRSKM/u7y0Geq9iQv1fT5KPKnyHhJyxsY7xw0fbyjtBrKU/Ap\nfLi4r1kFAgMBAAECggEAGcwzGhn1HLcafOztXiGhc1ms86JreIB8GZAtgCIbc1LE\n9c5nEF7+cz0BTsDSIqIZdiqx/BLTxeO7WXY2mL8yQrFXcE1PR9X6NJJ6VXhop3As\n7VyWdixHDLo/6A5rUfBZ8wvliq/ugg2x6hhDLHZMNUxRaTbWwoLweQ2qGzucEx+u\n4ESrlvMY39KdGXdr5SsxAanq5JDJO6xSreR9yQFrLvOEV3gBiBl/CfaQ5CVGvgiS\ntamn9ObXN/T7i62r/O7rsjgcklF7csSaB6w8uyOWAneBxlbQIKd4gS7I+pBkBI2M\n3HU1zPH4L6hHNQvST0NKD1VGWTkyzemfcKWuYdQFYQKBgQD7gl1DkgjXyfzixlmW\np4CSbkkLAdKPlYTRBFQl29h6R+uVPQ/Q7rWC1Bl+BKxK5tXGPr1bwXrL7j5KzwpE\nUNeQBjnxPXuCGREf+COajxRQuvYvbWQwXrUcl+J0Q+BnwMTdntAlPgS+bCHmRzNf\na+xe3+M1p6/pqKyuU/gWFDuCfQKBgQDhdCvi6xD2IAJlUVgEM0XlUnp/7jZWKV6/\nzPOD/KPY6yBRH6I7brWRG/GY9vIg3or47TrY6ek2WP2HWyQjWXVKg33kBM/cIp/e\nwspH/fxjIv1L258rIL3dfO7LVPmBTv2LlrA2WpdwLdEz0qpEnGwsjp04los3olwv\nnRGQPwSvKQKBgH5snlLr4lQOLXcUu03WbvOsSj0lMmGIiBXE9kN9igiVhF8lLYEZ\nrNXRperJkI2qEQUw3mB0FjTSUi+qeP+0H1c/OfsAq8fOr+QBCGyVxWF7SWq3syf5\nQ1LXKjbFM9UTeiHoxboivaG2mye03Kb3if56zixXWT670eljPg5jJzLFAoGALbcp\nwvyZVt8MvVCuQUPIU4TS9Cfweq4u2UOMyWGsM6sRxYFdmyGKzZ7V8Yd5d3LIyUsJ\nWLytnmiTGCRCAqz8HJznJRpYr7GRq1DiRZDZ4ZxRslUZRFyCQ2w226IiabcDsI9g\nsdTSyltwBUsdXYY+ZRaSCMx19FUGzlzSF+a/Y2kCgYAQrz5bL0xRRJ8PGid35Gpp\nZfxCUAxDn061f/13r0v4hxI901nBsK2RVBsDu4QuP5qkKCVlMA0/qORMsaRRjd23\nruyWdSfZ5DiYjgXmpzUmBP6ghBg19EfoHGKp/BZ8662GdC0EBkkyUuSU25PdtSgs\n5f8M0lmLe7m69uIM8niTRw==\n-----END PRIVATE KEY-----\n",
    "client_email": "908573186440-compute@developer.gserviceaccount.com",
    "client_id": "110252518196254568444",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/908573186440-compute%40developer.gserviceaccount.com"

}

try:

    """Uploads a file to the bucket."""
    credentials = service_account.Credentials.from_service_account_info(
        credentials_dict)
    storage_client = storage.Client(credentials=credentials)
    bucket = storage_client.get_bucket('atividade_iv')  # Nome do seu bucket
    blob = bucket.blob('atividade_iv.csv')

    pages = []
    names = "Name \n"

    for i in range(1, 5):
        url = 'https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ' + \
            str(i) + '.htm'
        pages.append(url)

    for item in pages:
        page = requests.get(item)
        soup = BeautifulSoup(page.text, 'html.parser')

        last_links = soup.find(class_='AlphaNav')
        last_links.decompose()

        artist_name_list = soup.find(class_='BodyText')
        artist_name_list_items = artist_name_list.find_all('a')

        for artist_name in artist_name_list_items:
            names = names + artist_name.contents[0] + "\n"

        blob.upload_from_string(names, content_type="text/csv")

except Exception as ex:
    print(ex)
