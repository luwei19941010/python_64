from django.db import models

# Create your models here.
class Author(models.Model):#作者表与作者详细信息表一对一关系
    nid=models.AutoField(primary_key=True)
    name=models.CharField(max_length=32)
    age=models.IntegerField()
    authorDetail=models.OneToOneField(to='AuthorDetail',to_field='nid',on_delete=models.CASCADE)#,related_name='xxx' 反向不需要写表名，直接写xxx
    def __str__(self):
        return self.name

class AuthorDetail(models.Model):#作者详细信息表
    nid=models.AutoField(primary_key=True)
    birthday=models.DateField()
    telephone=models.BigIntegerField()
    addr=models.CharField(max_length=64)
    def __str__(self):
        return self.addr

class Publish(models.Model):#出版社表与书籍表一对多,
    nid=models.AutoField(primary_key=True)
    name=models.CharField(max_length=32)
    city=models.CharField(max_length=32)
    email=models.EmailField()
    def __str__(self):
        return self.name

class Book(models.Model):#书籍表与出版社多对一,书籍表与作者表多对多
    nid=models.AutoField(primary_key=True)
    title=models.CharField(max_length=32)
    publishDate=models.DateField()
    price=models.DecimalField(max_digits=5,decimal_places=2)
    publish=models.ForeignKey(to='Publish',to_field='nid',on_delete=models.CASCADE)
    authors=models.ManyToManyField(to='Author')
    def __str__(self):
        return self.title

    def get_author_name(self):
        ret=','.join([author.name for author in (self.authors.all())])
        return ret