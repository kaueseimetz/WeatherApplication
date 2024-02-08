import calendar

def windDirection(direction):
    directions = {
        'N': 'Norte',
        'NE': 'Nordeste',
        'E': 'Leste',
        'SE': 'Sudeste',
        'S': 'Sul',
        'SW': 'Sudoeste',
        'W': 'Oeste',
        'NW': 'Noroeste'
    }
    return directions.get(direction, 'Desconhecido')

def wind_speed(speed):
    if speed <= 5:
        return "Calmo"
    elif speed <= 15:
        return "Moderado"
    elif speed <= 25:
        return "Ventoso"
    elif speed <= 35:
        return "Muito ventoso"
    elif speed <= 45:
        return "Fortemente ventoso"
    else:
        return "Extremamente ventoso"

def lifted_index_text(index):
    if index > 0:
        return "Menor chance de tempestades"
    elif index < 0:
        return "Maior chance de tempestades"
    else:
        return "Chance normal de tempestades"

def translateDay(day):
    days = {
    "0": "Segunda-feira",
    "1": "Terça-feira",
    "2": "Quarta-feira",
    "3": "Quinta-feira",
    "4": "Sexta-feira",
    "5": "Sábado",
    "6": "Domingo"
    }
    return days.get(day, "Null")

def translateTime(compostTime, Time):
    year, month, day, hour = map(int, str(compostTime).split("-"))
    
    monthRange = calendar.monthrange(year, month)
    
    finalHour = hour + Time
    
    while finalHour >= 24:
        day += 1
        finalHour -= 24
        
    if day > monthRange[1]:
        day -= monthRange[1]
        month += 1
        
    if month > 12:
        month -= 12
        year += 1
        
    return f"{year}_{month}_{day}_{translateDay(str(calendar.weekday(year, month, day)))}_{finalHour}:00"
