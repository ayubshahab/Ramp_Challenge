from bs4 import BeautifulSoup

def parse_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')

    # Find all section elements with data-id starting with 92
    sections = soup.find_all('section', {'data-id': lambda x: x and x.startswith('92')})
    
    # divs = articles.find_all('div', {'data-tag': lambda x: x and '78' in x})
    for section in sections:
        # print(section.prettify())
        articles = section.find_all('article', {'data-class': lambda x: x and x.endswith('45')})

        for article in articles:
            # print(article.prettify())
            divs = article.find_all('div', {'data-tag': lambda x: x and '78' in x})

            for div in divs:
                # print(div.prettify())
                b_elements = div.find_all('b', {'class': 'ref'})

                values = [b.get('value') for b in b_elements]
                print("".join(values), end="") #valid url

if __name__ == '__main__':
    file_path = "challenge.html"
    parse_html(file_path)
