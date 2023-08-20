import re


def convert_to_24_hour_format(time_str):
    # Extraction of  hour, minute, second, and AM/PM
    pattern = r'(\d{1,2}):(\d{1,2}):(\d{1,2}) (AM|PM)'
    match = re.match(pattern, time_str)
    
    if match:
        hour = int(match.group(1))
        minute = int(match.group(2))
        second = int(match.group(3))
        am_pm = match.group(4)
        
        # MAKING AM/PM ADJUSTMENTS
        if am_pm == 'PM' and hour != 12:
            hour += 12
        elif am_pm == 'AM' and hour == 12:
            hour = 0
        
        # MAKING IT INTO 24 HRS SYSTEM
        formatted_time = f'{hour:02d}:{minute:02d}:{second:02d}'
        return formatted_time
    
    else:
        return "Invalid input format"

# Testing with a specific date
input_time = "09:30:45 PM"
result = convert_to_24_hour_format(input_time)
print(result) 
