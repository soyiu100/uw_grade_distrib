from django.utils import timezone

def get_curr_yrqtr():
    # yyyyq, where y=digits for year; q=digit for quarter 
    # 1=winter, 2=spring, 3=summer, 4=autumn
    year = str(timezone.now().year) 
    quarter = timezone.now().month 
    day = timezone.now().day 
    if quarter >= 9 and quarter <= 12:
        quarter = str(4) 
    elif quarter >= 1 and quarter <= 3:     
        quarter = str(1)     
        # loose bound of where spring quarter may start,     
        # as it varies each year     
        if day > 15:         
            quarter = str(2)     
        else:         
            quarter = str(1) 
    elif quarter > 3 and quarter <= 6:     
        if day > 15:         
            quarter = str(3)     
        else:         
            quarter = str(2) 
    else:     
        quarter = str(3) 
    curr_yrqtr = year + quarter 
    curr_yrqtr = int(curr_yrqtr)
    return curr_yrqtr

def base4sub(value, arg):
    readj_arg = int(arg / 4) * 10 + arg % 4 
    return value - readj_arg

