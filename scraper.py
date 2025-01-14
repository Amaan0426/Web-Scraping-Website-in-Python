from bs4 import BeautifulSoup
import requests

def scrape_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract text from various HTML elements
        data = {
            'titles': [element.text.strip() for element in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])],
            'paragraphs': [p.text.strip() for p in soup.find_all('p')],
            'links': [a['href'] for a in soup.find_all('a', href=True)],
            'lists': [li.text.strip() for ul in soup.find_all('ul') for li in ul.find_all('li')],
            'tables': [[cell.text.strip() for cell in row.find_all(['th', 'td'])] for row in soup.find_all('tr')],
            'images': [img['src'] for img in soup.find_all('img', src=True)],
            # Add more elements as needed based on your requirements
        }

        return data

    except requests.RequestException as e:
        return f"Error: {str(e)}"
