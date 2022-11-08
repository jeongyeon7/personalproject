#mysql 설치 pip install pymysql

import pymysql

#db 연결
con = pymysql.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    passwd="ezen",
    db = "stock",charset = "euckr")

if con != None:
    cursor = con.cursor()  #cursor반드시 만들어야 함
else:
    exit(0)
    
#insert 구문 실행
sql = "insert into stock (date,start,end) "
sql += "values ('2022.10.24',10,20) "

#select 구문 실행
sql = "select date,start,end from stock "
cursor.execute(sql)

num_fields = len(cursor.description)
print("컬럼갯수 : " , num_fields)
for name in cursor.description:
    print("컬럼정보 : " , name)
    print("컬럼명 : " , name[0])
print("=" * 30)

rows_data = cursor.fetchall()
total = len(rows_data)
print("행갯수 : " , num_fields)
for i in range(0,total) :
    print(rows_data[i])
    print("=" * 30)

for i in range(0,total) :
    print("date:" , rows_data[i][0])
    print("start:" , rows_data[i][1])
    print("end:" , rows_data[i][2])
    print("=" * 30)
    
cursor.execute(sql)
#python은 sql문 실행 후 commit을 해야 함
con.commit()
#db연결 닫기
con.close()

