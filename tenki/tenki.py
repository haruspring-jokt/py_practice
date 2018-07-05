import requests
import json


def get_weather(city_id):
    url = 'http://weather.livedoor.com/forecast/webservice/json/v1?city=' + city_id
    html = requests.get(url)
    json_file = json.loads(html.text)
    data = json.dumps(json_file, indent=4, sort_keys=True, ensure_ascii=False)

    # output
    print(data)


if __name__ == '__main__':
    city_id = '130010'  # tokyo
    get_weather(city_id)
