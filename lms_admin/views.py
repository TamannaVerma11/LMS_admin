from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from lms_admin.models import *
from django.http import *
import mimetypes
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def login_user(request):
    message = ''
    if request.method == 'POST':
        authenticate(
            email = request.POST['email'],
            password = request.POST['password']
        )
        user = User.objects.get(email = request.POST['email'])
        if user is not None:
            login(request,user)
            return redirect('dashboard')
        else:
            message = 'Login Failed'
    return render(request, 'login.html', context={'message' : message})

def logout_user(request):
    logout(request)
    return redirect('login')

def signup_user(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_type = request.POST.get('user_type')
        dob = request.POST.get('dob')
        city = request.POST.get('city')
        pincode = request.POST.get('pincode')
        address = request.POST.get('address')
        is_active = 1
        qualification = request.POST.get('qualification')
        experience = request.POST.get('experience')
        resume = request.FILES.get('resume')
        mobile = request.POST.get('mobile')
        user = User.objects.create(
            username = first_name+last_name,
            first_name = first_name,
            last_name = last_name,
            email = email,
            password = make_password(password), 
            is_active = is_active
        )
        Files.objects.create(
            file_type =mimetypes.guess_type(resume),
            path = resume,
            model_ob = 'UserInfo'
        )
        UserInfo.objects.create(
            user_type = user_type,
            dob = dob,
            city = city,
            pincode = pincode,
            address = address,
            qualification = qualification,
            experience = experience,
            mobile = mobile
        )

        login(request, user)
        return redirect('dashboard')

@login_required(login_url='login')
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required(login_url='login')
def category(request):
    category = Category.objects.filter(status = 1)
    return render(request, 'category/index.html', context={'categories' : category})

@login_required(login_url='login')
def add_category(request):
    if request.method == 'POST':
        Category.objects.create(
            name = request.POST.get('name'),
            image = request.FILES.get('image'),
            status = request.POST.get('status')
        )
        messages.success(request, 'Category created successfully.')
        return redirect('category')
    return render(request, 'category/add.html')

@login_required(login_url='login')
def edit_category(request, id):
    category = Category.objects.get(id=id)
    if request.method == 'POST':
        Category.objects.filter(id=id).update(
            name = request.POST.get('name'),
            image = request.FILES.get('image'),
            status = request.POST.get('status')
        )
        messages.success(request, 'Category updated successfully.')
        return redirect('category')
    return render(request, 'category/edit.html', context={'category' : category})

@login_required(login_url='login')
def delete_category(request, id):
    category = Category.objects.get(id=id)
    category.delete()
    messages.success(request, 'Categotry deleted successfully')
    return redirect('category')

@login_required(login_url='login')
def sub_category(request):
    sub_category = SubCategory.objects.filter(status = 1)
    return render(request, 'sub-category/index.html', context={'subcategories' : sub_category})

@login_required(login_url='login')
def add_sub_category(request):
    categories = Category.objects.filter(status = 1)
    if request.method == 'POST':
        SubCategory.objects.create(
            name = request.POST.get('name'),
            image = request.FILES.get('image'),
            status = request.POST.get('status'),
            category = Category.objects.get(id=request.POST.get('category'))
        )
        messages.success(request, 'Subcategory created successfully.')
        return redirect('sub_category')
    return render(request, 'sub-category/add.html', context={'categories' : categories})

@login_required(login_url='login')
def edit_sub_category(request, id):
    categories = Category.objects.filter(status = 1)
    sub_category = SubCategory.objects.get(id=id)
    if request.method == 'POST':
        SubCategory.objects.filter(id=id).update(
            name = request.POST.get('name'),
            status = request.POST.get('status'),
            category = Category.objects.get(id=request.POST.get('category'))
        )
        messages.success(request, 'Subcategory updated successfully.')
        return redirect('sub_category')
    return render(request, 'sub-category/edit.html', context={'sub_category' : sub_category, 'categories' : categories})

@login_required(login_url='login')
def delete_sub_category(request, id):
    sub_category = SubCategory.objects.get(id=id)
    sub_category.delete()
    messages.success(request, 'Subcategory deleted successfully')
    return redirect('sub_category')

@login_required(login_url='login')
def blog(request):
    blogs = Blogs.objects.filter(status = 1)
    return render(request, 'blog/index.html', context={'blogs' : blogs})

@login_required(login_url='login')
def add_blog(request):
    if request.method == 'POST':
        Blogs.objects.create(
            title = request.POST.get('title'),
            image = request.FILES.get('image'),
            description = request.POST.get('description'),
            status = request.POST.get('status'),
            created_by = request.user
        )
        messages.success(request, 'Blog created successfully.')
        return redirect('blog')
    return render(request, 'blog/add.html')

@login_required(login_url='login')
def edit_blog(request, id):
    blog = Blogs.objects.get(id=id)
    if request.method == 'POST':
        Blogs.objects.filter(id=id).update(
            title = request.POST.get('title'),
            image = request.FILES.get('image'),
            description = request.POST.get('description'),
            status = request.POST.get('status')
        )
        messages.success(request, 'Blog updated successfully.')
        return redirect('blog')
    return render(request, 'blog/edit.html', context={'blog' : blog})

@login_required(login_url='login')
def delete_blog(request, id):
    blog = Blogs.objects.get(id=id)
    blog.delete()
    messages.success(request, 'Blog deleted successfully')
    return redirect('blog')

@login_required(login_url='login')
def page(request):
    pages = WebsiteData.objects.filter(status = 1)
    return render(request, 'page/index.html', context={'pages' : pages})

@login_required(login_url='login')
def add_page(request):
    if request.method == 'POST':
        WebsiteData.objects.create(
            section = request.POST.get('section'),
            image = request.FILES.get('image'),
            description = request.POST.get('description'),
            status = request.POST.get('status')
        )
        messages.success(request, 'Page created successfully.')
        return redirect('page')
    return render(request, 'page/add.html')

@login_required(login_url='login')
def edit_page(request, id):
    page = WebsiteData.objects.get(id=id)
    if request.method == 'POST':
        WebsiteData.objects.filter(id=id).update(
            section = request.POST.get('section'),
            image = request.FILES.get('image'),
            description = request.POST.get('description'),
            status = request.POST.get('status')
        )
        messages.success(request, 'Page updated successfully.')
        return redirect('page')
    return render(request, 'page/edit.html', context={'page' : page})

@login_required(login_url='login')
def delete_page(request, id):
    page = WebsiteData.objects.get(id=id)
    page.delete()
    messages.success(request, 'Page deleted successfully')
    return redirect('page')

@login_required(login_url='login')
def query(request):
    queries = Queries.objects.all()
    return render(request, 'query/index.html', context={'queries' : queries})

@login_required(login_url='login')
def course(request):
    courses = Course.objects.filter(status = 1)
    return render(request, 'course/index.html', context={'courses' : courses})

@login_required(login_url='login')
def add_course(request):
    users = UserInfo.objects.filter(user_type='tutor')
    if request.method == 'POST':
        Course.objects.create(
            name = request.POST.get('name'),
            image = request.FILES.get('image'),
            description = request.POST.get('description'),
            status = request.POST.get('status'),
            tutor = request.POST.get('tutor'),
            price = request.POST.get('price')
        )
        messages.success(request, 'Course created successfully.')
        return redirect('course')
    return render(request, 'course/add.html', context={'users' : users})

@login_required(login_url='login')
def edit_course(request, id):
    course = Course.objects.get(id=id)
    users = UserInfo.objects.filter(user_type='tutor')
    if request.method == 'POST':
        Course.objects.filter(id=id).update(
            name = request.POST.get('name'),
            image = request.FILES.get('image'),
            description = request.POST.get('description'),
            status = request.POST.get('status'),
            tutor = request.POST.get('tutor'),
            price = request.POST.get('price')
        )
        messages.success(request, 'Course updated successfully.')
        return redirect('course')
    return render(request, 'course/edit.html', context={'course' : course, 'users' : users})

@login_required(login_url='login')
def delete_course(request, id):
    course = Course.objects.get(id=id)
    course.delete()
    messages.success(request, 'Course deleted successfully')
    return redirect('course')