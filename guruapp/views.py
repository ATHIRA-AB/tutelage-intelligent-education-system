from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,HttpResponseRedirect,render_to_response,redirect
from django.db import connection
import datetime
from time import gmtime, strftime
from guruapp.forms import pform
from guruapp.models import pmodel

# Create your views here.

def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def chatbot(request):
    return render(request,'chatbot.html')

def adminHome(request):
    return render(request,'adminHome.html')

def studentHome(request):
    return render(request,'studentHome.html')


def facultyHome(request):
    return render(request,'facultyHome.html')

def Course(request):
    cur=connection.cursor()
    s="select * from tbl_dept"
    cur.execute(s)
    dept=[]
    result=cur.fetchall()
    for row in result:
        w={'dname':row[0]}
        dept.append(w)
    s="select * from tbl_course"
    cur.execute(s)
    list=[]
    result=cur.fetchall()
    for row in result:
        w={'ccode':row[0],'cname':row[1],'dname':row[2],'nos':row[3]}
        list.append(w)
    return render(request, 'Course.html',{'list':list,'dept':dept})

def courseaction(request):
    cur=connection.cursor()
    coc=request.GET['cou_code']
    cn=request.GET['cou_name']
    dep=request.GET['Department']
    sem=request.GET['cou_sem']
    
    
    s="select * from tbl_course where ccode='%s' or cname='%s'"%(coc,cn)
    cur.execute(s)
    if(cur.rowcount>0):
        st="<script>alert('already exists');window.location='/Course/'</script>"
        return HttpResponse(st)
    else:
        sql="insert into tbl_course values('%s','%s','%s','%s')"%(coc,cn,dep,sem)
        cur.execute(sql)
    s="select * from tbl_dept"
    cur.execute(s)
    dept=[]
    result=cur.fetchall()
    for row in result:
        w={'dname':row[0]}
        dept.append(w)
    s="select * from tbl_course"
    cur.execute(s)
    list=[]
    result=cur.fetchall()
    for row in result:
        w={'ccode':row[0],'cname':row[1],'dname':row[2],'nos':row[3]}
        list.append(w)
    return render(request, 'Course.html',{'list':list,'dept':dept})

def delcou(request):
    id=request.GET['d']	
    cur=connection.cursor()
    s="delete from  tbl_course where ccode='%s'"%(id)
    cur.execute(s)
    s="select * from tbl_dept"
    cur.execute(s)
    dept=[]
    result=cur.fetchall()
    for row in result:
        w={'dname':row[0]}
        dept.append(w)
                                                                                                                                                                                                
    return render(request, 'Course.html',{'list':list,'dept':dept})

def department(request):
    cur=connection.cursor()
    s="select * from tbl_dept"
    cur.execute(s)
    list=[]
    result=cur.fetchall()
    for row in result:
        w={'dname':row[0]}
        list.append(w)
    return render(request, 'department.html',{'list':list})

def deldpt(request):
    id=request.GET['dn']	
    cur=connection.cursor()
    s="delete from  tbl_dept where dname='%s'"%(id)
    cur.execute(s)
    s="select * from tbl_dept"
    cur.execute(s)
    list=[]
    result=cur.fetchall()
    for row in result:
        w={'dname':row[0]}
        list.append(w)
    return render(request, 'department.html',{'list':list})


def deptaction(request):
    cur=connection.cursor()
    n=request.GET['d']
    
    sql3="select * from tbl_dept where dname='%s'"%(n)
    cur.execute(sql3)
    rm=cur.fetchall()
    if(cur.rowcount)>0:
        st="<script>alert('department already exists');window.location='/department/'</script>"
        return HttpResponse(st)
    else:
        sql="insert into tbl_dept (dname)values('%s')"%(n)
        cur.execute(sql)
        h="<script>alert('Successfully inserted');window.location='/department/'</script>"
    return HttpResponse(h)

def Faculty(request):
    cur=connection.cursor()
    s="select * from tbl_dept"
    cur.execute(s)
    dept=[]
    result=cur.fetchall()
    for row in result:
        w={'dname':row[0]}
        dept.append(w)
    s="select * from tbl_faculty"
    cur.execute(s)
    list=[]
    result=cur.fetchall()
    for row in result:
        w={'fid':row[0],'fname':row[1],'adr':row[2],'phn':row[3],'em':row[4],'gen':row[5],'dname':row[6]}
        list.append(w)
    return render(request, 'Faculty.html',{'list':list,'dept':dept})

def facaction(request):
    cur=connection.cursor()
    fn = request.GET['fac_name']
    add = request.GET['address']
    ph = request.GET['phone']
    em = request.GET['email']
    gen = request.GET['gender']
    dep = request.GET['Department']
    pas = request.GET['password']

    s1="select * from tbl_faculty where em='%s'"%(em)
    cur.execute(s1)
    if(cur.rowcount>0):
        h="<script>alert('Already Exists');window.location='/Faculty/'</script>"
        return HttpResponse(h)
    else:
        sql = "insert into tbl_faculty values(null,'%s','%s','%s','%s','%s','%s')"%(fn,add,ph,em,gen,dep)
        cur.execute(sql)
        sql1 = "SELECT max(fid) as fid from tbl_faculty"
        cur.execute(sql1)
    
        result=cur.fetchall()
        for row in result:
            sql2 = "insert into tbl_login values('%s','%s','%s','faculty')"%(row[0],em,pas)
            cur.execute(sql2)
    s="select * from tbl_dept"
    cur.execute(s)
    dept=[]
    result=cur.fetchall()
    for row in result:
        w={'dname':row[0]}
        dept.append(w)
    s="select * from tbl_faculty"
    cur.execute(s)
    list=[]
    result=cur.fetchall()
    for row in result:
        w={'fid':row[0],'fname':row[1],'adr':row[2],'phn':row[3],'em':row[4],'gen':row[5],'dname':row[6]}
        list.append(w)
    
    return render(request, 'Faculty.html',{'list':list,'dept':dept})
       

def delfac(request):
    id=request.GET['d']	
    cur=connection.cursor()
    s="delete from  tbl_faculty where fid='%s'"%(id)
    cur.execute(s)
    s="select * from tbl_dept"
    cur.execute(s)
    dept=[]
    result=cur.fetchall()
    for row in result:
        w={'dname':row[0]}
        dept.append(w)
    s="select * from tbl_faculty"
    cur.execute(s)
    list=[]
    result=cur.fetchall()
    for row in result:
        w={'fid':row[0],'fname':row[1],'adr':row[2],'phn':row[3],'em':row[4],'gen':row[5],'dname':row[6]}
        list.append(w)
    return render(request, 'Faculty.html',{'list':list,'dept':dept})

def facultyHome(request):
    return render(request,'facultyHome.html')

def student(request):
    cur=connection.cursor()

    cco=[]
    s="select * from tbl_course"
    cur.execute(s)
   
    result=cur.fetchall()
    for row in result:
        w={'ccode':row[0],'cname':row[1],'dname':row[2],'nos':row[3]}
        cco.append(w)
    return render(request, 'student.html',{'cco':cco})

def vstudent(request):
    cur=connection.cursor()
    cc=request.GET['cc']
   
    s="select * from tbl_student where ccode='%s'"%(cc)
    cur.execute(s)
    list=[]
    result=cur.fetchall()
    for row in result:
        w={'stname':row[1],'stadr':row[2],'gen':row[3],'ccode':row[4],'sem':row[5],'uregno':row[6],'phn':row[7],'email':row[8]}
        list.append(w)
    return render(request, 'vstudent.html',{'list':list})

def studaction(request):
    cur=connection.cursor()
    stn = request.GET['std_name']
    sta = request.GET['address']
    gen = request.GET['gender']
    cco = request.GET['Course_Code']
    sem = request.GET['sem']
    ure = request.GET['regno']
    phn = request.GET['phone']
    ema = request.GET['email']
    
    s1="select * from tbl_student where uregno='%s'"%(ure)
    cur.execute(s1)
    if(cur.rowcount>0):
        html="<script>alert('Already Exists');window.location='/vcourse/'</script>"
    else:
        sql = "insert into tbl_student values(null,'%s','%s','%s','%s','%s','%s','%s','%s')"%(stn,sta,gen,cco,sem,ure,phn,ema)
        cur.execute(sql)
        html="<script>alert('Added');window.location='/vcourse/'</script>"
    return HttpResponse(html)
        

def vcourse(request):
    cur=connection.cursor()
  
    s="select * from tbl_course where dname = (select dname from tbl_faculty where fid=%s)"%(request.session['uid'])
    cur.execute(s)
    list=[]
    result=cur.fetchall()
    for row in result:
        w={'ccode':row[0],'cname':row[1],'dname':row[2],'nos':row[3]}
        list.append(w)
    return render(request, 'vcourse.html',{'list':list})

def vsubject(request):
    cur=connection.cursor()
    cc=request.GET['cc']
    
    s="select * from tbl_subject where ccode='%s'"%(cc)
    cur.execute(s)
    list=[]
    result=cur.fetchall()
    for row in result:
        w={'scode':row[0],'sname':row[1],'ccode':row[2],'sem':row[3]}
        list.append(w)
    return render(request, 'vsubject.html',{'list':list})

def Subject(request):
    cur=connection.cursor()
    cc=request.GET['cc']
    cco=[]
    c={'cc':cc}
    cco.append(c)
    
    s="select * from tbl_subject where ccode='%s'"%(cc)
    cur.execute(s)
    list=[]
    result=cur.fetchall()
    for row in result:
        w={'scode':row[0],'sname':row[1],'ccode':row[2],'sem':row[3]}
        list.append(w)
    return render(request, 'Subject.html',{'list':list,'cco':cco})

def subaction(request):
    cur=connection.cursor()
    s=request.GET['sub_code']
    sn=request.GET['sub_name']
    cc=request.GET['Course_Code']
    sem=request.GET['Sem']
    s1="select * from tbl_subject where scode='%s' and ccode='%s' and sem='%s'"%(s,cc,sem)
    cur.execute(s1)
    if(cur.rowcount>0):
        html="<script>alert('Already Exists');window.location='/Course/'</script>"
        return HttpResponse(html)
    else:
        sql="insert into tbl_subject values('%s','%s','%s','%s')"%(s,sn,cc,sem)
        cur.execute(sql)
    cco=[]
    c={'cc':cc}
    cco.append(c)
    s="select * from tbl_subject where ccode='%s'"%(cc)
    cur.execute(s)
    list=[]
    result=cur.fetchall()
    for row in result:
        w={'scode':row[0],'sname':row[1],'ccode':row[2],'sem':row[3]}
        list.append(w)
    return render(request, 'Subject.html',{'list':list,'cco':cco})


def delsub(request):
    id=request.GET['d']	
    cc=request.GET['cc']	
    cur=connection.cursor()
    s="delete from  tbl_subject where scode='%s'"%(id)
    cur.execute(s)
    cco=[]
    c={'cc':cc}
    cco.append(c)
    s="select * from tbl_subject where ccode='%s'"%(cc)
    cur.execute(s)
    list=[]
    result=cur.fetchall()
    for row in result:
        w={'scode':row[0],'sname':row[1],'ccode':row[2],'sem':row[3]}
        list.append(w)
    return render(request, 'Subject.html',{'list':list,'cco':cco})

def Timetable(request):
    sc=request.GET['d']	
    cc=request.GET['cc']	
    s=request.GET['s']
    list=[]
    w={'sc':sc,'cc':cc,'s':s}
    list.append(w)
    return render(request, 'Timetable.html',{'list':list})

def timeaction(request):
    cur=connection.cursor()
    dat=request.GET['tdate']
    day=request.GET['day']
    cou=request.GET['course']
    sem=request.GET['Sem']
    sub=request.GET['Subject_Name']
    fac=request.session['uid']
    
    sql="insert into tbl_timetable values(null,'%s','%s','%s','%s','%s','%s')"%(dat,day,cou,sem,sub,fac)
    cur.execute(sql)
    return render(request, 'facultyHome.html')

def vtimetable(request):
    cur=connection.cursor()
    list=[]
    sql = "select * from tbl_timetable where fid=%s"%(request.session['uid'])
    cur.execute(sql)
    rs=cur.fetchall()
    for row in rs:
        w={'ttid':row[0],'tdate':row[1].strftime("%Y-%m-%d"),'tday':row[2],'ccode':row[3],'sem':row[4],'scode':row[5]}
        list.append(w)
    return render(request, 'vtimetable.html',{'list':list})

def svtimetable(request):
    uno=request.session['uregno']
    flag=[]
    att=[]
    sd=datetime.date.today()
    dt=[]
    w={'sd':sd}
    dt.append(w)
    cur=connection.cursor()
    sql1 = "SELECT * FROM tbl_student WHERE uregno='%s'"%(request.session['uregno'])
    cur.execute(sql1)
    rs=cur.fetchall()
    for row in rs:
        sql = "select * from tbl_timetable inner join tbl_faculty on tbl_faculty.fid=tbl_timetable.fid where ccode='%s' and sem='%s' order by tdate desc"%(row[4],row[5])
        cur.execute(sql)
        list=[]
    
        rs=cur.fetchall()
        for row in rs:
            w={'ttid':row[0],'tdate':row[1],'tday':row[2],'ccode':row[3],'sem':row[4],'scode':row[5],'fname':row[8]}
            list.append(w)
            s="select * from tbl_att where ttid=%s"%(row[0])
            cur.execute(s)
            if(cur.rowcount>0):
                w={'f':1}
                flag.append(w)
            else:
                w={'f':0}
                flag.append(w)
        
    s="select distinct(ttid) from tbl_att where uregno=%s"%(uno)
    cur.execute(s)
    rs1=cur.fetchall()
    for row1 in rs1:
        w={'ttid':row1[0]}
        att.append(w)

    
    return render(request, 'svtimetable.html',{'list':list,'dt':dt,'flag':flag,'uno':uno,'att':att})

def fvstudent(request):
    cur=connection.cursor()
   
    sql = "select * from tbl_course where dname = (select dname from tbl_faculty where fid=%s)"%(request.session['uid'])
    cco=[]
    cur.execute(sql)
    rs=cur.fetchall()
    for row in rs:
        w={'ccode':row[0],'cname':row[1],'dname':row[2],'nos':row[3]}
        cco.append(w)
   
    
    
    return render(request, 'fvstudent.html',{'cco':cco})

def fvstudent1(request):
    cur=connection.cursor()
    sem=request.GET['sem']
    cc=request.GET['cc']
      
    
    s="select * from tbl_student where ccode='%s' and sem='%s'"%(cc,sem)
    cur.execute(s)
    list=[]
    result=cur.fetchall()
    for row in result:
        w={'stname':row[1],'stadr':row[2],'gen':row[3],'ccode':row[4],'sem':row[5],'uregno':row[6],'phn':row[7],'email':row[8]}
        list.append(w)
    return render(request, 'fvstudent1.html',{'list':list})

def fvatt1(request):
    cur=connection.cursor()
    sem=request.GET['sem']
    cc=request.GET['cc']
    ttid=request.GET['ttid']
      
    
    s = "select * from tbl_student where ccode='%s' and sem='%s' and uregno in (select uregno from tbl_att where ttid='%s')"%(cc,sem,ttid)
    cur.execute(s)
    list=[]
    result=cur.fetchall()
    for row in result:
        w={'stname':row[1],'stadr':row[2],'gen':row[3],'ccode':row[4],'sem':row[5],'uregno':row[6],'phn':row[7],'email':row[8]}
        list.append(w)
    return render(request, 'fvatt1.html',{'list':list})

def notes(request):
    cur=connection.cursor()
    flag=0
    tid = request.GET['d']
    sql = "select * from tbl_timetable where ttid=%s"%(tid)
    cur.execute(sql)
    result=cur.fetchall()
    nt=[]
    for row in result:
        request.session['ttid']=tid
        request.session['cc']=row[3]
        request.session['sc']=row[5]
        w={'ttid':tid,'scode':row[5],'ccode':row[3]}
        nt.append(w)
        
    s1 = "select * from tbl_notes where ttid=%s"%(tid)
    cur.execute(s1)
    rs=cur.fetchall()
    list=[]
    for row in rs:
        w={'nid':row[0],'ccode':row[1],'scode':row[2],'ttid':row[3],'descp':row[4],'path':row[5]}
        list.append(w)

    s2 = "select * from tbl_qns where nid in (select nid from tbl_notes where ttid=%s)"%(tid)
    print s2
    cur.execute(s2)
    print cur.rowcount
    if cur.rowcount>0:
        flag=1
    print flag
    return render(request, 'notes.html',{'list':list,'nt':nt,'flag':flag})

def noteaction(request):
    if request.method == "POST":
        MyProfileForm = pform(request.POST, request.FILES)
        if MyProfileForm.is_valid():
            profile =pmodel()
            profile.ccode = request.POST["cc"]
            profile.scode =request.POST["sc"]
            profile.ttid =request.POST["ttid"]
            profile.descp =request.POST["descp"]
            
            profile.path = MyProfileForm.cleaned_data["path"]
           
            profile.save()
            html = "<script>alert('successfully added! ');window.location='/facultyHome/';</script>"
            saved = True
	else:
		MyProfileForm = pform()
	return HttpResponse(html)

def adqns(request):
    cur=connection.cursor()
    flag=0
    nid = request.GET['d']
    s1 = "select * from tbl_qns where nid=%s"%(nid)
    cur.execute(s1)
    rs=cur.fetchall()
    list=[]
    for row in rs:
        w={'qid':row[0],'nid':row[1],'q1':row[2],'q2':row[3],'q3':row[4],'q4':row[5],'q5':row[6]}
        list.append(w)
    return render(request, 'adqns.html',{'list':list,'nid':nid})

def chat(request):
    cur=connection.cursor()
    
    nid = request.GET['id']
    s1 = "select * from tbl_chat where nid=%s"%(nid)
    cur.execute(s1)
    rs=cur.fetchall()
    list=[]
    for row in rs:
        w={'chid':row[0],'nid':row[1],'chat':row[2],'ctype':row[3],'uregno':row[4]}
        list.append(w)
    return render(request, 'chat.html',{'list':list,'nid':nid})

def chataction(request):
    cur=connection.cursor()
    nid=request.GET['nid']
    msg=request.GET['msg']
    uregno=request.session['uregno']
    ctype="student"
    
    
    sql="insert into tbl_chat values(null,'%s','%s','%s','%s')"%(nid,msg,ctype,uregno)
    cur.execute(sql)
    s1 = "select * from tbl_chat where nid=%s"%(nid)
    cur.execute(s1)
    rs=cur.fetchall()
    list=[]
    for row in rs:
        w={'chid':row[0],'nid':row[1],'chat':row[2],'ctype':row[3],'uregno':row[4]}
        list.append(w)
    return render(request, 'chat.html',{'list':list,'nid':nid})

def vchat(request):
    cur=connection.cursor()
    
    nid = request.GET['id']
    s1 = "select * from tbl_chat where nid=%s"%(nid)
    cur.execute(s1)
    rs=cur.fetchall()
    list=[]
    for row in rs:
        w={'chid':row[0],'nid':row[1],'chat':row[2],'ctype':row[3],'uregno':row[4]}
        list.append(w)
    return render(request, 'vchat.html',{'list':list,'nid':nid})

def vchataction(request):
    cur=connection.cursor()
    nid=request.GET['nid']
    msg=request.GET['msg']
    uregno=request.session['uid']
    ctype="faculty"
    
    
    sql="insert into tbl_chat values(null,'%s','%s','%s','%s')"%(nid,msg,ctype,uregno)
    cur.execute(sql)
    s1 = "select * from tbl_chat where nid=%s"%(nid)
    cur.execute(s1)
    rs=cur.fetchall()
    list=[]
    for row in rs:
        w={'chid':row[0],'nid':row[1],'chat':row[2],'ctype':row[3],'uregno':row[4]}
        list.append(w)
    return render(request, 'vchat.html',{'list':list,'nid':nid})

def vqns(request):
    cur=connection.cursor()
    s="select ttid from tbl_att where atid=(select max(atid) from tbl_att)"
    cur.execute(s)
    rs1=cur.fetchall()
    for rw in rs1:
        ttid=rw[0]

    s1 = "select * from tbl_qns where nid in (select nid from tbl_notes where ttid=%s)"%(ttid)
    cur.execute(s1)
    rs=cur.fetchall()
    list=[]
    for row in rs:
        w={'qid':row[0],'nid':row[1],'q1':row[2],'q2':row[3],'q3':row[4],'q4':row[5],'q5':row[6]}
        list.append(w)
    return render(request, 'vqns.html',{'list':list})

def qnaction(request):
    cur=connection.cursor()
    nid=request.GET['nid']
    q1=request.GET['q1']
    q2=request.GET['q2']
    q3=request.GET['q3']
    q4=request.GET['q4']
    q5=request.GET['q5']
    
    sql="insert into tbl_qns values(null,'%s','%s','%s','%s','%s','%s')"%(nid,q1,q2,q3,q4,q5)
    cur.execute(sql)
    return render(request, 'facultyHome.html')


def ansaction(request):
    cur=connection.cursor()
    qid=request.GET['qid']
    q1=request.GET['q1']
    q2=request.GET['q2']
    q3=request.GET['q3']
    q4=request.GET['q4']
    q5=request.GET['q5']
    uregno=request.session['uregno']
    sql="insert into tbl_ans values(null,'%s','%s','%s','%s','%s','%s','%s')"%(qid,q1,q2,q3,q4,q5,uregno)
    cur.execute(sql)
    return render(request, 'studentHome.html')

def vnotes(request):
    cur=connection.cursor()
    flag=0
    tid = request.GET['d']
    sql = "select * from tbl_timetable where ttid=%s"%(tid)
    cur.execute(sql)
    result=cur.fetchall()
    for row in result:
        request.session['ttid']=tid
        request.session['cc']=row[3]
        request.session['sc']=row[5]
        
    s1 = "select * from tbl_notes where ttid=%s"%(tid)
    cur.execute(s1)
    rs=cur.fetchall()
    list=[]
    for row in rs:
        w={'nid':row[0],'ccode':row[1],'scode':row[2],'ttid':row[3],'descp':row[4],'path':row[5]}
        list.append(w)
    return render(request, 'vnotes.html',{'list':list})

def stvtimetable(request):
    cur=connection.cursor()
   
    tid = request.GET['d']
    
        
    s1 = "select * from tbl_notes where ttid=%s"%(tid)
    cur.execute(s1)
    rs=cur.fetchall()
    list=[]
    for row in rs:
        w={'nid':row[0],'ccode':row[1],'scode':row[2],'ttid':row[3],'descp':row[4],'path':row[5]}
        list.append(w)
    return render(request, 'stvtimetable.html',{'list':list})

def attaction(request):
    cur=connection.cursor()
    uno=request.session['uregno']
    ttid=request.GET['ttid']
    s="insert into tbl_att values(null,'%s','%s')"%(ttid,uno)
    cur.execute(s)
    html="<script>alert('Attendance Marked');window.location='/vqns/'</script>"
    return HttpResponse(html)

    
def delnot(request):
    id=request.GET['d']	
    cur=connection.cursor()
    s="delete from  tbl_notes where nid='%s'"%(id)
    cur.execute(s)
    list=[]
    sql = "select * from tbl_timetable where fid=%s"%(request.session['uid'])
    cur.execute(sql)
    rs=cur.fetchall()
    for row in rs:
        w={'ttid':row[0],'tdate':row[1],'tday':row[2],'ccode':row[3],'sem':row[4],'scode':row[5]}
        list.append(w)
    return render(request, 'vtimetable.html',{'list':list}) 

def delqns(request):
    id=request.GET['d']	
    cur=connection.cursor()
    s="delete from  tbl_qns where qid='%s'"%(id)
    cur.execute(s)
    html="<script>alert('Deleted');window.location='/facultyHome/'</script>"
    return HttpResponse(html)   

def logaction(request):
	cursor=connection.cursor()
	p=request.GET['n']
	q=request.GET['p']
	sql2="select * from tbl_login where uname='%s'and upass='%s'"%(p,q)
	cursor.execute(sql2)
	rs=cursor.fetchall()
	if(cursor.rowcount)>0:
		sql3="select * from tbl_login where uname='%s' and upass='%s'"%(p,q)
		cursor.execute(sql3)
		rsl=cursor.fetchall()
		for rowl in rsl:
			request.session['uid']=rowl[0]
			request.session['utype']=rowl[3]
		if(request.session['utype']=='admin'):
			return render(request,'adminHome.html')
		if(request.session['utype']=='faculty'):
			return render(request,'facultyHome.html')
        
        
	else:
		html="<script>alert('invalid password and username');window.location='/index/'</script>"
		return HttpResponse(html)

def slogaction(request):
    cursor=connection.cursor()
    n=request.GET['n']
    p=request.GET['p']
    sql2="select * from tbl_student where uregno='%s'and email='%s'"%(p,n)
    cursor.execute(sql2)
    rs=cursor.fetchall()
    if(cursor.rowcount)>0:
        for row1 in rs:
		    request.session['uregno']=row1[6]
		    return render(request,'studentHome.html')
    else:
        html="<script>alert('invalid password and username');window.location='/index/'</script>"
        return HttpResponse(html)
