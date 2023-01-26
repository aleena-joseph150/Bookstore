from django import forms
class regform(forms.Form): #capital letter F
    fname=forms.CharField(max_length=30)
    uname = forms.CharField(max_length=30)
    email=forms.EmailField()
    phno=forms.IntegerField()
    passw=forms.CharField(max_length=20)
    cpassw=forms.CharField(max_length=20)
    place=forms.CharField(max_length=20)
    utype = forms.CharField(max_length=20)

class logform(forms.Form):
    uname=forms.CharField(max_length=20)
    psw=forms.CharField(max_length=20)

class storeregform(forms.Form):
    username = forms.CharField(max_length=30)
    email = forms.EmailField()
    password = forms.CharField(max_length=20)

class storelogform(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=20)

class bookform(forms.Form):
    bname=forms.CharField(max_length=20)
    bprice=forms.IntegerField()
    des=forms.CharField(max_length=20)
    image=forms.FileField()



class profileform(forms.Form):
    name=forms.CharField(max_length=20)
    cid = forms.IntegerField()
    phn = forms.IntegerField()
    loc = forms.CharField(max_length=50)

