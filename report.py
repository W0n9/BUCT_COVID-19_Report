import json
import time

import requests

if __name__ == '__main__':

	# init
	s = requests.session()
	headers = {
	}

	# report
	cookies = {
		'eai-sess':'', #使用cookies进行身份认证
		'UUkey':''
	}

	data = {
		'ismoved': '0',
		'sfxk':'0',
		'dqjzzt': '1',  # 当前居住状态，0在校、1在京不在校
		'jhfjrq': '',  # 计划返京日期
		'jhfjjtgj': '',  # 计划返京交通工具
		'jhfjhbcc': '',  # 计划返京航班车次
		'tw': '3',  # 体温范围所对应的页面上的序号（下标从 1 开始）
		'sfcxtz': '0', # 今日是否出现发热、乏力、干咳、呼吸困难等症状？
		'sfjcbh': '0', # 今日是否接触疑似/确诊人群？
		'sfcxzysx': '0', # 是否有任何与疫情相关的注意事项？
		'qksm': '',  # 情况说明
		'sfyyjc': '0', # 是否医院检查
		'jcjgqr': '0', # 检查结果确认
		'remark': '',
		'address': '中国',  # 地址
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
			'pois': []},
		'area': '中国',  # 所在区域
		'province': '', # 所在省
		'city': '', # 所在市
		'sfzx': '0', # 是否已经返校
		'sfjcwhry': '0',  # 是否接触武汉人员
		'sfjchbry': '0',  # 是否接触湖北人员
		'sfcyglq': '0',  # 是否处于隔离期
		'gllx': '',  # 隔离类型
		'glksrq': '',  # 隔离开始日期
		'jcbhlx': '', # 接触病患类型
		'jcbhrq': '', # 接触病患日期
		'bztcyy': '', # 当前地点与上次不在同一城市，原因如下：2 探亲, 3 旅游, 4 回家, 1 其他
		'sftjhb': '0',  # 是否停经湖北
		'sftjwh': '0',  # 是否停经武汉
		'sfsfbh': '0', # 是否所在省份变化
		'xjzd': '', # 现居住地
		'jcwhryfs': '',  # 接触武汉人员方式
		'jchbryfs': '',  # 接触湖北人员方式
		'szgj': '', # 所在国家
		'jcjg': '' # 检查结果
	}
	r = s.post('https://eai.buct.edu.cn/ncov/wap/default/save', data=data, headers=headers, cookies=cookies)
	print('【上报】' + json.loads(r.text)['m'])
	time.sleep(3)
