from django.db import models


# Create your models here.


class Menu(models.Model):
    name = models.CharField(max_length=250,
                            unique=True,
                            null=False,
                            verbose_name='Menu name')
    uri = models.TextField(max_length=250, unique=True, null=False, default='donnu/')


    def __str__(self):
        return self.name


class Submenu(models.Model):
    submenu_name = models.CharField(max_length=250,
                            unique=True,
                            null=False,
                            verbose_name='Submenu name')

    menu = models.ForeignKey('Menu',
                             on_delete=models.CASCADE,
                             default=None,
                             null=False,
                             verbose_name='Related menu')

    parent_menu = models.ForeignKey("Submenu",
                                    on_delete=models.CASCADE,
                                    default=None,
                                    null=True,
                                    blank=True,
                                    verbose_name='Parent'
                                    )

    uri = models.CharField(max_length=250,
                           unique=True,
                           null=False,
                           blank=False,
                           default='donnu',
                           verbose_name='URI')

    named_url = models.CharField(max_length=250,
                                 null=True,
                                 default=None,
                                 blank=True,
                                 verbose_name='URL name(if any)')

    def __str__(self):
        return self.submenu_name


