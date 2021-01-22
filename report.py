import csv
import json
import time
import requests

filename = "id.csv"  # 最好填写csv绝对路径，默认为$PWD工作路径
url = "https://eai.buct.edu.cn/ncov/wap/default/save"


def post_and_print(s, url, data, headers, cookies):
    result = s.post(url, data=data, headers=headers, cookies=cookies)
    print(
        time.strftime("%m/%d %H:%M:%S ", time.localtime()) + name + ' ' +
        json.loads(result.text)['m'])


if __name__ == '__main__':

    # init
    s = requests.session()
    headers = {}

    # report
    cookies = {}
    data = {
        'sfzx': '0',  # 是否在校
        'sfzgn': '1',  # 所在地点中国大陆
        'zgfxdp': '0',  # 不在中高风险地区
        'jcjgqr': '0',  # 正常，非疑似/确诊
        'sfcxtz': '0',  # 没有出现发热、乏力、干咳、呼吸困难等症状
        'sfjcbh': '0',  # 今日是否接触无症状感染/疑似/确诊人群
        'mjry': '0',  # 今日是否接触密接人员
        'csmjry': '0',  # 近14日内本人/共同居住者是否去过疫情发生场所
        'sfcyglq': '0',  # 是否处于观察期
        'szsqsfybl': '0',  # 所在社区是否有确诊病例
        'sfcxzysx': '0',  # 是否有任何与疫情相关的， 值得注意的情况
        'tw': '1',  # 体温范围（下标从 1 开始），此处是36 - 36.5
        'area': '西藏自治区 日喀则市 定日县',  # 所在区域
        'province': '西藏自治区',  # 所在省
        'city': '日喀则市',  # 所在市
        'address': '西藏自治区日喀则市定日县珠峰大本营',  # 地址
        # 'sfcyglq': '0',  # 是否处于隔离期
        # 'sfyzz': '0',  # 是否有症状
        # 'askforleave': '0',  # 是否请假外出
        'qksm': '',  #其他情况
        'geo_api_info': {
            'type': 'complete',
            'info': 'SUCCESS',
            'status': 1,
            'Eia': 'jsonp_913580_',
            'position': {
                'O': 113.0270592,  # 经度
                'P': 22.5524345,  # 纬度
                'lng': 113.0270592,  # 经度
                'lat': 22.5524345  # 纬度
            },
            'message': 'Get+ipLocation+success.Get+address+success.',
            'location_type': 'ip',
            'accuracy': None,
            'isConverted': True,
            'addressComponent': {
                'citycode': '',
                'adcode': '',  # 行政区划代码
                'businessAreas': [],
                'neighborhoodType': '',
                'neighborhood': '',
                'building': '',
                'buildingType': '',
                'street': '',
                'streetNumber': '',
                'province': '',  # 所在省
                'city': '',  # 所在市
                'district': '',  # 所在区
                'township': ''  # 所在街道
            },
            'formattedAddress': '',  # 拼接后的地址
            'roads': [],
            'crosses': [],
            'pois': []
        },
    }

    with open(filename, 'r', encoding='gb2312') as f:
        reader = csv.reader(f)
        reader.__next__()
        for row in reader:
            name = row[0]
            cookies['eai-sess'] = row[1]
            at_school_status = row[2]
            custom_area_status = row[3]
            if at_school_status == '1':  #   判断在校同学
                at_school_data = data
                at_school_data.update(sfzx='1',
                                      area='北京市 朝阳区',
                                      province='北京市',
                                      city='北京市',
                                      address='北京市朝阳区北三环东路15号北京化工大学')
                post_and_print(s, url, at_school_data, headers, cookies)
                continue
            if custom_area_status == '1':  #   判断自定义位置
                custom_area_data = data
                custom_area_data.update(area=row[4],
                                        province=row[4].split()[0],
                                        city=row[4].split()[1],
                                        address=row[4])
                post_and_print(s, url, custom_area_data, headers, cookies)
                continue
            post_and_print(s, url, data, headers, cookies)
