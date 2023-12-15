import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Set the URL of the website with images
print("Put in a website with images")
url = input()

# Make a GET request to the website
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Create a BeautifulSoup object
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all images on the website
    images = soup.find_all('img')

    # Download and save each image
    for i, img in enumerate(images, 1):
        img_url = img['src']
        img_url = urljoin(url, img_url)  # Handle relative URLs
        img_data = requests.get(img_url).content

        with open(f"image_{i}.jpg", 'wb') as img_file:
            img_file.write(img_data)

        print(f"Image {i} downloaded successfully.")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
