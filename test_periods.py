import datetime
# import dateutil
from dateutil.relativedelta import relativedelta

def get_new_dates(start_date: datetime.datetime,end_date: datetime.datetime, period: str):
    if period not in ['monthly','quarterly','semi-annually','annually']:
        print("Incorrect period specification\nShould be one of 'monthly', 'quarterly', 'semi-annually', or 'annually'")
        return []
    if start_date > end_date:
        print("Start date cannot be later than End date\nExiting")
        return []
    dates=[]
    previous_date=start_date
    dates.append(previous_date)

    if period=='monthly':
        while True:
            next_date=previous_date+relativedelta(day=31)
            next_date+=relativedelta(days=1)
            next_date=next_date.replace(hour=0,minute=0,second=0,microsecond=0)
            if next_date == end_date:
                dates.append(next_date)
                break
            elif next_date > end_date:
                dates.append(end_date)
                break
            else:
                dates.append(next_date)
                previous_date=next_date
    elif period == 'quarterly':
        if start_date.month in [1,2,3]:
            next_date_month=4
            next_date_year=previous_date.year    
        elif start_date.month in [4,5,6]:
            next_date_month=7
            next_date_year=previous_date.year    
        elif start_date.month in [7,8,9]:
            next_date_month=10
            next_date_year=previous_date.year    
        else:
            next_date_month=1
            next_date_year=previous_date.year+1
        next_date=datetime.datetime(next_date_year,next_date_month,1)
        dates.append(next_date)
        previous_date=next_date
        while True:
            next_date=previous_date+relativedelta(months=3)
            if next_date == end_date:
                dates.append(next_date)
                break
            elif next_date > end_date:
                dates.append(end_date)
                break
            else:
                dates.append(next_date)
                previous_date=next_date
    elif period=='semi-annually':
        if start_date.month in [1,2,3,4,5,6]:
            next_date_month=7
            next_date_year=previous_date.year   
        else:
            next_date_month=1
            next_date_year=previous_date.year+1
        next_date=datetime.datetime(next_date_year,next_date_month,1)
        dates.append(next_date)
        previous_date=next_date
        while True:
            next_date=previous_date+relativedelta(months=6)
            if next_date == end_date:
                dates.append(next_date)
                break
            elif next_date > end_date:
                dates.append(end_date)
                break
            else:
                dates.append(next_date)
                previous_date=next_date
    elif period=='annually':
        while True:
            next_date=datetime.datetime(previous_date.year+1,1,1,0,0,0)
            if next_date == end_date:
                dates.append(next_date)
                break
            elif next_date > end_date:
                dates.append(end_date)
                break
            else:
                dates.append(next_date)
                previous_date=next_date
    return dates      





start_date=datetime.datetime.now()
end_date=datetime.datetime(2030,6,5)
print(start_date,end_date)

new_dates=get_new_dates(end_date,start_date,'annually')
for date in new_dates:
    print(date)
pass
# print('\n\nDates by month\n')
# dates=[]

# previous_date=start_date
# dates.append(previous_date)

# while True:
#   next_date=previous_date+relativedelta(day=31)
#   next_date+=relativedelta(days=1)
#   next_date=next_date.replace(hour=0,minute=0,second=0,microsecond=0)
#   if next_date == end_date:
#     dates.append(next_date)
#     break
#   elif next_date > end_date:
#     dates.append(end_date)
#     break
#   else:
#     dates.append(next_date)
#     previous_date=next_date
# for date in dates:
#     print(date)

# print('\n\nDates by quarter\n')
# dates=[]
# previous_date=start_date
# dates.append(previous_date)
# if start_date.month in [1,2,3]:
#     next_date_month=4
#     next_date_year=previous_date.year    
# elif start_date.month in [4,5,6]:
#     next_date_month=7
#     next_date_year=previous_date.year    
# elif start_date.month in [7,8,9]:
#     next_date_month=10
#     next_date_year=previous_date.year    
# else:
#     next_date_month=1
#     next_date_year=previous_date.year+1
# next_date=datetime.datetime(next_date_year,next_date_month,1)
# dates.append(next_date)
# previous_date=next_date
# while True:
#     next_date=previous_date+relativedelta(months=3)
#     if next_date == end_date:
#         dates.append(next_date)
#         break
#     elif next_date > end_date:
#         dates.append(end_date)
#         break
#     else:
#         dates.append(next_date)
#         previous_date=next_date    
# for date in dates:
#     print(date)

# print('\n\nDates by half-year\n')
# dates=[]
# previous_date=start_date
# dates.append(previous_date)
# if start_date.month in [1,2,3,4,5,6]:
#     next_date_month=7
#     next_date_year=previous_date.year   
# else:
#     next_date_month=1
#     next_date_year=previous_date.year+1
# next_date=datetime.datetime(next_date_year,next_date_month,1)
# dates.append(next_date)
# previous_date=next_date
# while True:
#     next_date=previous_date+relativedelta(months=6)
#     if next_date == end_date:
#         dates.append(next_date)
#         break
#     elif next_date > end_date:
#         dates.append(end_date)
#         break
#     else:
#         dates.append(next_date)
#         previous_date=next_date    
# for date in dates:
#     print(date)

# print('\n\nDates by year\n')
# dates=[]
# previous_date=start_date
# dates.append(previous_date)
# while True:
#     next_date=datetime.datetime(previous_date.year+1,1,1,0,0,0)
#     if next_date == end_date:
#         dates.append(next_date)
#         break
#     elif next_date > end_date:
#         dates.append(end_date)
#         break
#     else:
#         dates.append(next_date)
#         previous_date=next_date    
# for date in dates:
#     print(date)