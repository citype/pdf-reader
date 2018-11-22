##pdf 2 txt
测试过 PyPDF2 和 pdfminer3k 两种 python 现有的 pdf 读取库
都出现编码转化的问题还有就是对中文扫描件的识别问题。

后期使用
```
sudo pip install pdfminer.six    
```
利用内部的 pdf2txt.py 进行识别
```
 pdf2txt.py /Users/xihe/Desktop/aa.pdf   
 ```
 不存在编码转化的问题，
 同时可以发现对正规生成的 pdf 而非扫描件的 pdf 识别率差别较为明显