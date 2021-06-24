
api_key = '851effbc4ba11c6314ac49c144503ce3'
geo_api = '5cc90063b698433c9e339c156b4d9777'

# icon url
# http://openweathermap.org/img/wn/{icon}@2x.png
# http://openweathermap.org/img/wn/10d@2x.png


#Hiện tại
# http://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&units=metric&lang=vi&appid={api_key}
# return {"coord":{"lon":106.6667,"lat":10.75},"weather":[{"id":802,"main":"Clouds","description":"mây rải rác","icon":"03d"}],"base":"stations","main":{"temp":34.01,"feels_like":41.01,"temp_min":34.01,"temp_max":34.01,"pressure":1008,"humidity":59},"visibility":10000,"wind":{"speed":2.57,"deg":280},"clouds":{"all":40},"dt":1624001857,"sys":{"type":1,"id":9314,"country":"VN","sunrise":1623969113,"sunset":1624015019},"timezone":25200,"id":1566083,"name":"Thành phố Hồ Chí Minh","cod":200}


#Tương lai (7 ngày) và hiện tại (thêm &exclude=hourly,daily,minutely để bỏ 3 cái)
# https://api.openweathermap.org/data/2.5/onecall?lat=10.75&lon=106.6667&exclude=hourly&units=metric&lang=vi&appid=
# https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&units=metric&lang=vi&appid={api_key}



#Quá khứ (hourly: 7am to 6am nextday, daily: trong vòng 5 ngày trước) với time theo kiểu timestamp
# https://api.openweathermap.org/data/2.5/onecall/timemachine?lat={lat}&lon={lon}&units=metric&lang=vi&dt={time}&appid={api_key}



# erro code
# API: cod 401, 404, 429(make more than 60 API calls per minute.)
# 
# cod 200 (success)
# 
# other: lon, lat, country_code, ....
