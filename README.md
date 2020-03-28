# BUCT_nCoV_Report
基于 Python3 的适用于化工大学的 nCoV 自动填报脚本

## 使用方式

1. 在微信进入“疫情防控”页面，抓包获得'cookies'，修改'report.py'内的'cookies'值
    ```text
    'eai-sess':'', 
	  'UUkey':''
    ```
2. 修改 `report.py` 内的经纬度和地址信息（可选)
3. 安装所需依赖：`pip3 install requests`
4. 执行 `report.py`

## 自动化

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
