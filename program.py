

def main():
    print_the_header()
    code = input('What zip code would you like the weather forecast for?')
    # get html from web
    get_html_from_web(code)
    # parse html
    # display forecast
    print('hello from main')


def print_the_header():
    print('=====================')
    print('     Weather App     ')
    print('=====================')


def get_html_from_web(zipcode):
    url = 'https://www.wunderground.com/weather/us/in/indianapolis/{}'.format(zipcode)
    # print(url)
    # requests hello git!


if __name__ == '__main__':
    main()