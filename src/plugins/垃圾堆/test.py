from GetData import WeatherData
params = {
        'cityid': "",
        "city": "北京",
        'ip': ''

    }

print(WeatherData().request_data(params))
