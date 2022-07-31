import openpyxl as xl
import datetime
import pandas as pd
import numpy

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
    combined_array=list(zip(days_from_start,data_arrays[i]))

  # new_dates=[datetime.datetime.utcfromtimestamp(i.tolist()/1e9)+datetime.timedelta(days=days_to_shift) for i in dates_list]
  # dates_list=[datetime.datetime.utcfromtimestamp(i.tolist()/1e9) for i in dates_list]



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

