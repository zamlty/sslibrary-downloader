# sslibrary-downloader

Download a book from www.sslibrary.com and create PDF.

Logic learned from [padeoe's nju-lib-downloader](https://github.com/padeoe/nju-lib-downloader), many thanks!

zamlty  2017.06.18

- Requirements: 
  1. Download: Python3 (Anaconda would be better)
  2. Create PDF: Java

- How to use:
  1. Download `sslibrary.py` and `img2pdf.jar`
  2. Search the book from www.duxiu.com or www.sslibrary.com
  3. Modify `sslibrary.py`
      1. `url` - the url for the book, like "http://img.sslibrary.com/n/slib/book/slib/11647684/4fae1823b856407795c25ba7a8af7432/4bd18516cf404e663f8d36e2f949ec43.shtml?dxbaoku=true"
      2. `path` - the directory's path to store pics and PDF
      3. `threads` - thread number for downloading
  4. Run `sslibrary.py`
