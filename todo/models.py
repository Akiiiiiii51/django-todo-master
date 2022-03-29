from django.db import models 
 
 
class Todo(models.Model): 
    #todo = models.CharField('ToDo', max_length=100, blank=False)
    
    # タイトル（100文字までで、空白は許可しない）
    #todo = models.CharField('タイトル', max_length=100, blank=False)
    title = models.CharField('タイトル', max_length=100, blank=False)
    # 本文
    text = models.TextField('本文')
    
    created_at = models.DateTimeField('作成日時', auto_now_add=True)
    updated_at = models.DateTimeField('更新日時',auto_now=True)
    
    def __str__(self):
        return self.todo