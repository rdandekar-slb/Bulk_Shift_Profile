import openpyxl as xl
import datetime
import pandas as pd
import numpy


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


def lin_int(x_arr,y_arr,x):
    if x<=x_arr[0]:
        return y_arr[0]
    if x>=x_arr[-1]:
        return y_arr[-1]

    for i in range(1,len(x_arr)-1):
        if x<=x_arr[i] and x>x_arr[i-1]:
            return y_arr[i-1]+((y_arr[i]-y_arr[i-1])/(x_arr[i]-x_arr[i-1]))*(x-x_arr[i-1])


def dates_bulk_shifted(workbook, worksheet,days):
  df=pd.read_excel(workbook,sheet_name=worksheet,header=[0,1],index_col=0,parse_dates=True)
  req_df=pd.DataFrame(df.loc[slice(None),(slice(None),['CUMGAS','CUMOIL','CUMWAT'])])
  del df
  if req_df.empty:
    return

  required_columns=req_df.columns.values
  data_values=req_df.values
  data_arrays=[[data_values[i,j] for i in range(len(data_values))] for j in range(len(required_columns))]
  dates_list=req_df.index.values
  print(dates_list.max(), dates_list.min())
  days_from_start=[(i-dates_list[0])/numpy.timedelta64(1,'D') for i in dates_list]
  for i in range(len(required_columns)):
    shifted_values=[]







print("Hello World")
try:
  workbook=xl.load_workbook(r"C:\Users\rdandekar\Desktop\ProductionProfile.xlsx")
except Exception:
  print('File not found')
  exit()
print(f'Workbook opened \n')


# read bulk shift days from excel_input_sheet
first_row=next(workbook['Bulk_Shift_Input'].rows)
days_to_shift=first_row[1].value
worksheets=workbook.sheetnames
workbook.close()

#for testing
entity_types=['USERDF','SOURCE','SEP','TANK','JOINT','WELL','INLGEN']
entity_dates=[]

for entity_type in entity_types:
  dates_bulk_shifted(r"C:\Users\rdandekar\Desktop\ProductionProfile.xlsx",entity_type,days_to_shift)

print("I am here")

