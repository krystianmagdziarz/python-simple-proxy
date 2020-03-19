# Easy to use python free proxy library

This code is created for people who want to use free proxy servers to work with their projects.
It aggregates all sources of free proxies and gives the possibility of easy handling. 

Great to use with #selenium, #scrapy and #bs4 for web scraping purposes. :shipit:

Enjoy :+1:

### Requirements:

* python >= 3.5
* beautifulsoup4

### Installation:
```shell script
# Clone repo
git clone https://github.com/OceanFireSoftware/python-simple-proxy.git

# Change directory
cd pythonsimpleproxy

# Create virtual environment
virtualenv venv --python=python3

# Install requirements
pip install -r requirements.txt
```

### How to use

```python
from proxymanager import ProxyManager

proxy = ProxyManager()
proxy.print_all()
```

Output:

```text
125.167.230.150:8080
168.131.152.152:3128
157.230.253.73:44344
200.73.128.244:3128
...
```

### References:

* [fate0/proxylist](https://github.com/fate0/proxylist/)
* [pubproxy.com](http://pubproxy.com/api/proxy?limit=5&format=txt&https=true&type=https)
