from time import sleep
import json
import requests
import base64
import time
import datetime
import random
import sql.sql
import log.log


# 作用
# 解析百度识图的结果
def get_code(js):
    co = json.loads(js)
    if co['words_result']:
        return co['words_result'][0]['words']
    else:
        return False


# 解析token
def get_token(str1):
    token = requests.get(str1)
    if token:
        obj = json.loads(token.text)
        return obj['access_token']


# 向百度ocr发送验证码图像

def get_img_str(img_str, token1):
    post_url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic'

    img_data = {
        'image': img_str,
        'access_token': token1
    }
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"}
    img_str = requests.post(post_url, img_data, headers)
    if img_str:
        return img_str.text


def add_main(to_us, to_ps, address1, to_token, to_id):

    result = 0
    is_ok = False
    us = to_us
    ps = to_ps
    token = to_token
    id = to_id

    coo = 'csrftoken=' + token[0:63] + '; ' + 'sessionid=' + id + ' '
    head = {'Cookie': coo,
            'Referer': 'https://ksxskj.hevttc.edu.cn/'
            }
    jc = requests.get('https://ksxskj.hevttc.edu.cn/', headers=head)
    if jc.text.find('确定退出') != -1:
        print('身份码有效')
    else:
        print('已经失效！准备重新获取')
        is_ok = True

    if is_ok:
        i = 0
        # 这三个为获取百度ocr识别所需
        url = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id='
        client_id = '###################'
        client_secret = '###################'
        # 得到科师服务器下发的token
        get_tokens = requests.get('https://ksxskj.hevttc.edu.cn/')

        token = get_tokens.headers['Set-Cookie'][10:74]
        getmd = get_tokens.text[1562:1626]

        # 显示token
        headd = {
            'Cookie': 'csrftoken=' + token
        }
        # 首次获得id和img 抛弃img 只保留id
        get_img = requests.get(
            'https://ksxskj.hevttc.edu.cn/getcheckimg/?timestamp=' + str(int(time.time() * 1000)) + '/',
            headers=headd)

        id = get_img.headers['Set-Cookie'][10:42]

        coo = 'csrftoken=' + token + '; ' + 'sessionid=' + id + ' '

        head = {'Cookie': coo,
                'Referer': 'https://ksxskj.hevttc.edu.cn/login/?next=/'
                }

        while True:
            get_img = requests.get(
                'https://ksxskj.hevttc.edu.cn/getcheckimg/?timestamp=' + str(int(time.time() * 1000)) + '/',
                headers=head)

            id = get_img.headers['Set-Cookie'][10:42]
            coo = 'csrftoken=' + token + '; ' + 'sessionid=' + id
            sleep(3)
            bm = get_img.content
            img_sr = base64.b64encode(bm)
            t = get_img_str(img_sr, get_token(url + client_id + '&' + 'client_secret=' + client_secret))
            if get_code(t):
                print("识别的验证码:" + get_code(t))
                chick = get_code(t)
                heady = {'Cookie': coo,
                         'Referer': 'https://ksxskj.hevttc.edu.cn/login/?next=/'
                         }

                datay = {'csrfmiddlewaretoken': getmd,
                         'username': us,
                         'password': ps,
                         'check_code': chick,
                         'next': '%2F'
                         }
                jiance = requests.post('https://ksxskj.hevttc.edu.cn/login/?next=/', headers=heady, data=datay,
                                       allow_redirects=False)

                if jiance.text.find('注意他们都是区分大小写的') != int(-1):
                    result = -2
                    break
                if jiance.text.find('验证码错误') == -1:

                    token = jiance.headers['Set-Cookie'][10:74]
                    id = jiance.headers['Set-Cookie'][
                         jiance.headers['Set-Cookie'].find('sessionid=') + 10:jiance.headers['Set-Cookie'].find(
                             'sessionid=') + 42]

                    print("-------------------------------------------------------")
                    print('登陆成功！')
                    print("密钥 已经更新到数据库！")
                    print('--------------------------------------------------------')
                    # 数据库更新 函数
                    sql.sql.up_user(user=us, Etoken=token, Eid=id)

                    break
                else:
                    i = i + 1
                    print("验证码识别错误！正在进行第" + str(++i) + "次尝试")

    wd = random.randint(361, 367) / 10.0
    wd1 = random.randint(361, 367) / 10.0
    csrftoken = token
    sessionid = id

    cookie = 'csrftoken=' + csrftoken + ';' + 'sessionid=' + sessionid
    url_am = 'https://ksxskj.hevttc.edu.cn/NCIR/user_data/add/ambt/'
    url_pm = 'https://ksxskj.hevttc.edu.cn/NCIR/user_data/add/pmbt/'

    if (datetime.datetime.now().hour >= 6) & (datetime.datetime.now().hour < 12):
        url_t = url_am
        post_headers = {"Content-Type": "application/x-www-form-urlencoded", "Referer": url_t,
                        "Cookie": cookie}

        key = requests.get('https://ksxskj.hevttc.edu.cn/NCIR/user_data/add/ambt/', headers=post_headers)
        if key.text.find('不可重复录入') != -1:
            return 11
        key = key.text[key.text.find('csrfmiddlewaretoken') + 28:key.text.find('csrfmiddlewaretoken') + 92]

        post_data = {
            'csrfmiddlewaretoken': key,
            'tw': wd,
            'fl': 'False',
            'gk': 'False',
            'hx': 'False',
            'qt': 'False',
            'jc': 'False',
            'fx': 'False',
            'jqjc': '',
            'lc': address1,
            'hsjc_or_not': 'True',
            'initial-hsjc_or_not': 'True',
            'hsjc_reason': '',
            'initial-hsjc_reason': '',
            'hsjc_result': '0',
            'initial-hsjc_result': '0',
            'actionName': 'actionValue'
        }

        res = requests.post(url_t, data=post_data, headers=post_headers)
        if res.text.find('保存成功') != -1:
            print('已经保存晨检体温:' + str(wd))
            log.log.add_log(us, wd, "am")
            result = 1

    if (datetime.datetime.now().hour >= 12) & (datetime.datetime.now().hour <= 18):
        url_t = url_pm

        post_headers = {"Content-Type": "application/x-www-form-urlencoded", "Referer": url_t,
                        "Cookie": cookie}
        key = requests.get('https://ksxskj.hevttc.edu.cn/NCIR/user_data/add/ambt/', headers=post_headers)
        if key.text.find('不可重复录入') != -1:
            return 22
        key = key.text[key.text.find('csrfmiddlewaretoken') + 28:key.text.find('csrfmiddlewaretoken') + 92]

        post_data = {
            'csrfmiddlewaretoken': key,
            'tw': wd1,
            'fl': 'False',
            'gk': 'False',
            'hx': 'False',
            'qt': 'False',
            'jc': 'False',
            'fx': 'False',
            'jqjc': '',
            'lc': address1,
            'hsjc_or_not': 'True',
            'initial-hsjc_or_not': 'True',
            'hsjc_reason': '',
            'initial-hsjc_reason': '',
            'hsjc_result': '0',
            'initial-hsjc_result': '0',
            'actionName': 'actionValue'
        }
        res = requests.post(url_t, data=post_data, headers=post_headers)

        if res.text.find('保存成功') != -1:
            print('已经保存午检体温:' + str(wd1))
            log.log.add_log(us, wd1, "pm")
            result = 2

    if (datetime.datetime.now().hour >= 19) & (datetime.datetime.now().hour < 22):

        post_headers = {"Content-Type": "application/x-www-form-urlencoded", "Referer": url_am,
                        "Cookie": cookie}
        key = requests.get('https://ksxskj.hevttc.edu.cn/NCIR/user_data/add/ambt/', headers=post_headers)

        key = key.text[key.text.find('csrfmiddlewaretoken') + 28:key.text.find('csrfmiddlewaretoken') + 92]
        post_data = {
            'csrfmiddlewaretoken': key,
            'tw': wd,
            'fl': 'False',
            'gk': 'False',
            'hx': 'False',
            'qt': 'False',
            'jc': 'False',
            'fx': 'False',
            'jqjc': '',
            'lc': address1,
            'hsjc_or_not': 'True',
            'initial-hsjc_or_not': 'True',
            'hsjc_reason': '',
            'initial-hsjc_reason': '',
            'hsjc_result': '0',
            'initial-hsjc_result': '0',
            'actionName': 'actionValue'
        }
        result_a = 0
        res = requests.post(url_am, data=post_data, headers=post_headers)
        if res.text.find('保存成功') != -1:
            print('已经补填晨检体温:' + str(wd))
            result_a = 3
        else:
            print(res.text)
        sleep(2)
        post_headers = {"Content-Type": "application/x-www-form-urlencoded", "Referer": url_pm,
                        "Cookie": cookie}
        key = requests.get('https://ksxskj.hevttc.edu.cn/NCIR/user_data/add/pmbt/', headers=post_headers)
        key = key.text[key.text.find('csrfmiddlewaretoken') + 28:key.text.find('csrfmiddlewaretoken') + 92]
        post_data = {
            'csrfmiddlewaretoken': key,
            'tw': wd1,
            'fl': 'False',
            'gk': 'False',
            'hx': 'False',
            'qt': 'False',
            'jc': 'False',
            'fx': 'False',
            'jqjc': '',
            'lc': address1,
            'hsjc_or_not': 'True',
            'initial-hsjc_or_not': 'True',
            'hsjc_reason': '',
            'initial-hsjc_reason': '',
            'hsjc_result': '0',
            'initial-hsjc_result': '0',
            'actionName': 'actionValue'
        }
        result_p = 0
        res = requests.post(url_pm, data=post_data, headers=post_headers)
        if res.text.find('保存成功') != -1:
            print('已经补填午检体温:' + str(wd1))
            result_p = 3
        else:
            print(res.text)

        if (result_p == 3) and (result_a == 3):
            log.log.add_log_bt(us, wd, wd1)
            result = 3

    return result
