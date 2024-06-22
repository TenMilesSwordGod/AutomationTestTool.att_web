from django.http import HttpResponse
# from django.shortcuts import render

# Create your views here.
# 在 views.py 文件夹中， 这是一个示例
def report_web(request):	# 函数必须要有一个 request 参数
    return HttpResponse("hello world")
