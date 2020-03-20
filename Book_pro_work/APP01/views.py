from django.shortcuts import render,HttpResponse,redirect
from APP01 import models
# Create your views here.

def index(request):
    all_objs=models.Book.objects.all()
    return  render(request,'index.html',{'all_objs':all_objs})

def add_book(request):
    if request.method=='GET':
        publish_obj=models.Publish.objects.all()
        author_obj=models.Author.objects.all()
        return render(request,'add_book.html',{'publish_obj':publish_obj,'author_obj':author_obj})
    else:
        # print(request.POST)
        # title=request.POST.get('book_title')
        # price=request.POST.get('book_price')
        # pubdate=request.POST.get('book_pub_date')
        # publish=request.POST.get('publish')
        # author=request.POST.getlist('author')
        # print(title,price,pubdate,publish,author)
        # new_book_obj=models.Book.objects.create(
        #     title=title,
        #     price=price,
        #     publish_id=publish,
        #     publishDate=pubdate,
        # )
        # new_book_obj.authors.add(*author)

        all_data=request.POST.dict()
        # print(all_data)
        authors=request.POST.getlist('author')
        del all_data['csrfmiddlewaretoken']
        del all_data['author']
        # print(all_data)
        new_book_obj=models.Book.objects.create(
            **all_data
        )
        new_book_obj.authors.add(*authors)
        return redirect('index1')

def edit_book(request,book_id):
    book_obj = models.Book.objects.filter(nid=book_id)
    if request.method=='GET':
        book_obj=book_obj.first()
        publish_obj=models.Publish.objects.all()
        author_obj=models.Author.objects.all()
        return render(request,'edit_book.html',{'book_obj':book_obj,'publish_obj':publish_obj,'author_obj':author_obj})
    else:
        all_data = request.POST.dict()
        authors=request.POST.getlist('author')
        del all_data['csrfmiddlewaretoken']
        del all_data['author']
        book_obj.update(**all_data)
        book_obj.first().authors.set(authors)
        return redirect('index1')
def del_book(request,book_id):
    models.Book.objects.filter(nid=book_id).delete()
    return redirect('index1')