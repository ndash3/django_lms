from django.shortcuts import render,HttpResponse
from leave_mngt.models import shift_rota as sr
#from django.db.models import Count
#from datetime import datetime as dt
import datetime as dt
#import openpyxl
import pandas as pd
import json

# Create your views here.

def home(request):
    today_date=dt.datetime.now()
    month=today_date.strftime('%B')
    year=today_date.strftime('%Y')
    date=today_date.strftime('%d')
    return render(request,'leave_mngt/homepage.html',{'month':month,'year':year,'date':date})

def shiftrota_view(request):
#     grouped=[day['shift_date'] for day in sr.objects.values('shift_date').annotate(unique_names=Count('shift_date',distinct=True))]
#     day=[i for i in grouped]
#     resource_grouped=[i['Resource_Analyst'] for i in sr.objects.values('Resource_Analyst').annotate(unique_names=Count('Resource_Analyst',distinct=True))]
#     resource=[i for i in resource_grouped]
#     #application_grouped=[i['application'] for i in sr.objects.values('application','Resource_Analyst').annotate(unique_names=Count('Resource_Analyst',distinct=True))]
#     #application=[i for i in application_grouped]
#     application_grouped = [i for i in sr.objects.values('application', 'Resource_Analyst').annotate(unique_names=Count('Resource_Analyst', distinct=True))]
#     application = [i for i in application_grouped]
#     location_groupped=[i for i in sr.objects.values('location','Resource_Analyst').annotate(unique_name=Count('Resource_Analyst',distinct=True))]
#     location=[i for i in location_groupped]

    #obj=sr.objects.all().order_by('-location')
    #return render(request,'leave_mngt/shift.html',{'obj':obj,'day':day,'resource':resource,'application':application,'location':location})
    # wb=openpyxl.load_workbook("leave_data_v2.xlsx")
    # worksheet=wb["Sheet1"]
    # print(worksheet)
    # excel_data=list()
    # for row in worksheet.iter_rows():
    #     row_data=list()
    #     for cell in row:
    #         row_data.append(str(cell.value))
    #     excel_data.append(row_data)
    #return render(request,'leave_mngt/shift.html',{'obj':obj})
    excel_data=pd.read_excel("leave_data_v2.xlsx")
    dt_list=['location','application','Resource_Analyst']
    excel_data=excel_data.rename(columns=lambda x:x.strftime('%d-%b') if x not in dt_list else x)
    today = dt.date.today()
    day1 = today - dt.timedelta(days=today.weekday())
    day2 = day1 + dt.timedelta(days=1)
    day2 = day2.strftime('%d-%b')
    day3 = day1 + dt.timedelta(days=2)
    day3 = day3.strftime('%d-%b')
    day4 = day1 + dt.timedelta(days=3)
    day4 = day4.strftime('%d-%b')
    day5 = day1 + dt.timedelta(days=4)
    day5 = day5.strftime('%d-%b')
    day1 = day1.strftime('%d-%b')
    filtered_columns=['location','application','Resource_Analyst',day1,day2,day3,day4,day5]
    excel_data=excel_data.reindex(columns=filtered_columns)
    #excel_data=excel_data.loc[:,['location','application','Resource_Analyst',day1,day2,day3,day4,day5]]
    #date1=pd.DataFrame(excel_data.columns[3:])
    #date_json_records=date1.reset_index().to_json(orient='records')
    #date=json.loads(date_json_records)
    #day1=[str(row['0']) for row in date]
    day=[i for i in excel_data.columns[3:]]
    json_records=excel_data.reset_index().to_json(orient='records')
    #data=[]
    data=json.loads(json_records)
    #my_list=zip(data,day1)
    context={'df':data,'day':day,'day1':day1}
    #context={'mylist':my_list}
    #df=excel_data.to_html()
    #return HttpResponse(df)
    return render(request, 'leave_mngt/shift_v1.html', context)