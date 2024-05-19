# Blackclone

Blackclone is a powerful website cloning tool designed to scrape, clone, and download the content of web pages. Whether you need to save the HTML, extract textual data, or download images, Blackclone has you covered. Developed in Python, Blackclone leverages the `requests`, `BeautifulSoup`, and `wget` libraries to deliver a seamless and efficient cloning experience.

## Features

- **Scrape Webpage**: Extract and save HTML and text data from a web page.
- **Clone Webpage**: Download the entire webpage to your local directory.
- **Scrape Images**: Download all images from a webpage.
- **Scrape and Clone Entire Website**: Recursively scrape and clone an entire website.
- **Change URL**: Easily change the target URL for new operations.

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/blackclone.git
    cd blackclone
    ```

2. **Install the required libraries**:
    ```sh
    pip install -r requirements.txt
    ```

    *Contents of `requirements.txt`:*
    ```plaintext
    requests
    beautifulsoup4
    wget
    ```

## Usage

Run the main script to start Blackclone:
```sh
python blackclone.py
```
You'll be presented with a menu to choose the desired operation:

   - Scrape Webpage: Extracts HTML and text data from the specified URL.
   - Clone Webpage: Downloads the specified webpage.
   - Scrape Images: Downloads all images from the specified webpage.
   - Scrape and Clone Entire Website: Recursively scrapes and clones the entire website starting from the specified URL.
   - Change URL: Allows you to input a new URL.
   - Exit: Exits the program.

## Example
```
Enter the URL: https://example.com

Main Menu:
1. Scrape Webpage
2. Clone Webpage
3. Scrape Images
4. Scrape and Clone Entire Website
5. Change URL
0. Exit
Blackmagic is your webdaddy
Enter your choice: 1
```
## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any suggestions or bug reports.

## Acknowledgements

Blackclone uses the following libraries:
```
    requests
    BeautifulSoup
    wget
```

Happy Cloning! 
