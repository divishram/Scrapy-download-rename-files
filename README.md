# Scrapy download rename files

By default Scrapy uses the SHA1 Hash as the file name, and this can lead to confusion. I modified the pipelines so Scrapy would replace the file name with the title extracted with the XPath selector.

![](media/scrapy-crawl.gif)

### Prerequisites

```
-Python 3.5+
-Scrapy 2.1.0
```

### Installing
```
pip install scrapy
```

### Usage
![](media/downloaded_pics.JPG)
