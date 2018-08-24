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
    month = value % 10
    i = 0
    test = month - arg
    while test <= 0:
        test += 4
        i += 1
    return (int(value / 10) - i) * 10 + test

def yearsub(year1, year2):
    month1 = year1 % 10
    month2 = year2 % 10
    test = month1 - month2
    i = 0
    while test <= 0:
        test += 4
        i += 1
    return (int(year1 / 10) - int(year2 / 10) - i) * 4 + test

def get_years(course, qtr_num, curr_yrqtr):
    years = [0]* qtr_num
    for i in range(0, qtr_num):
        if course.crs_avail[i] == "1":
            years[i] = base4sub(curr_yrqtr, i)
    years = list(filter(lambda a: a != 0, years))
    return years
