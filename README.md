# AAAI-2021 论文集爬取下载

> 通过 scrapy 爬取 AAAI 国际顶会的论文列表并下载


## Usage

### 获取cookie

先在 chrome 中登录自己的 [AAAI-2021账号](https://virtual.2021.aaai.org/papers.html?program=all&filter=titles&track=All+tracks)

打开开发者工具，找到登录后的第一条，将里面的 `Request Headers` 中 `Cookie` 字段文字全部复制

通过[这个工具](http://tools.bugscaner.com/cookietodict) 把 cookie 字符串转成 json

### 下载代码

```bash
git clone https://github.com/rxrw/scrapy-aaai-2021
```

### 安装环境

首先保证自己有 python3 

```bash
pip install scrapy
```

### 修改配置
把刚才生成的 json 替换 aaai/settings.py 中的最后 COOKIE 字段

### 运行
```bash
scrapy crawl aaai -o results.csv
```

## 备注
可以通过修改主程序来增加更多你想要的字段， pipelines 里面可以调整输出的文件格式