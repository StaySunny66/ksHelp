# 用于检测结果是否正常
import core.mail


def chick(code, email):
    code = int(code)
    if code == 0:
        print('失败')
        core.mail.mail_false(email, code)
    else:
        if code == 1:
            print('成功')
            #core.mail.mail_ok('上午', '填写', email)
        else:
            if code == 2:
                print('成功')
                #core.mail.mail_ok('下午', '填写', email)
            else:
                if code == 3:
                    print('成功')
                    #core.mail.mail_ok('上午和下午', '补填', email)
                else:
                    if code == -2:
                        print('密码错了')
                        core.mail.mail_error(email, '您好 您的密码有误  @矢光小屋 ')
                    else:
                        if code == 11:
                            print('晨检已经填过')
                            #core.mail.mail_error(email, '您好 本次体温操作并没有执行 \n 因为我们发现您已经填写了晨检体温 \n\n\n\n  @矢光小屋 ')
                        else:
                            if code == 22:
                                print('午检已经填过')
                                #core.mail.mail_error(email, '您好 本次体温操作并没有执行 \n 因为我们发现您已经填写了午检体温 \n\n\n\n  @矢光小屋 ')
                            else:
                                print('什么也没做')

