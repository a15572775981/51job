# -*- coding: utf-8 -*-

# Scrapy settings for job51 project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'job51'

SPIDER_MODULES = ['job51.spiders']
NEWSPIDER_MODULE = 'job51.spiders'

PROXY_URL = 'http://127.0.0.1:8888/random'

MYSQL_HOST = 'localhost'
MYSQL_DATABASE = 'job51'
MYSQL_USER = 'root'
MYSQL_PASSWORD = '15572775981'
MYSQL_PORT = 3306


# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 'guid=928ac502c5e9972832b293627edab27e; nsearch=jobarea%3D%26%7C%26ord_field%3D%26%7C%26recentSearch0%3D%26%7C%26recentSearch1%3D%26%7C%26recentSearch2%3D%26%7C%26recentSearch3%3D%26%7C%26recentSearch4%3D%26%7C%26collapse_expansion%3D; ps=us%3DATgBaw5rCyMGZlw1VzEBLFRjAzIELABnXGoFYQt9U2IAPVszVTMGNlAyAWpWM1ZnAzkDMlNkWjpQKgIxCWkFQgFZAWg%253D%26%7C%26needv%3D0; mq=%C5%C0%B3%E6; search=jobarea%7E%60180200%7C%21ord_field%7E%600%7C%21recentSearch0%7E%601%A1%FB%A1%FA180200%2C00%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA%C5%C0%B3%E6%A1%FB%A1%FA2%A1%FB%A1%FA%A1%FB%A1%FA-1%A1%FB%A1%FA1555481427%A1%FB%A1%FA0%A1%FB%A1%FA%A1%FB%A1%FA%7C%21recentSearch1%7E%601%A1%FB%A1%FA180200%2C00%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA%D7%D4%B6%AF%BB%AF%D4%CB%CE%AC%A1%FB%A1%FA2%A1%FB%A1%FA%A1%FB%A1%FA-1%A1%FB%A1%FA1555481367%A1%FB%A1%FA0%A1%FB%A1%FA%A1%FB%A1%FA%7C%21recentSearch2%7E%601%A1%FB%A1%FA180300%2C00%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA%D7%D4%B6%AF%BB%AF%B2%E2%CA%D4%B9%A4%B3%CC%CA%A6%A1%FB%A1%FA2%A1%FB%A1%FA%A1%FB%A1%FA-1%A1%FB%A1%FA1555481351%A1%FB%A1%FA0%A1%FB%A1%FA%A1%FB%A1%FA%7C%21recentSearch3%7E%601%A1%FB%A1%FA180200%2C00%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA%D7%D4%B6%AF%BB%AF%B2%E2%CA%D4%B9%A4%B3%CC%CA%A6%A1%FB%A1%FA2%A1%FB%A1%FA%A1%FB%A1%FA-1%A1%FB%A1%FA1555481310%A1%FB%A1%FA0%A1%FB%A1%FA%A1%FB%A1%FA%7C%21recentSearch4%7E%601%A1%FB%A1%FA070400%2C00%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA%D7%D4%B6%AF%BB%AF%B2%E2%CA%D4%B9%A4%B3%CC%CA%A6%A1%FB%A1%FA2%A1%FB%A1%FA%A1%FB%A1%FA-1%A1%FB%A1%FA1555481300%A1%FB%A1%FA0%A1%FB%A1%FA%A1%FB%A1%FA%7C%21collapse_expansion%7E%601%7C%21; _ujz=MTUwMzA3NjUzMA%3D%3D; 51job=cuid%3D150307653%26%7C%26cusername%3Dphone_15572775981_201902017022%26%7C%26cpassword%3D%26%7C%26cname%3D%25D1%25CF%25CE%25B0%25BD%25A8%26%7C%26cemail%3D15572775981%2540163.com%26%7C%26cemailstatus%3D0%26%7C%26cnickname%3D%26%7C%26ccry%3D.0XZptO8BAMm2%26%7C%26cconfirmkey%3D1590qW2LY06qU%26%7C%26cresumeids%3D.0VrWUI7NvXb6%257C%26%7C%26cautologin%3D1%26%7C%26cenglish%3D0%26%7C%26sex%3D0%26%7C%26cnamekey%3D15mSYPR%252FRMGyQ%26%7C%26to%3Dac67f47ea0181e277e3ef072d65e5a255cb6c3e2%26%7C%26; adv=adsnew%3D0%26%7C%26adsnum%3D2168966%26%7C%26adsresume%3D1%26%7C%26adsfrom%3Dhttps%253A%252F%252Fwww.baidu.com%252Fbaidu.php%253Fsc.K600000F3Z4zzZ2Y9yWtKuDpMAPXCaGCm-x-cX5YPOkFngcNdNfekGbecc3EZDxcZBLNO-DBwO6dbeOc7QDnzESo7Ae2uQCQTKlGGUxpgJsyjXXcl-KvbrzZIgJ56dz806qSg-rV_YKDvcBa8K3LFYhGCv6L0kVHcpCJEH9683gBCXSYIJg_LqibDVHzjhoCIETSbcVUkn4XkBL5Z6.DR_NR2Ar5Od66CHnsGtVdXNdlc2D1n2xx81IZ76Y_u2SMuElXMJ1-k_nOEOlecxLO3MHSEwECntx135zOCxgvg45E6OeAHxfOgkOdkxo3O-CLOWEWEzgxwOsr5Oml5dlpoQOvSajSw7OVxwxS9yOO_xVYXveqElqEgVmvfdG_H3en-dvHFIjxvuQVOB-MFb8lRq5uEtN2s1f_IheF3S260.U1Yk0ZDqkea11neXYtT0TA-W5H00IjLZ_nvS1VeHksKGUHYznjf0u1dBugK1nfKdpHdBmy-bIfKspyfqnHm0mv-b5HnLP6KVIjYknjDLg1DsnH-xnH0YP7t1PW0k0AVG5H00TMfqP1T10ANGujYkPjR3g1cknHD1g1D3PHmsg1c3P1TYg1c3P1csg1c3PHRLg1c3rjnzg1c3PH6dg1cvn1Rsg1c3PW0Yg1c3P10k0AFG5HcsP0KVm1Y3nHczP1fzrj9xnH0snNtknjFxn0KkTA-b5H00TyPGujYs0ZFMIA7M5H00mycqn7ts0ANzu1Yz0ZKs5H00UMus5H08nj0snj0snj00Ugws5H00uAwETjYs0ZFJ5H00uANv5gKW0AuY5H00TA6qn0KET1Ys0AFL5HDs0A4Y5H00TLCq0A71gv-bm1dsTzdWUfKYIgnqnHndPHcsP1mdPWRYPjR4rjTkPH60ThNkIjYkPHRdPj6sPWfkrjbs0ZPGujd-ryP-PWnknH0snHbvPvR10AP1UHY3nRD1PHfznHKjfH-KnRRv0A7W5HD0TA3qn0KkUgfqn0KkUgnqn0KlIjYs0AdWgvuzUvYqn7tsg1DsPjuxn0Kbmy4dmhNxTAk9Uh-bT1Ysg1Kxn1n3Pjc4Pdts0ZK9I7qhUA7M5H00uAPGujYs0ANYpyfqQHD0mgPsmvnqn0KdTA-8mvnqn0KkUymqn0KhmLNY5H00uMGC5H00uh7Y5H00XMK_Ignqn0K9uAu_myTqnfK_uhnqn0KEIjYs0AqzTZfqnanscznsc100mLFW5HfvPWm1%2526word%253D%2525E5%252589%25258D%2525E7%2525A8%25258B%2525E6%252597%2525A0%2525E5%2525BF%2525A7%2526ck%253D6774.8.88.452.560.617.563.95%2526shh%253Dwww.baidu.com%2526sht%253Dbaidu%2526us%253D1.0.2.0.1.302.0%2526bc%253D110101; partner=www_baidu_com; slife=lastvisit%3D230400%26%7C%26lowbrowser%3Dnot%26%7C%26lastlogindate%3D20190421%26%7C%26',
    'Host': 'jobs.51job.com',
    'Referer': 'https://mq.51job.com/',
    'Upgrade-Insecure-Requests': '1',
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'job51.middlewares.Job51SpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'job51.middlewares.Job51DownloaderMiddleware': 400,
   'job51.middlewares.RandomUserAgentMiddleware': 410,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'job51.pipelines.Job51Pipeline': 200,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
