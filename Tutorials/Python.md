# Python Study Note

# Spider

Websites to test spider:

1. https://pythonprogramming.net/parsememcparseface/, this website is widely used to test **Beautifulsoup**

# Proxy

## Proxy websites

1. [西刺代理](http://www.xicidaili.com/wn/)
2. http://cn-proxy.com/
3. [快代理](https://www.kuaidaili.com/free/)
1. [代理66](http://www.66ip.cn/)
2. [IP181](http://www.ip181.com/)
3. [Proxylist+](https://list.proxylistplus.com/)



```
import requests
proxy = {}
```





# Beautifulsoup

Websites to test spider:

1. https://pythonprogramming.net/parsememcparseface/

**Simple Example**:

```python
import bs4 as bs
import urllib.request

sauce = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
soup = bs.BeautifulSoup(sauce,'lxml')

print(soup.title)
print(soup.title.name)
print(soup.title.string)
print(soup.title.text)

```

Results:

```bash
<title>Python Programming Tutorials</title>
title
Python Programming Tutorials
Python Programming Tutorials

```






# Python Study Resources

1. Python Programming Net: https://pythonprogramming.net/
2. Python - Reading HTML Pages, https://www.tutorialspoint.com/python/python_reading_html_pages.htm

