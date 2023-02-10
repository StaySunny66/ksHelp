import smtplib
from email.mime.text import MIMEText


# 发信模块 将运行结果发送给客户与管理员
def mail_ok(st, way, email):
    msg_from = '###################'
    passwd = '###################'
    msg_to = email

    subject = "科师 体温自动填报系统"
    content = '你好 您今日的' + st + '体温已经为您' + way + '完成！\n 因为验证码自动识别的次数有限且准确率不高\n 请不要频繁登录您的小程序\n 以免资源耗尽 无法登录\n\n\n\n     @矢光小屋'
    msg = MIMEText(content)
    msg['Subject'] = subject
    msg['From'] = msg_from
    msg['To'] = msg_to
    try:
        s = smtplib.SMTP_SSL("smtp.qq.com", 465)
        s.login(msg_from, passwd)
        s.sendmail(msg_from, msg_to, msg.as_string())
        print("给" + email + "邮件发送成功")
    except s.SMTPException as e:
        print("发送失败")
    finally:
        s.quit()


def mail_false(email, code):
    msg_from = '###################'
    passwd = '###################'
    msg_to = email

    subject = "科师 体温自动填报系统"
    content = '很抱歉, 系统未能将你的体温填写完成，\n\n 错误代码:' + str(code)+'\n\n\n\n      @矢光小屋'
    msg = MIMEText(content)
    msg['Subject'] = subject
    msg['From'] = msg_from
    msg['To'] = msg_to
    try:
        s = smtplib.SMTP_SSL("smtp.qq.com", 465)
        s.login(msg_from, passwd)
        s.sendmail(msg_from, msg_to, msg.as_string())
        print("给" + email + "邮件发送成功")
    except s.SMTPException as e:
        print("发送失败")
    finally:
        s.quit()


def mail_all(T, F,time):
    msg_from = '###################'
    passwd = '###################'
    msg_to = '###################'

    subject = "科师 体温自动填报系统"
    content = '小主您好，\n\n 本次系统运行统计如下' + '\n成功:' + str(T) + "\n失败:" + str(F)+'耗时'+str(time)+'秒'
    msg = MIMEText(content)
    msg['Subject'] = subject
    msg['From'] = msg_from
    msg['To'] = msg_to
    try:
        s = smtplib.SMTP_SSL("smtp.qq.com", 465)
        s.login(msg_from, passwd)
        s.sendmail(msg_from, msg_to, msg.as_string())
        print("给管理员发送邮件成功")
    except s.SMTPException as e:
        print("给管理员发送邮件失败")
    finally:
        s.quit()


def mail_error(email, contant):
    msg_from = '###################'
    passwd = '###################'
    msg_to = email

    subject = "科师 体温自动填报系统"
    content = contant
    msg = MIMEText(content)
    msg['Subject'] = subject
    msg['From'] = msg_from
    msg['To'] = msg_to
    try:
        s = smtplib.SMTP_SSL("smtp.qq.com", 465)
        s.login(msg_from, passwd)
        s.sendmail(msg_from, msg_to, msg.as_string())
        print("给" + email + "邮件发送成功")
    except s.SMTPException as e:
        print("发送失败")
    finally:
        s.quit()
