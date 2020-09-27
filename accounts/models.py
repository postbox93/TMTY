from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from .managers import UserManager

# Create your models here.


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False) # a admin user; non super-user
    admin = models.BooleanField(default=False) # a superuser
    # notice the absence of a "Password field", that is built in.

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] # Email & Password are required by default.
    objects = UserManager()

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
    
    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin

    @property
    def is_active(self):
        "Is the user active?"
        return self.active




class Profile(models.Model):
    TELUGU = 'TE'
    ENGLISH = 'EN'
    HINDI = 'HI'
    TAMIL = 'TL'
    MOTHER_TONGUE_CHOICES = [
        (TELUGU , 'telugu'),
        (ENGLISH , 'english'),
        (HINDI , 'hindi'),
        (TAMIL , 'tamil'),
    ]
    HINDU = 'HN'
    MUSLIM = 'MS'
    CASTE_CHOICES = [
        (HINDU , 'hindu'),
        (MUSLIM , 'muslim'),
    ]
    NO = 'NO'
    YES = 'YS'
    DONTKNOW = 'DK'
    DOSHAM_CHOICES = [
        (NO , 'no'),
        (YES , 'yes'),
        (DONTKNOW , 'dontknow'),
    ]
    NEVER_MARRIED = 'NM'
    WINDOWED = 'WD'
    DIVERCED = 'DI'
    AWAITING_DIVERCE = 'AD'
    MIDDLE_CLASS = 'MC'
    UPPER_MIDDLE_CLASS ='UMC'
    RICH = 'RH'
    AFFLUENT ='AE'
    JOINT = 'JT'
    NUCLEAR = 'NR'
    ORTHODOX = 'OX'
    TRADITIONAL = 'TRL'
    MODERATE = 'MRT'
    LIBERAL ='LRL'
    NORMAL = 'NL'
    PHISHYCALLY_CHALLANGED = 'PHD'
    FIVE_FT = '5'
    SIX_FT = '6'
    MARITAL_STATUS_CHOICES = [
        (NEVER_MARRIED , 'never_married'),
        (WINDOWED , 'windowed'),
        (DIVERCED , 'diverced'),
        (AWAITING_DIVERCE , 'awaiting_diverce'),
    ]
    HEIGHT_CHOICES = [
        (FIVE_FT , '5_ft'),
        (SIX_FT , '6_ft'),
    ]
    FAMILY_STATUS_CHOICES = [
        (MIDDLE_CLASS , 'middle class'),
        (UPPER_MIDDLE_CLASS  , 'upeer middle class'),
        (RICH , 'rich'),
        (AFFLUENT , 'affluent'),
    ]
    FAMILY_TYPE_CHOICES = [
        (JOINT , 'joint'),
        (NUCLEAR , 'nuclear'),
    ]
    FAMILY_VALUES_CHOICES = [
        (ORTHODOX , 'orthodox'),
        (TRADITIONAL , 'traditional'),
        (MODERATE , 'moderate'),
        (LIBERAL , 'liberal'),
    ]
    ANY_DISABILITY_CHOICES = [
        (NORMAL , 'normal'),
        (PHISHYCALLY_CHALLANGED , 'physically challanged'),

    ]


    # user = models.OneToOneField(User, on_delete = models.CASCADE)
    name = models.CharField(max_length = 30)
    date_of_birth = models.DateField()
    religion = models.CharField(max_length = 30)
    mother_tongue = models.CharField(
        max_length = 2,
        choices = MOTHER_TONGUE_CHOICES,
    )
    caste = models.CharField(
        max_length = 2,
        choices = CASTE_CHOICES,
    )
    gothram = models.CharField(max_length=40)
    dosham = models.CharField(
        max_length= 2,
        choices = DOSHAM_CHOICES,
    )
    marital_status = models.CharField(
        max_length= 3,
        choices = MARITAL_STATUS_CHOICES,
    )
    height = models.CharField(
        max_length= 3,
        choices = HEIGHT_CHOICES,
    )
    family_status = models.CharField(
        max_length= 3,
        choices = FAMILY_STATUS_CHOICES,
    )
    family_type = models.CharField(
        max_length= 3,
        choices = FAMILY_TYPE_CHOICES,
    )
    family_values = models.CharField(
        max_length= 3,
        choices = FAMILY_VALUES_CHOICES,
    )
    any_diability = models.CharField(
        max_length= 3,
        choices = ANY_DISABILITY_CHOICES,
    )
    about_you = models.TextField()


