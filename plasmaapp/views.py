
from random import randint
from tkinter import Button
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib import messages
from django.http import HttpResponse
import xlwt
from plasmaapp.models import  *

# Create your views here.
def index(request):
  
    return render(request,'index.html')
def dashboard(request):
    return render(request,'dashboard.html')
 
def pay(request):
    return render(request,'paymentdata.html')
 


  


def reg(request):
  return render(request,'register.html')



def regdata(request):
  return render(request,'registrationdata.html')


  
def regval(request):
  if request.POST:
      tname = request.POST.get('tname')
      mem1name = request.POST.get('mem1')
      mem1email = request.POST.get('mem2')
      mem1phone = request.POST.get('mem3')
      mem1college = request.POST.get('mem4')
      mem1branch = request.POST.get('mem5')
      mem2name = request.POST.get('mem6')
      mem2email = request.POST.get('mem7')
      mem2phone = request.POST.get('mem8')
      mem2college = request.POST.get('mem9')
      mem2branch = request.POST.get('mem10')
      mem3name = request.POST.get('mem11')
      mem3email = request.POST.get('mem12')
      mem3phone = request.POST.get('mem13')
      mem3college = request.POST.get('mem14')
      mem3branch = request.POST.get('mem15')
      mem4name = request.POST.get('mem16')
      mem4email = request.POST.get('mem17')
      mem4phone = request.POST.get('mem18')
      mem4college = request.POST.get('mem19')
      mem4branch = request.POST.get('mem20')
      total = request.POST.get('amount')
      eventnames = request.POST.get('eventname')
      hospital = request.POST.get('selected1')
   
      typeacct = request.POST.get('selected')
      paidamo = request.POST.get('paidamount')
      utrnum = request.POST.get('utrno')
      paydate = request.POST.get('pdate')
      paiby = request.POST.get('paidby')
      if len(request.FILES)!=0:
        photo = request.FILES['fl']
      else:
        return HttpResponse("error")

    
    
      data = registration_details(team_name=tname,member1_name=mem1name,member1_email=mem1email,member1_phone=mem1phone,member1_college=mem1college,member1_branch=mem1branch,member2_name=mem2name,member2_email=mem2email,member2_phone=mem2phone,member2_college=mem2college,member2_branch=mem2branch,member3_name=mem3name,member3_email=mem3email,member3_phone=mem3phone,member3_college=mem3college,member3_branch=mem3branch,member4_name=mem4name,member4_email=mem4email,member4_phone=mem4phone,member4_college=mem4college,member4_branch=mem4branch,total_amount=total,selected_event=eventnames,hospitality=hospital)
      data1 = payment(member1_name=mem1name,member1_email=mem1email,member1_phone=mem1phone,member1_college=mem1college,member1_branch=mem1branch,paid_amount=paidamo,payment_mode=typeacct,payment_date=paydate,paid_by=paiby,utr_upi_no=utrnum,screenshot=photo)
      data.save()
      data1.save()
  
      return render(request,'index.html')



def regfor(request):
  
  if request.POST:
    nam = request.POST.get('names')
    em = request.POST.get('emails')
    sub = request.POST.get('subjects')
    mess = request.POST.get('messages')
  
    u = contact(name=nam,email=em,subject=sub,messages=mess)
    u.save()
    return render(request,'index.html')
  


def regdetails(request):
  if request.POST:
    rej = registration_details.objects.all()
   
    istr = '''
    <table style="height:100%;width:100%;">
    <thead style="">
        <tr> 
            <th>ID</th>
             <th data-type="text-short">Team Name</th>
            <th>Member 1 name</th>
            <th style="padding-right:1.5cm;">Member 1 email</th>
            <th style="padding-right:1.5cm;">Member 1 phone</th>
            <th style="padding-right:1.5cm;">Member 1 college</th>
            <th style="padding-right:1.5cm;">Member 1 branch</th>
                <th style="padding-right:1.5cm;">Member 2 name</th>
            <th >Member 2 email</th>
            <th>Member 2 phone</th>
            <th>Member 2 college</th>
            <th>Member 2 branch</th>
                <th>Member 3 name</th>
            <th>Member 3 email</th>
            <th>Member 3 phone</th>
            <th>Member 3 college</th>
            <th>Member 3 branch</th>
                 <th>Member 4 name</th>
            <th>Member 4 email</th>
            <th>Member 4 phone</th>
            <th>Member 4 college</th>
            <th>Member 4 branch</th>
            
            <th>Total Amount</th>
            <th style="padding-right:2cm;">EVENT Name</th>
            <th>ACCOMODATION</th>
            
          
         
        </tr>
        
        
    </thead>
   
  </table>

  
  
    '''
 
    

       
    for bn in rej:
      
      istr += "<tr><td><br>" + str(bn.unique_id)+"</td><td>"+ bn.team_name +"</td><td>"+bn.member1_name + \
            "</td><td>"+bn.member1_email+ "</td><td>"+str(bn.member1_phone)+ "</td><td>"+bn.member1_branch+ "</td><td>"+bn.member1_college+ "</td><td>"+bn.member2_name + \
            "</td><td>"+bn.member2_email+ "</td><td>"+str(bn.member2_phone)+ "</td><td>"+bn.member2_branch+ "</td><td>"+bn.member2_college+ "</td><td>"+bn.member3_name + \
            "</td><td>"+bn.member3_email+ "</td><td>"+str(bn.member3_phone)+ "</td><td>"+bn.member3_branch+ "</td><td>"+bn.member3_college+ "</td><td>"+bn.member4_name + \
            "</td><td>"+bn.member4_email+ "</td><td>"+str(bn.member4_phone)+ "</td><td>"+bn.member4_branch+ "</td><td>"+bn.member4_college+ "</td><td>"+str(bn.total_amount)+ "</td><td >"+bn.selected_event + "</td><td>"+bn.hospitality+"</td><td> "'</button>'+onclick('''+bn.member1_email''')+  '<button>''submit' ""
 

 
  return HttpResponse(istr) 


def export_users_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="registrationdetails.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users Data') # this will make a sheet named Users Data

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['ID','Team Name', 'Member 1 name', 'Member 1 email', 'Member 1 phone','Member 1 college','Member 1 branch','Member 2 name', 'Member 2 email', 'Member 2 phone','Member 2 college','Member 2 branch','Member 3 name', 'Member 3 email', 'Member 3 phone','Member 3 college','Member 3 branch','Member 4 name', 'Member 4 email', 'Member 4 phone','Member 4 college','Member 4 branch','Total Amount','Event NAmes','Accomodation' ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style) # at 0 row 0 column 

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = registration_details.objects.all().values_list('unique_id','team_name', 'member1_name', 'member1_email', 'member1_phone','member1_college','member1_branch','member2_name', 'member2_email', 'member2_phone','member2_college','member2_branch','member3_name', 'member3_email', 'member3_phone','member3_college','member3_branch','member4_name', 'member4_email', 'member4_phone','member4_college','member4_branch','total_amount','selected_event','hospitality')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)

    return response
  
  

def export_excel2(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="payment.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users Data') # this will make a sheet named Users Data

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Member 1 name', 'Member 1 email', 'Member 1 phone','Member 1 college','Member 1 branch','payment mode','paid amount','utr/unique tra no','payment_date','paid_by','screenshot' ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style) # at 0 row 0 column 

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = payment.objects.all().values_list('member1_name', 'member1_email', 'member1_phone','member1_college','member1_branch','payment_mode','paid_amount','utr_upi_no','payment_date','paid_by','screenshot')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)

    return response


def export_excel3(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="query.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users Data') # this will make a sheet named Users Data

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['NAME','EMAIL','SUBJECT','MESSAGE' ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style) # at 0 row 0 column 

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = contact.objects.all().values_list('name','email','subject','messages')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)

    return response

def paydetails(request):
  if request.POST:
    reji = payment.objects.all()
   
    istr = '''
    <table style="height:100%;width:100%;">
    <thead style="">
        <tr> 
            
            <th>Member 1 name</th>
            <th style="padding-right:1.5cm;">Member 1 email</th>
            <th style="padding-right:1.5cm;">Member 1 phone</th>
            <th style="padding-right:1.5cm;">Member 1 college</th>
            <th style="padding-right:1.5cm;">Member 1 branch</th>
            <th style="padding-right:1.5cm;">Payment Mode</th>
            <th style="padding-right:1.5cm;">Paid_amount</th>
            <th style="padding-right:1.5cm;">UTR/Unique tra num</th>
            
            <th style="padding-right:1.5cm;">payment Date</th>
            <th style="padding-right:1.5cm;">Paid By</th>
            <th style="padding-right:1.5cm;">Screenshot</th>
         
        </tr>
    </thead>
  </table>
  
  
  
    '''
    
    for bn in reji:
      
      istr += "<tr><td><br>"+bn.member1_name + \
            "</td><td>"+bn.member1_email+ "</td><td>"+str(bn.member1_phone)+ "</td><td>"+bn.member1_college+ "</td><td>"+bn.member1_branch+ "</td><td>"+bn.payment_mode + \
            "</td><td>"+str(bn.paid_amount)+"</td><td>"+str(bn.utr_upi_no)+"</td><td>"+str(bn.payment_date)+"</td><td>"+str(bn.paid_by)+"</td><td>"+str(bn.screenshot)+"</td><td>"
            
  return HttpResponse(istr) 




def query(request):
  return render(request,'query.html')
  


def que(request):
  if request.POST:
    reji = contact.objects.all()
   
    istr = '''
    <table style="height:100%;width:100%;">
    <thead style="">
        <tr> 
            
            <th>NAME</th>
            <th style="padding-right:1.5cm;">EMAIL</th>
            <th style="padding-right:1.5cm;">SUBJECT</th>
            <th style="padding-right:1.5cm;">MESSAGES</th>
         
         
        </tr>
    </thead>
  </table>
  
  
  
    '''
    
    for bn in reji:
      
      istr += "<tr><td><br>"+bn.name + \
            "</td><td>"+bn.email+ "</td><td>"+str(bn.subject)+"</td><td>"+bn.messages
            
  return HttpResponse(istr) 