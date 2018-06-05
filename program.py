import requests
import bs4


def main():
    print_the_header()
    code = input('What zip code would you like the weather forecast for?')
    html = get_html_from_web(code)

    # parse html
    get_weather_from_html(html)
    # display forecast
    print('hello from main')


def print_the_header():
    print('=====================')
    print('     Weather App     ')
    print('=====================')


def get_html_from_web(zipcode):
    url = 'https://www.wunderground.com/weather/us/in/indianapolis/{}'.format(zipcode)
    response = requests.get(url)
    # print(response.text[0:250])

    return response.text


def get_weather_from_html(html):
    soup = bs4.BeautifulSoup(html, 'html.parser')
    loc = soup.find(class_='region-content-header').find('h1').get_text()
    condition = soup.find(class_='condition-icon').get_text()
    temp = soup.find(class_='wu-unit-temperature').find(class_='wu-value').get_text()
    scale = soup.find(class_='wu-unit-temperature').find(class_='wu-label').get_text()
    # print(loc, condition, temp, scale)
    print('The weather in {} is {}, and {}{}'.format(loc, condition, temp, scale))


if __name__ == '__main__':
    main()