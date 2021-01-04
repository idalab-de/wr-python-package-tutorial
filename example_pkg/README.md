# Web Log Pipeline
A small pipeline analyzing mocked web logs.


## Background

A common use case for a data pipeline is figuring out information about the visitors to your web site. If you’re familiar with Google Analytics, you know the value of seeing real-time and historical information on visitors. This pipeline will use data from web server logs to answer questions about website visitors. 

If you’re unfamiliar, every time you visit a web page, your browser is sent data from a web server. In this example pipeline, we use a high-performance web server called Nginx. Here’s how the process of you typing in a URL and seeing a result works:

