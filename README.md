<!--
 * @Author: your name
 * @Date: 2020-03-28 10:35:53
 * @LastEditTime: 2020-03-28 10:38:05
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: \BUCT_nCoV_Report\README.md
 -->
# BUCT_nCoV_Report
基于 Python3 的适用于北京化工大学的 nCoV 自动填报脚本

## 使用方式

1. 在微信进入“疫情防控”页面，抓包获得'cookies'，修改'report.py'内的'cookies'值
    ```text
    'eai-sess':'', 
	  'UUkey':''
    ```
2. 修改 `report.py` 内的经纬度（可选)
3. 填写 `province` 和 `city`避免报 `上报位置不能为空` 错误
4. 安装所需依赖：`pip3 install requests`
5. 执行 `report.py`

## 自动化
### Window：任务计划程序
### Linux：使用 Crontab

```shell script
sudo crontab -e
```

每天早晨 6 点上报
```shell script
0 6 * * * python3 main.py
```

## 感谢
[BJUT_nCoV_Report](https://github.com/nonPointer/BJUT_nCoV_Report)
