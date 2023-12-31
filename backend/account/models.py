from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, phonenumber, password = None):
        if not email:
            raise ValueError("User must have email address")
        
        email = self.normalize_email(email)
        
        user = self.model(
            email = email,
            first_name = first_name,
            last_name = last_name,
            phonenumber = phonenumber
        )
        
        user.set_password(password)
        user.save(using = self._db)
        return user
    
    #superadmin@gmail.com qwerty
    def create_superuser(self, email, first_name, last_name, phonenumber, password = None):
        user = self.create_user(email, first_name, last_name, phonenumber, password)
        
        
        user.is_staff = True
        user.is_superuser = True
        user.is_superadmin = True
        user.is_active = True
        
        user.save(using = self._db)
        
        return user
    
    def create_superadmin(self, email, first_name, last_name, phonenumber, password = None):
        user = self.create_user(email, first_name, last_name, phonenumber, password)
        
        user.is_staff = True
        user.is_superuser = True
        user.is_superadmin = True
        user.is_active = True
        
        user.save(using = self._db)
        
        return user
    
    def create_admin(self, email, first_name, last_name, phonenumber, password = None):
        user = self.create_user(email, first_name, last_name, phonenumber, password)
        
        # user.is_superuser = True
        # user.is_staff = True    
        user.is_admin = True    
        user.save(using = self._db)
        
        return user
    
    def create_employee(self, email, first_name, last_name, phonenumber, password = None):
        user = self.create_user(email, first_name, last_name, phonenumber, password)
        
        # user.is_superuser = True
        # user.is_staff = True    
        user.is_employee = True 
        user.is_active = True   
        user.save(using = self._db)
        
        return user
        


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phonenumber = models.CharField(max_length=20, default = "+77777777777")
    
    
    is_active = models.BooleanField(default=False)
    is_staff= models.BooleanField(default=False)
    
    is_superadmin = models.BooleanField(default=False)
    
    is_admin = models.BooleanField(default=False)
    
    is_employee = models.BooleanField(default=False)
    
    objects = UserManager()
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "phonenumber"]
    
    def __str__(self):
        return self.email
        