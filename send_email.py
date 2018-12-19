import smtplib
from email.message import EmailMessage

import getpass
password= getpass.getpass('비밀번호 뭐니 : ') #비밀번호 물어보기 커맨드창

email_list = ['wnsdnjs0123@gmail.com','kjmoo455@nate.com'] #email list 변수저장

for email in email_list:   #for문으로 반복해서 보내기
    msg = EmailMessage()#EmailMessage변수저장
    msg['Subject']="제목은 제목입니다!!!" #설정해줌 딕셔너리접근
    msg['From'] = "pok_kjy@naver.com"#누가 보내는지
    msg['To']=email#누구에게 보낼지
    msg.set_content('내용은 내용입니다!!')#내용작성
    
    smtp_url = 'smtp.naver.com'#SMTP 서버명(건물)
    smtp_port = 465  #PORT 접속(문)
    
s=smtplib.SMTP_SSL(smtp_url,smtp_port)#보안연결을위해 하는것(어디건물,어디문)
s.login('pok_kjy','password') #아이디와 패스워드

s.send_message(msg)#메세지 보내게하는 명령어

