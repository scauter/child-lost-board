from django.db import models

from users.models import User

class Room(models.Model):
    num = models.CharField(
        verbose_name='部屋番号',
        max_length=8,
        blank=False,
        null=False,
    )
    
    def __str__(self):
        return self.num

    class Meta:
        verbose_name = '部屋番号'
        verbose_name_plural = '部屋番号'

class LostChildInfo(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    content = models.CharField(
        verbose_name='部屋番号',
        max_length=400,
        blank=False,
        null=False,
    )
    # 作成者(ユーザー)
    created_by = models.ForeignKey(
        User,
        verbose_name='作成者',
        blank=True,
        null=True,
        related_name='CreatedBy',
        on_delete=models.SET_NULL,
        editable=False,
    )

    # 作成時間
    created_at = models.DateTimeField(
        verbose_name='作成時間',
        blank=True,
        null=True,
        editable=False,
    )
    
    # 更新時間
    updated_at = models.DateTimeField(
        verbose_name='更新時間',
        blank=True,
        null=True,
        editable=False,
    )

    
    def __str__(self):
        return self.content

    class Meta:
        verbose_name = '迷子情報'
        verbose_name_plural = '迷子情報'
