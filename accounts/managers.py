from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _

class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_('이메일을 입력하세요!ㄟ( ▔, ▔ )ㄏ'))
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser는 is_staff값을 무조건 True로 가져야 합니당'))
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser는 is_speruser값을 무조건 True로 가져야 합니다아아'))
        
        return self.create_user(email, password, **extra_fields)    