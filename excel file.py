                                                #DATA ANALYSIS PROJECT-1
                    
'''
#creating mysql by using faker
import numpy as np
import pandas as pd
import pymysql
import faker
fake=faker.Faker()
connection=pymysql.connect(host='localhost',user='root',password='root',db='fakedb',charset='utf8')
c=connection.cursor()
first_name=[]
last_name=[]
email_id=[]
salary=[]
bonus=[]
exp=[]
skill=[]
company_name=[]
emi=[]
height=[]
gender=[]
monthly_expenses=[]
maritalStatus=[]
company_location=[]
hometown=[]
qualification=[]
percentage=[]
passedoutyear=[]
ownHouse=[]
ownCar=[]
age=[]
for i in range(10):
    first_name.append(fake.first_name())
    last_name.append(fake.last_name())
    email_id.append(fake.email())
    salary.append(fake.random_element(elements=(10000,15000,18000,17000,25000,30000,100000)))
    bonus.append(fake.random_element(elements=(500,1000,1500,2000,3000,4000,5000)))
    exp.append(fake.random_element(elements=(0,4,3,5,8,9,3,2,10)))
    skill.append(fake.random_element(elements=('C','C++','Python','Java','PHP','devops','Aws','Powerbi','Mysql','Sql server')))
    company_name.append(fake.random_element(elements=('TCS', 'Wipro', 'CTS', 'Infosys', 'PTG', 'NTH', 'microsoft', 'accenture', 'dell', 'hp', 'capgemini')))
    emi.append(fake.random_element(elements=(500,1000,2000,3000,4000)))
    height.append(fake.random_element(elements=(4.5,4.8,5.0,5.5,5.8,6.0,6.6,7.0)))
    gender.append(fake.random_element(elements=('Male','Female')))
    monthly_expenses.append(fake.random_element(elements=(10000,15000,20000,25000,30000,35000,40000,45000,50000)))
    maritalStatus.append(fake.random_element(elements=('yes','No')))
    company_location.append(fake.random_element(elements=('Hyd','Bang','Mumbai','Chennai','Delhi','pune','kalkata','guntur')))
    hometown.append(fake.random_element(elements=('Hyd','Bang','Mumbai','Chennai','Delhi','pune','kalkata','guntur')))
    qualification.append(fake.random_element(elements=('BTech','MTech','Degree','MCA','Diploma','bca')))
    percentage.append(fake.random_element(elements=(90,95,89,84,86,99,98,100)))
    passedoutyear.append(fake.random_element(elements=(2011,2015,2017,2020, 2021,2023,2024)))
    ownHouse.append(fake.random_element(elements=('Yes','No')))
    ownCar.append(fake.random_element(elements=('Yes','No')))
    age.append(fake.random_element(elements=(20,22,24,25,28,29,30,35)))
students={'first_name':first_name,'last_name':last_name,'email_id':email_id,'salary':salary,'bonus':bonus,'exp':exp,'skill':skill,'company_name':company_name,
          'emi':emi,'height':height,'gender':gender,'monthly_expenses':monthly_expenses,'maritalStatus':maritalStatus,'company_location':company_location,
          'hometown':hometown,'qualification':qualification,'percentage':percentage,'passedoutyear':passedoutyear,'ownHouse':ownHouse,'ownCar':ownCar,'age':age}
mdf=pd.DataFrame(students)
print(mdf)
for i,j in mdf.iterrows():
    c.execute("insert into fakedata values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
              (j.first_name,j.last_name,j.email_id,j.salary,j.bonus,j.exp,j.skill,j.company_name,j.emi,j.height,j.gender,j.monthly_expenses,j.maritalStatus,
               j.company_location,j.hometown,j.qualification,j.percentage,j.passedoutyear,j.ownHouse,j.ownCar,j.age))
    connection.commit()
       

#creating text file by using faker 
import faker
fake=faker.Faker()
with open('fakedata.txt','w') as f:
    for i in range(10):
        first_name=fake.first_name()
        last_name=fake.last_name()
        email_id=fake.email()
        salary=fake.random_element(elements=(10000,15000,18000,17000,25000,30000,100000))
        bonus=fake.random_element(elements=(500,800,600,900,1000,1500,5000,3000))
        exp=fake.random_element(elements=(14,12,10,8,6,4,2,0))
        skill=fake.random_element(elements=('C', 'C++', 'Java', 'Python', 'PHP', 'devops', 'aws', 'powerbi', 'mysql', 'sql','server'))
        company_name=fake.random_element(elements=('TCS', 'Wipro', 'CTS', 'Infosys', 'PTG', 'NTH', 'microsoft', 'accenture', 'dell', 'hp', 'capgemini')) 
        emi=fake.random_element(elements=(500,1000,1500,2000,2500,3000,3500,4000,4500,5000))
        height=fake.random_element(elements=(4.5,4.8,5.0,5.2,5.5,5.8,6.0,6.3,6.6,7.0))
        gender=fake.random_element(elements=('Male','Female'))
        monthly_expenses=fake.random_element(elements=(10000,15000,20000,25000,30000,350000,40000,45000,50000))
        maritalStatus=fake.random_element(elements=('yes','No'))
        company_location=fake.random_element(elements=('Hyderabad', 'bangalore', 'chennai', 'mumbai', 'pune', 'kalkata', 'delhi', 'guntur'))
        hometown=fake.random_element(elements=('Hyderabad', 'bangalore', 'chennai', 'mumbai', 'pune', 'kalkata', 'delhi', 'guntur'))
        qualification=fake.random_element(elements=('Btech', 'Mtech', 'Mca', 'Degree', 'Diploma', 'bca'))
        percentage=fake.random_element(elements=(70,80,97,65,99,88,95,72,79,86))
        passedoutyear=fake.random_element(elements=(2010,2012,2014,2016,2018,2020,2022,2024))
        ownHouse=fake.random_element(elements=('yes','No'))
        ownCar=fake.random_element(elements=('yes','No'))
        age=fake.random_element(elements=(44,40,36,32,29,25))
        f.write(f'{first_name},{last_name},{email_id},{salary},{bonus},{exp},{skill},{company_name},{emi},{height},{gender},{monthly_expenses},{maritalStatus},{company_location},{hometown},{qualification},{percentage},{passedoutyear},{ownHouse},{ownCar},{age}\n')


#creating sql server by using faker
import pandas as pd
import numpy as np
import pymysql
import pypyodbc as odbc
import faker
fake=faker.Faker()
a=odbc.connect('DRIVER={SQL Server}; Server=GNAGAMANI\SQLEXPRESS; Database=fakedb')
c=a.cursor()

for i in range(10):
    first_name=fake.first_name()
    last_name=fake.last_name()
    email_id=fake.email()
    salary=fake.random_element(elements=(10000,15000,18000,17000,25000,30000,100000))
    bonus=fake.random_element(elements=(500,800,600,1000,1500,5000,3000))
    exp=fake.random_element(elements=(14,12,10,8,6,4,2,0))
    skill=fake.random_element(elements=('C', 'C++', 'Java', 'Python', 'PHP', 'devops', 'aws', 'powerbi', 'mysql', 'sql server'))
    company_name=fake.random_element(elements=('TCS', 'Wipro', 'CTS', 'Infosys', 'PTG', 'NTH', 'microsoft', 'accenture', 'dell', 'hp', 'capgemini'))
    emi=fake.random_element(elements=(500,1000,1500,2000,2500,3000,3500,4000,4500,5000))
    height=fake.random_element(elements=(4.5,4.8,5.0,5.5,5.8,6.0,6.6,7.0))
    gender=fake.random_element(elements=('Male','Female'))
    monthly_expenses=fake.random_element(elements=(10000,15000,20000,25000,30000,35000,40000,45000,50000))
    maritalStatus=fake.random_element(elements=('Yes','No'))
    company_location=fake.random_element(elements=('Hyderabad', 'bangalore', 'chennai', 'mumbai', 'pune', 'kalkata', 'delhi', 'guntur'))
    hometown=fake.random_element(elements=('Hyderabad', 'bangalore', 'chennai', 'mumbai', 'pune', 'kalkata', 'delhi', 'guntur'))
    qualification=fake.random_element(elements=('btech', 'mtech', 'mca', 'degree', 'diploma', 'bca'))
    percentage=fake.random_element(elements=(70,80,65,99,98,72,79,86))
    passedoutyear=fake.random_element(elements=(2010,2014,2016,2018,2020,2022,2024))
    ownHouse=fake.random_element(elements=('Yes','No'))
    ownCar=fake.random_element(elements=('Yes','No'))
    age=fake.random_element(elements=(44,40,36,32,29,25))

    c.execute("insert into fakedata values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
              (first_name,last_name,email_id,salary,bonus,exp,skill,company_name,emi,height,gender,monthly_expenses,maritalStatus,
               company_location,hometown,qualification,percentage,passedoutyear,ownHouse,ownCar,age))
a.commit()



#create excel by using faker
import pandas as pd
import numpy as np
import pymysql
import faker
from openpyxl import Workbook
fake=faker.Faker()
wb=Workbook()
sheet=wb.active
for i in range(10):
    sheet.append([
    fake.first_name(),
    fake.last_name(),
    fake.email(),
    fake.random_element(elements=(10000,15000,18000,17000,25000,30000,100000)),
    fake.random_element(elements=(500,800,600,1000,1500,5000,3000)),
    fake.random_element(elements=(14,12,10,8,6,4,2,0)),
    fake.random_element(elements=('C', 'C++', 'Java', 'Python', 'PHP', 'devops', 'aws', 'powerbi', 'mysql', 'sql server')),
    fake.random_element(elements=('TCS', 'Wipro', 'CTS', 'Infosys', 'PTG', 'NTH', 'microsoft', 'accenture', 'dell', 'hp', 'capgemini')),
    fake.random_element(elements=(500,1000,1500,2000,2500,3000,3500,4000,4500,5000)),
    fake.random_element(elements=(4.5,4.8,5.0,5.5,5.8,6.0,6.6,7.0)),
    fake.random_element(elements=('Male','Female')),
    fake.random_element(elements=(10000,15000,20000,25000,30000,35000,40000,45000,50000)),
    fake.random_element(elements=('Yes','No')),
    fake.random_element(elements=('Hyderabad', 'bangalore', 'chennai', 'mumbai', 'pune', 'kalkata', 'delhi', 'guntur')),
    fake.random_element(elements=('Hyderabad', 'bangalore', 'chennai', 'mumbai', 'pune', 'kalkata', 'delhi', 'guntur')),
    fake.random_element(elements=('btech', 'mtech', 'mca', 'degree', 'diploma', 'bca')),
    fake.random_element(elements=(70,80,65,99,98,72,79,86)),
    fake.random_element(elements=(2010,2014,2016,2018,2020,2022,2024)),
    fake.random_element(elements=('Yes','No')),
    fake.random_element(elements=('Yes','No')),
    fake.random_element(elements=(44,40,36,32,29,25))])
    wb.save('fakedata.xlsx')
    edf=pd.read_excel(io='c:\\Users\\gugul\\AppData\\Local\\Programs\\Python\\Python312\\fakedata.xlsx')
    print(edf)

'''
#DATA FRAMES
#Creating MYSQL to DataFrame
#pymysql
import pymysql
import numpy as np
import pypyodbc as odbc
import pandas as pd
import faker
fake=faker.Faker()
connection=pymysql.connect(host='localhost',user='root',password='root',db='fakedb',charset='utf8')
c=connection.cursor()
c.execute('select * from fakedata')
data=c.fetchall()
first_name=[]
last_name=[]
email_id=[]
salary=[]
bonus=[]
exp=[]
skill=[]
company_name=[]
emi=[]
height=[]
gender=[]
monthly_expenses=[]
maritalStatus=[]
company_location=[]
hometown=[]
qualification=[]
percentage=[]
passedoutyear=[]
ownHouse=[]
ownCar=[]
age=[]
for i in data:
    first_name.append(i[0])
    last_name.append(i[1])
    email_id.append(i[2])
    salary.append(i[3])
    bonus.append(i[4])
    exp.append(i[5])
    skill.append(i[6])
    company_name.append(i[7])
    emi.append(i[8])
    height.append(i[9])
    gender.append(i[10])
    monthly_expenses.append(i[11])
    maritalStatus.append(i[12])
    company_location.append(i[13])
    hometown.append(i[14])
    qualification.append(i[15])
    percentage.append(i[16])
    passedoutyear.append(i[17])
    ownHouse.append(i[18])
    ownCar.append(i[19])
    age.append(i[20])
students={'first_name':first_name,'last_name':last_name,'email_id':email_id,'salary':salary,'bonus':bonus,'exp':exp,'skill':skill,
          'company_name':company_name,'emi':emi,'height':height,'gender':gender,'monthly_expenses':monthly_expenses,'maritalStatus':
          maritalStatus,'company_location':company_location,'hometown':hometown,'qualification':qualification,'percentage':percentage,
          'passedoutyear':passedoutyear,'ownHouse':ownHouse,'ownCar':ownCar,'age':age}
mdf=pd.DataFrame(data=students)
print(mdf)

#Creating Textfile to DataFrame
import pandas as pd
x=open('fakedata.txt','r').read().split('\n')
first_name=[]
last_name=[]
email_id=[]
salary=[]
bonus=[]
exp=[]
skill=[]
company_name=[]
emi=[]
height=[]
gender=[]
monthly_expenses=[]
maritalStatus=[]
company_location=[]
hometown=[]
qualification=[]
percentage=[]
passedoutyear=[]
ownHouse=[]
ownCar=[]
age=[]
for i in x:
    y=i.split(',')
    first_name.append(y[0])
    last_name.append(y[1])
    email_id.append(y[2])
    salary.append(y[3])
    bonus.append(y[4])
    exp.append(y[5])
    skill.append(y[6])
    company_name.append(y[7])
    emi.append(y[8])
    height.append(y[9])
    gender.append(y[10])
    monthly_expenses.append(y[11])
    maritalStatus.append(y[12])
    company_location.append(y[13])
    hometown.append(y[14])
    qualification.append(y[15])
    percentage.append(y[16])
    passedoutyear.append(y[17])
    ownHouse.append(y[18])
    ownCar.append(y[19])
    age.append(y[20])

students2={'first_name':first_name,'last_name':last_name,'email_id':email_id,'salary':salary,'bonus':bonus,'exp':exp,'skill':skill,
          'company_name':company_name,'emi':emi,'height':height,'gender':gender,'monthly_expenses':monthly_expenses,'maritalStatus':
          maritalStatus,'company_location':company_location,'hometown':hometown,'qualification':qualification,'percentage':percentage,
          'passedoutyear':passedoutyear,'ownHouse':ownHouse,'ownCar':ownCar,'age':age}
tdf=pd.DataFrame(data=students2)
print(tdf)

#Creating Sql Sever to DataFrame
import pypyodbc as odbc
import pandas as pd
a=odbc.connect('DRIVER={SQL Server}; Server=GNAGAMANI\SQLEXPRESS; Database=fakedb')
c=a.cursor()
c.execute('select*from fakedata')
data=c.fetchall()
first_name=[]
last_name=[]
email_id=[]
salary=[]
bonus=[]
exp=[]
skill=[]
company_name=[]
emi=[]
height=[]
gender=[]
monthly_expenses=[]
maritalStatus=[]
company_location=[]
hometown=[]
qualification=[]
percentage=[]
passedoutyear=[]
ownHouse=[]
ownCar=[]
age=[]
for i in data:
    first_name.append(i[0])
    last_name.append(i[1])
    email_id.append(i[2])
    salary.append(i[3])
    bonus.append(i[4])
    exp.append(i[5])
    skill.append(i[6])
    company_name.append(i[7])
    emi.append(i[8])
    height.append(i[9])
    gender.append(i[10])
    monthly_expenses.append(i[11])
    maritalStatus.append(i[12])
    company_location.append(i[13])
    hometown.append(i[14])
    qualification.append(i[15])
    percentage.append(i[16])
    passedoutyear.append(i[17])
    ownHouse.append(i[18])
    ownCar.append(i[19])
    age.append(i[20])
students3={'first_name':first_name,'last_name':last_name,'email_id':email_id,'salary':salary,'bonus':bonus,'exp':exp,'skill':skill,
          'company_name':company_name,'emi':emi,'height':height,'gender':gender,'monthly_expenses':monthly_expenses,'maritalStatus':
          maritalStatus,'company_location':company_location,'hometown':hometown,'qualification':qualification,'percentage':percentage,
          'passedoutyear':passedoutyear,'ownHouse':ownHouse,'ownCar':ownCar,'age':age}
sdf=pd.DataFrame(data=students3)
print(sdf)

#Creating Excelto DataFrame
import pandas as pd
import faker
fake=faker.Faker()
from openpyxl import Workbook
data=pd.read_excel('fakedata.xlsx',header=None)
fake=faker.Faker()
wb=Workbook()
sheet=wb.active
first_name=[]
last_name=[]
email_id=[]
salary=[]
bonus=[]
exp=[]
skill=[]
company_name=[]
emi=[]
height=[]
gender=[]
monthly_expenses=[]
maritalStatus=[]
company_location=[]
hometown=[]
qualification=[]
percentage=[]
passedoutyear=[]
ownHouse=[]
ownCar=[]
age=[]
for j,i in data.iterrows():
    first_name.append(i[0])
    last_name.append(i[1])
    email_id.append(i[2])
    salary.append(i[3])
    bonus.append(i[4])
    exp.append(i[5])
    skill.append(i[6])
    company_name.append(i[7])
    emi.append(i[8])
    height.append(i[9])
    gender.append(i[10])
    monthly_expenses.append(i[11])
    maritalStatus.append(i[12])
    company_location.append(i[13])
    hometown.append(i[14])
    qualification.append(i[15])
    percentage.append(i[16])
    passedoutyear.append(i[17])
    ownHouse.append(i[18])
    ownCar.append(i[19])
    age.append(i[20])
students={'first_name':first_name,'last_name':last_name,'email_id':email_id,'salary':salary,'bonus':bonus,'exp':exp,'skill':skill,
          'company_name':company_name,'emi':emi,'height':height,'gender':gender,'monthly_expenses':monthly_expenses,'maritalStatus':
          maritalStatus,'company_location':company_location,'hometown':hometown,'qualification':qualification,'percentage':percentage,
          'passedoutyear':passedoutyear,'ownHouse':ownHouse,'ownCar':ownCar,'age':age}
edf=pd.DataFrame(students)
print(edf)

#loading data to sql server
import pypyodbc as odbc
import numpy as np
import pymysql
import pandas as pd
import faker
fake=faker.Faker()
a=odbc.connect('DRIVER={SQL Server}; Server=GNAGAMANI\SQLEXPRESS; Database=projectdb')
c=a.cursor()

df=pd.concat([mdf,tdf,sdf,edf])
print(df)

for i,j in df.iterrows():
    c.execute("insert into mainproject values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
               (j.first_name,j.last_name,j.email_id,j.salary,j.bonus,j.exp,j.skill,j.company_name,j.emi,j.height,j.gender,
                j.monthly_expenses,j.maritalStatus,j.company_location,j.hometown,j.qualification,j.percentage,j.passedoutyear,
                j.ownHouse,j.ownCar,j.age))
    a.commit()



    







    
