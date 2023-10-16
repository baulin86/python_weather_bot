def matchig_weather(code):
    if code == '01d'or code == '01n':
        return '☀️y' 
    elif code == '02d'or code == '02n':
        return '🌤'
    elif code == '03d'or code == '03n':
        return '🌥'
    elif code == '04d'or code == '04n':
        return '☁️'
    elif code == '09d'or code == '09n':
        return '🌧'
    elif code == '10d'or code == '10n':
        return '🌦'
    elif code == '11d'or code == '11n':
        return '🌩'
    elif code == '13d'or code == '13n':
        return '❄️'
    elif code == '50d'or code == '50n':
        return '💨'
    else:
        return '🤷‍♂️'
    
    
def mathing_wind(direction):
    if direction > 337.5 or direction <= 22.5:
        return '⬆️'
    elif 22.5 < direction <= 67.5:
        return '↗️'
    elif 67.5 < direction <= 112.5:
        return '➡️'
    elif 112.5 < direction <= 177.5:
        return '↘️'
    elif 177.5 < direction <= 202.5:
        return '⬇️'
    elif 202.5 < direction <= 247.5:
        return '↙️'
    elif 247.5 < direction <= 292.5:
        return '⬅️'
    elif 292.5 < direction <= 337.5:
        return '↖️'