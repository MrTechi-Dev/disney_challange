import requests

def get_http_status_code(url):
    try:
        response = requests.get(url)
        return response.status_code
    except requests.exceptions.RequestException as e:
        return f"Request failed: {e}"

def read_urls_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            urls = file.readlines()
            return [url.strip() for url in urls]
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return []

def main(file_path):
    urls = read_urls_from_file(file_path)
    if not urls:
        return

    for url in urls:
        status_code = get_http_status_code(url)
        print(f"URL: {url} - Status Code: {status_code}")

if __name__ == "__main__":
    file_path = '/Users/andres/Documents/disney_challange/disney_challange/aws_scripts/urls.txt'  
    #file_path = 'www.gogole.com'
    main(file_path)
