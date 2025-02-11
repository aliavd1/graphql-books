from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=150, verbose_name="عنوان")
    author = models.ForeignKey(
        "Author", related_name="books", on_delete=models.CASCADE, verbose_name="نویسنده"
    )
    publisher = models.ForeignKey(
        "Publisher", related_name="books", on_delete=models.CASCADE, verbose_name="ناشر"
    )
    publication_date = models.DateField(verbose_name="تاریخ انتشار")
    isbn = models.CharField(max_length=13, verbose_name="شابک")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="قیمت")
    pages = models.PositiveBigIntegerField(verbose_name="تعداد صفحات")
    cover_image = models.FileField(
        upload_to="book/covers", null=True, blank=True, verbose_name="تصویر جلد"
    )

    class Meta:
        verbose_name = "کتاب"
        verbose_name_plural = "کتاب ها"
    
    def __str__(self):
        return self.title


class Author(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="نام")
    last_name = models.CharField(max_length=150, verbose_name="نام خانوادگی")
    age = models.PositiveSmallIntegerField(verbose_name="سن")
    email = models.EmailField(unique=True, verbose_name="ایمیل")
    biography = models.TextField(null=True, blank=True, verbose_name="بیوگرافی")
    birth_date = models.DateField(null=True, blank=True, verbose_name="تاریخ تولد")
    nationality = models.CharField(
        max_length=100, null=True, blank=True, verbose_name="ملیت"
    )
    website = models.URLField(null=True, blank=True, verbose_name="وب‌سایت")

    class Meta:
        verbose_name = "نویسنده"
        verbose_name_plural = "نویسندگان"
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Publisher(models.Model):
    name = models.CharField(max_length=255, verbose_name="نام")
    address = models.TextField(null=True, blank=True, verbose_name="آدرس")
    phone_number = models.CharField(
        max_length=20, null=True, blank=True, verbose_name="شماره تماس"
    )
    website = models.URLField(null=True, blank=True, verbose_name="وب‌سایت")

    class Meta:
        verbose_name = "ناشر"
        verbose_name_plural = "ناشران"
    
    def __str__(self):
        return self.name
