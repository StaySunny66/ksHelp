from time import sleep
import core.result_chick
import core.put_for_www
import sql.sql
import core.mail
import log.log
import time

T = 0
F = 0
print('这是科师体温主程序\n')
time_begin = int(time.time())
# 读取数据库 中的条目
lis = sql.sql.get_user()
# 得出所有的数据并进行遍历填写 因为百度 ocr API限制 暂定为单线程
for x in lis:
    user = str(x[0])
    school_pass = x[1]
    address = x[2]
    token = x[3]
    id = x[4]
    email = x[5]
    log.log.add_log(user, 0, "new")
    print("*******************************************************************************************************")
    print('学号: ' + user + ' 地址: ' + address + ' Email: ' + email)
    result = core.put_for_www.add_main(to_us=user, to_ps=school_pass, address1=address, to_token=token, to_id=id)
    core.result_chick.chick(result, email)
    if (result == -1) or (result == 0) or (result == -2):
        F = F + 1
    else:
        T = T + 1
    sleep(2)
time_end = int(time.time())
count = time_end - time_begin

print('耗时' + str(count) + '秒')
# 统计汇总 报告开发者
core.mail.mail_all(T, F, count)
