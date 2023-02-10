import requests


def add_log(school_id, tw, when):
    if when == "am":
        log = {
            'user': school_id,
            'cjtw': tw,
            'source': "python",
            'when': "am"
        }
    if when == "pm":
            log = {
                'user': school_id,
                'wjtw': tw,
                'source': "python",
                'when': "pm"
            }
    if when == "new":
            log = {
                'user': school_id,
                'wjtw': tw,
                'source': "python",
                'when': "new"
            }
            
    r = requests.post("https://###################/user/log.php", data=log)


def add_log_bt(school_id, cjtw, wjtw):
    log = {
        'user': school_id,
        'cjtw': cjtw,
        'wjtw': wjtw,
        'source': "python",
        'when': "night"
    }
    requests.post("https://###################/user/log.php", data=log)

