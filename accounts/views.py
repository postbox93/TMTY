from django.shortcuts import render, redirect
# from django.contrib import auth.logout
# from django.contrib.auth.models import User, check_password
# Create your views here.
from django.contrib.auth import login, authenticate
from django.views.generic.detail import DetailView

from .forms import RegisterForm,SignUpForm,Basic_details,Religion_details,Personal_details,About_you
from formtools.wizard.views import SessionWizardView
from .models import Profile

class UserView(DetailView):
    template_name = 'accounts/home.html'

    def get_object(self):
        print(self.request.user)
        return self.request.user


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(request, email=user.email, password=raw_password)
            if user is not None:
                login(request, user)
            else:
                print("user is not authenticated")
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})


class ProfileView(SessionWizardView):
    template_name = "accounts/profile.html"
    model = Profile
    form_list = [Basic_details,Religion_details,Personal_details,About_you]
    def done(self, form_list, form_dict,**kwargs):
        # print("*************************************",form_dict)
        # # form_list.save()
        # add_data=Profile(**form_dict)
        # add_data.save()
        # return render(self.request, 'accounts/success.html', {
        #     'form_data': [form.cleaned_data for form in form_list],
        # })
        form_data = [form.cleaned_data for form in form_list]
        data_dict={}
        for item in form_data:
            data_dict.update(item)
        # data_dict.update({'user':CustomUser.objects.get(email=self.request.user)})
        add_data=Profile(**data_dict)
        add_data.save()
        return render(self.request, 'accounts/success.html',locals())


# class Login(object):
# 	"""
# 	Email Authentication Backend

# 	Allows a user to sign in using an email/password pair rather than
# 	a username/password pair.
# 	"""
 
# 	def authenticate(self, username=None, password=None):
# 		""" Authenticate a user based on email address as the user name. """
# 		try:
# 			user = User.objects.get(email=username)
# 			if user.check_password(password):
# 				return user
# 			except User.DoesNotExist:
# 				return None
 
# 	def get_user(self, user_id):
# 		""" Get a User object from the user_id. """
# 		try:
# 			return User.objects.get(pk=user_id)
# 	except User.DoesNotExist:
# 		return None

#  def logout_request(request):
#     logout(request)
#     messages.info(request, "Logged out successfully!")
#     return redirect("homepage")