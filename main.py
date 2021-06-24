
import requests
from datetime import datetime, time

api_key = '851effbc4ba11c6314ac49c144503ce3'
geo_api = '5cc90063b698433c9e339c156b4d9777'

# return {'status': 'success', 'countryCode': 'VN', 'city': 'Ho Chi Minh City'}
def ip2place():
    # url = "http://ip-api.com/json/"    #--> get full fields
    url = f"http://ip-api.com/json/?fields=status,countryCode,city"
    res = requests.get(url).json()
    return res

# input YYYY-MM-DD format
def get_time(time_str):
    try:
        year, month, day = map(int, time_str.split('-'))
    except:
        return datetime.now()
    return datetime(year, month, day)

def get_lat_lon(address, geo_api):
    url = f"https://api.opencagedata.com/geocode/v1/json?q={address}&key={geo_api}"
    res = requests.get(url).json()
    return res

#one call api --> return current and forecast next 7 days 
def get_weather(api_key, lat, lon):
    url = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&units=metric&lang=vi&appid={api_key}"
    res = requests.get(url).json()
    return res

#one call api --> return current in history, hourly: 7am to 6am next day
def get_his_weather(api_key, lat, lon, time):
    time = int(time.timestamp())
    url = f'https://api.openweathermap.org/data/2.5/onecall/timemachine?lat={lat}&lon={lon}&units=metric&lang=vi&dt={time}&appid={api_key}'
    res = requests.get(url).json()
    return res

#show current
def show_weather(res):
  if 'cod' in res:
    print(res['message'])
  else:
    print('Thời tiết tại khu vực', res['timezone'],', vào lúc',datetime.fromtimestamp(res['current']['dt']),'theo giờ địa phương:')
  
    print('* Nhiệt độ trung bình:', res['current']['temp'],'°C')
    print('* Nhiệt độ ngoài trời:', res['current']['feels_like'],'°C')
   
    print('Thời tiết:', res['current']['weather'][0]['description'])
    # res['current']['weather'][0]['icon']

    print('Tỉ lệ mây:',res['current']['clouds'],'%')
    print('Độ ẩm:',res['current']['humidity'],'%')
    print('Áp xuất:', res['current']['pressure'],'hPa')
    print('Tốc độ gió:', res['current']['wind_speed'], 'm/s')
    print('Tầm nhìn xa:',res['current']['visibility']/1000,'km')

    print('Mặt trời mọc lúc: ', datetime.fromtimestamp(res['current']['sunrise']))
    print('Mặt trời lặn lúc: ', datetime.fromtimestamp(res['current']['sunset']))

#show future
def show_future_weather(res, number_of_days):
    if 'cod' in res:
        print(res['message'])
    else:
        print('Thời tiết tại khu vực', res['timezone'],', vào lúc',datetime.fromtimestamp(res['daily'][number_of_days]['dt']),'theo giờ địa phương:')
        
        print("* Nhiệt độ trung bình:")
        print('   Ban ngày:', res['daily'][number_of_days]['temp']['day'],'°C')
        print('   Sáng sớm:', res['daily'][number_of_days]['temp']['morn'],'°C')
        print('   Giữa trưa:', res['daily'][number_of_days]['temp']['eve'],'°C')
        print('   Ban đêm:', res['daily'][number_of_days]['temp']['night'],'°C')
        print('   Thấp nhất:', res['daily'][number_of_days]['temp']['min'],'°C')
        print('   Cao nhất:', res['daily'][number_of_days]['temp']['max'],'°C')

        print('* Nhiệt độ ngoài trời:')
        print('   Ban ngày:', res['daily'][number_of_days]['feels_like']['day'],'°C')
        print('   Sáng sớm:', res['daily'][number_of_days]['feels_like']['morn'],'°C')
        print('   Giữa trưa:', res['daily'][number_of_days]['feels_like']['eve'],'°C')
        print('   Ban đêm:', res['daily'][number_of_days]['feels_like']['night'],'°C')

        print('Thời tiết:', res['daily'][number_of_days]['weather'][0]['description'])
        # res['daily'][number_of_days]['weather'][0]['icon']

        print('Tỉ lệ mây:',res['daily'][number_of_days]['clouds'],'%')
        print('Độ ẩm:',res['daily'][number_of_days]['humidity'],'%')
        print('Áp xuất:', res['daily'][number_of_days]['pressure'],'hPa')
        print('Tốc độ gió:', res['daily'][number_of_days]['wind_speed'], 'm/s')
        print('==> Khả năng mưa:', res['daily'][number_of_days]['rain'], '%')

        print('Mặt trời mọc lúc: ', datetime.fromtimestamp(res['daily'][number_of_days]['sunrise']))
        print('Mặt trời lặn lúc: ', datetime.fromtimestamp(res['daily'][number_of_days]['sunset']))

def weather_forecast(place, time):
    '''
    time: datetime
    place: address, city + country_code, ...
    '''

    # Calculate number of days between two dates
    now = datetime.now().date()
    delta = time.date() - now
    number_of_days = delta.days

    #get lat lon
    geo = get_lat_lon(place, geo_api)

    if geo['status']['message'] != 'OK':
        print('Lỗi địa chỉ')
        return False

    lat = geo['results'][0]['geometry']['lat']
    lon = geo['results'][0]['geometry']['lng']

    if number_of_days >= 0 and number_of_days < 8:
        res = get_weather(api_key, lat, lon)
        if number_of_days == 0:
            show_weather(res)
        else:
            show_future_weather(res, number_of_days)
    elif number_of_days < 0 and number_of_days > -6:
        res = get_his_weather(api_key, lat, lon, time)
        show_weather(res)
    else:
        print('Chưa có dữ liệu')
        return False
    return True

if __name__ == '__main__':
    print('Fill in or leave blank to get weather information at current location')
    place = input('Address/City, CountryCode: ')
    time_str = input("Enter date in YYYY-MM-DD format: ")
    
    if time_str == '':
        time = datetime.now()
    else:
        time = get_time(time_str)
        
    if place == '':
        res = ip2place()
        if res['status'] != 'success':
            print('can not get address from ip')
        else:
            place = res['city']+','+res['countryCode']
    
    weather_forecast(place, time)
