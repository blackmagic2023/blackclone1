import requests
from bs4 import BeautifulSoup
import os
import wget
import urllib.parse
from concurrent.futures import ThreadPoolExecutor

# Function to scrape webpage and save data and HTML separately
def scrape_webpage(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise exception for bad status codes
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            # Save HTML
            with open('webpage.html', 'w', encoding='utf-8') as f:
                f.write(response.text)
            # Save data
            with open('webpage_data.txt', 'w', encoding='utf-8') as f:
                f.write(soup.get_text())
    except requests.exceptions.RequestException as e:
        print(f"Error scraping webpage: {e}")

# Function to clone webpage
def clone_webpage(url):
    try:
        wget.download(url, out=os.getcwd())
    except Exception as e:
        print(f"Error cloning webpage: {e}")

# Function to scrape images from webpage
def scrape_images(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise exception for bad status codes
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            img_tags = soup.find_all('img')
            for img_tag in img_tags:
                img_url = img_tag.get('src')
                if img_url:
                    img_url = urllib.parse.urljoin(url, img_url)
                    filename = os.path.basename(img_url)
                    wget.download(img_url, out=filename)
    except requests.exceptions.RequestException as e:
        print(f"Error scraping images: {e}")

# Function to scrape and clone entire website
def scrape_and_clone_website(url):
    try:
        scrape_webpage(url)
        clone_webpage(url)
        response = requests.get(url)
        response.raise_for_status()  # Raise exception for bad status codes
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            links = soup.find_all('a', href=True)
            for link in links:
                link_url = urllib.parse.urljoin(url, link['href'])
                with ThreadPoolExecutor(max_workers=5) as executor:
                    executor.submit(scrape_and_clone_website, link_url)
    except Exception as e:
        print(f"Error scraping and cloning website: {e}")

# Function to change URL
def change_url():
    new_url = input("Enter the new URL: ")
    return new_url

# Main menu
def main():
    url = input("Enter the URL: ")
    try:
        while True:
            print("\nMain Menu:")
            print("1. Scrape Webpage")
            print("2. Clone Webpage")
            print("3. Scrape Images")
            print("4. Scrape and Clone Entire Website")
            print("5. Change URL")
            print("0. Exit")
            print("Blackmagic is your webdaddy")
            choice = input("Enter your choice: ")

            if choice == '1':
                scrape_webpage(url)
            elif choice == '2':
                clone_webpage(url)
            elif choice == '3':
                scrape_images(url)
            elif choice == '4':
                scrape_and_clone_website(url)
            elif choice == '5':
                url = change_url()
            elif choice == '0':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please enter a valid option.")
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")

if __name__ == "__main__":
    main()
