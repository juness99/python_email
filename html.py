import csv
import smtplib#smtplib이라는 파이썬 기본내장 모듈
from email.message import EmailMessage
import getpass


smtp_url = 'smtp.naver.com'#SMTP 서버명(건물)
smtp_port = 465  #PORT 접속(문)
s=smtplib.SMTP_SSL(smtp_url,smtp_port)#보안연결을위해 하는것(어디건물,어디문)
f= open('pygj - email.csv','r',encoding='utf-8')#r은 email 을 읽음 encoding 파일을 열어줌
read_csv =csv.reader(f) #csv를 열어주는 함수
password= getpass.getpass('비밀번호 뭐니 : ') #비밀번호 물어보기 커맨드창
s.login("pok_kjy@naver.com",password) #아이디와 패스워드


for line in read_csv:
    print(line)
    print(line[0]+'/'+line[1])#0~1라인사이에 /를 넣고 출력
    email_list = line[1]
    msg = EmailMessage()#EmailMessage변수저장
    msg['Subject']="제목은 제목입니다!!!" #설정해줌 딕셔너리접근
    msg['From'] = "pok_kjy@naver.com"#누가 보내는지
    msg['To']=email_list#누구에게 보낼지
    msg.set_content('내용은 내용입니다.!!!')
    msg.add_alternative('''<h1>안녕</h1><p>난은솔이야</p>''',subtype="html")
    s.send_message(msg)
    
f.close()
 #email list 변수저장
    