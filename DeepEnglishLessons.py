import requests
from bs4 import BeautifulSoup

# Base URL
base_url = "https://deepenglish.com/lessons/"

# Fetch the webpage
response = requests.get(base_url)

# Check for successful response
if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Find all links on the page
    lesson_links = []
    for link in soup.find_all("a", href=True):
        href = link["href"]
        # Filter lesson links (likely sub-paths of /lessons/)
        if "/lessons/" in href and href != "/lessons/":
            lesson_name = href.split("/")[-2]
            if lesson_name not in lesson_links:  # Avoid duplicates
                lesson_links.append(lesson_name)
    
    # Display the full lesson URLs
    full_urls = [f"{base_url}{lesson}" for lesson in lesson_links]
    for url in full_urls:
        print(url)
else:
    print(f"Failed to fetch the webpage. Status code: {response.status_code}")
