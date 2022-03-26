from django.contrib import messages
from django.shortcuts import render, redirect

# from .forms import UserForm, customerForm

# Create your views here.
from .filters import FoodFilter
from .forms import UserForm, customerForm, chefForm, waiterForm, FoodForm, incredientsForm, OrderForm, TableForm, \
    TablForm, TabForm
from .models import chef, waiter, incre_req, food, customer, food_order, table_order, table


def index(request):
    return render(request, 'index.html')


def home(request):
    return render(request, 'ho/home.html')


def adminpag(request):
    return render(request, 'ad/index.html')


def register(request):
    return render(request, 'register/register.html')


def userview(request):
    user = request.user
    if (user.is_staff):
        return redirect('adminpag')
    elif (user.is_chef):
        return redirect('chef_home')
    elif (user.is_customer):
        return redirect('customer_home')
    elif (user.is_waiter):
        return redirect('waiter_home')
    else:
        return redirect('index')


def waiter_home(request):
    return render(request, 'waiter/index.html')


def chef_home(request):
    return render(request, 'chef/index.html')


def customer_home(request):
    return render(request, 'customer/index.html')


def add_customer(request):
    form = UserForm()
    n_form = customerForm()
    if request.method == 'POST':
        form = UserForm(request.POST, )
        n_form = customerForm(request.POST, )
        if form.is_valid() and n_form.is_valid():
            user = form.save(commit=False)
            user.is_customer = True
            user.save()
            s = n_form.save(commit=False)
            s.user = user
            s.save()
            messages.info(request, 'Add Successfully')
            return redirect('add_customer')
    return render(request, 'register/register.html', {'form': form, 'n_form': n_form})


def add_chef(request):
    form = UserForm()
    n_form = chefForm()
    if request.method == 'POST':
        form = UserForm(request.POST, )
        n_form = chefForm(request.POST, )
        if form.is_valid() and n_form.is_valid():
            user = form.save(commit=False)
            user.is_chef = True
            user.save()
            s = n_form.save(commit=False)
            s.user = user
            s.save()
            messages.info(request, 'Add Successfully')
            return redirect('add_chef')
    return render(request, 'ad/add_chef.html', {'form': form, 'n_form': n_form})


def view_chef(request):
    dataset = chef.objects.all()
    context = {
        'data': dataset
    }
    return render(request, 'ad/view_chef.html', context)


def update_chef(request, id=None):
    data = chef.objects.get(id=id)
    m_form = chefForm(instance=data)
    if request.method == 'POST':
        m_form = chefForm(request.POST, instance=data)
        if m_form.is_valid():
            m_form.save()
            # messages.info(request, ' updated Successfully')
            return redirect('view_chef')

    return render(request, 'ad/update.html', {'m_form': m_form})


def delete_chef(request, id=None):
    data = chef.objects.get(id=id)
    data.delete()
    return redirect('view_chef')


def add_waiter(request):
    form = UserForm()
    n_form = waiterForm()
    if request.method == 'POST':
        form = UserForm(request.POST, )
        n_form = waiterForm(request.POST, )
        if form.is_valid() and n_form.is_valid():
            user = form.save(commit=False)
            user.is_waiter = True
            user.save()
            s = n_form.save(commit=False)
            s.user = user
            s.save()
            messages.info(request, 'Add Successfully')
            return redirect('add_waiter')
    return render(request, 'ad/add_waiter.html', {'form': form, 'n_form': n_form})


def view_waiter(request):
    dataset = waiter.objects.all()
    context = {
        'data': dataset
    }
    return render(request, 'ad/view_waiter.html', context)


def update_waiter(request, id=None):
    data = waiter.objects.get(id=id)
    m_form = waiterForm(instance=data)
    if request.method == 'POST':
        m_form = waiterForm(request.POST, instance=data)
        if m_form.is_valid():
            m_form.save()
            # messages.info(request, ' updated Successfully')
            return redirect('view_waiter')

    return render(request, 'ad/update_waiter.html', {'m_form': m_form})


def delete_waiter(request, id=None):
    data = waiter.objects.get(id=id)
    data.delete()
    return redirect('view_waiter')


def view_re(request):
    dataset = table_order.objects.all()
    context = {
        'data': dataset
    }
    return render(request, 'ad/view_req.html', context)


def approve(request, id):
    req = table_order.objects.get(id=id)
    req.t_status = 1

    req.save()

    messages.info(request, 'Approved ')
    return redirect('view_re')


def reject(request, id):
    req = table_order.objects.get(id=id)
    req.t_status = 2
    req.save()
    messages.info(request, 'Rejected  ')
    return redirect('view_re')


# -------------------chef-------------------------------------------------------------------


def add_food(request):
    u = chef.objects.get(user=request.user)
    b_form = FoodForm()
    if request.method == 'POST':
        b_form = FoodForm(request.POST, request.FILES)
        if b_form.is_valid():
            ob = b_form.save(commit=False)
            ob.c = u
            ob.save()
            messages.info(request, ' Successfull')
            return redirect('add_food')
    return render(request, 'chef/add_food.html', {'b_form': b_form})


# def view_food(request):
#     dataset = food.objects.all()
#     context = {
#         'data': dataset
#     }
#     return render(request, 'customer/menu.html', context)

def view_food(request):
    f = food.objects.all()
    foodFilter = FoodFilter(request.GET, queryset=f)
    f = foodFilter.qs
    context = {
        'foods': f,
        'foodFilter': foodFilter
    }
    return render(request, 'customer/menu.html', context)


def add_req(request):
    u = chef.objects.get(user=request.user)
    b_form = incredientsForm()
    if request.method == 'POST':
        b_form = incredientsForm(request.POST, request.FILES)
        if b_form.is_valid():
            ob = b_form.save(commit=False)
            ob.c = u
            ob.save()
            messages.info(request, ' Successfull')
            return redirect('add_req')
    return render(request, 'chef/incredients_req.html', {'b_form': b_form})


# def add_order(request):
#     u = customer.objects.get(user=request.user)
#     b_form = OrderForm()
#     if request.method == 'POST':
#         b_form = OrderForm(request.POST, request.FILES)
#         if b_form.is_valid():
#
#
#             ob = b_form.save(commit=False)
#             ob.custom = u
#             ob.pay_status = 1
#
#             ob.save()
#             messages.info(request, ' Successfull')
#             return redirect('add_order')
#     return render(request, 'customer/add_order.html', {'b_form': b_form})


# def add_order(request):
#     u = customer.objects.get(user=request.user)
#     b_form = OrderForm()
#     if request.method == 'POST':
#         b_form = OrderForm(request.POST, request.FILES)
#         if b_form.is_valid():
#             tbl = b_form.cleaned_data['table_no']

#         ob = b_form.save(commit=False)
#         ob.custom = u
#         ob.pay_status = 1
#         ret = food_order.objects.filter(table_no=tbl)
#         if ret.exists():
#             messages.info(request, 'This table Already assigned ')
#         else:
#             ob.save()
#             messages.info(request, ' Successfull')
#             return redirect('add_order')
# return render(request, 'customer/add_order.html', {'b_form': b_form})


def add_order(request, id):
    u = customer.objects.get(user=request.user)
    accessory = food.objects.get(id=id)
    t = table.objects.all()
    print(t)
    if request.method == 'POST':
        FoodName = request.POST.get('FoodName')
        food_type = request.POST.get('food_type')
        Price = request.POST.get('Price')
        table_no = request.POST.get('table_no')
        phone = request.POST.get('phone')
        cardnumber = request.POST.get('cardnumber')
        cvv = request.POST.get('cvv')
        date = request.POST.get('date')
        ob = food_order()
        ob.FoodName = FoodName
        ob.food_type = food_type
        ob.Price = Price
        ob.table_no = table_no
        ob.phone = phone
        ob.cardnumber = cardnumber
        ob.cvv = cvv
        ob.date = date
        ob.custom = u
        ob.pay_status = 1
        ret = food_order.objects.filter(table_no=table_no)
        if ret.exists():
            messages.info(request, 'This table Already assigned ')
        else:
            ob.save()
            messages.info(request, 'Request')
            return redirect('view_order')
    return render(request, 'customer/add_order.html', {'key': accessory, 't': t})


def add_tables(request):
    b_form = TableForm()
    if request.method == 'POST':
        b_form = TableForm(request.POST, )
        if b_form.is_valid():
            ob = b_form.save(commit=False)

            ob.save()
            messages.info(request, 'Successfull')
            return redirect('add_tables')

    return render(request, 'ad/add_tables.html', {'b_form': b_form})


def add_rtables(request):
    b_form = TablForm()
    if request.method == 'POST':
        b_form = TablForm(request.POST, )
        if b_form.is_valid():
            ob = b_form.save(commit=False)

            ob.save()
            messages.info(request, 'Successfull')
            return redirect('add_rtables')

    return render(request, 'ad/add_reservation_tables.html', {'b_form': b_form})


def view_order(request):
    u = customer.objects.get(user=request.user)
    dataset = food_order.objects.filter(custom=u)
    context = {
        'data': dataset
    }
    return render(request, 'customer/view_order.html', context)


def view_table_req(request):
    u = customer.objects.get(user=request.user)
    dataset = table_order.objects.filter(custom=u)
    context = {
        'data': dataset
    }
    return render(request, 'customer/view_treq.html', context)


# ====================================chef--------------
def view_req(request):
    dataset = food_order.objects.all()
    context = {
        'data': dataset
    }
    return render(request, 'chef/view_req.html', context)


def ap(request, id):
    req = food_order.objects.get(id=id)
    req.order_status = 1

    req.save()

    messages.info(request, 'Approved ')
    return redirect('view_req')


def rej(request, id):
    req = food_order.objects.get(id=id)
    req.order_status = 2
    req.save()
    messages.info(request, 'Rejected  ')
    return redirect('view_req')


# -------------------------------waiter---------------------------

def view_request(request):
    dataset = food_order.objects.all()
    context = {
        'data': dataset
    }
    return render(request, 'waiter/view_confirmed_req.html', context)


def apr(request, id):
    req = food_order.objects.get(id=id)
    req.delivered_status = 1

    req.save()

    messages.info(request, 'Approved ')
    return redirect('view_request')


def reje(request, id):
    req = food_order.objects.get(id=id)
    req.delivered_status = 2
    req.save()
    messages.info(request, 'Rejected  ')
    return redirect('view_request')


# ------------------------------customer----------------------------

def view_che(request):
    dataset = chef.objects.all()
    context = {
        'data': dataset
    }
    return render(request, 'customer/view_chef.html', context)


def order_table(request):
    u = customer.objects.get(user=request.user)
    b_form = TabForm()
    if request.method == 'POST':
        b_form = TabForm(request.POST, )
        if b_form.is_valid():
            tbl = b_form.cleaned_data['table_no']

            ob = b_form.save(commit=False)
            ob.custom = u
            ret = table_order.objects.filter(table_no=tbl)
            if ret.exists():
                messages.info(request, 'This table Already BOOKED SELCT ANOTHER ONE ')
            else:
                ob.save()
                messages.info(request, ' Successfull')
                return redirect('order_table')
    return render(request, 'customer/tablebook.html', {'b_form': b_form})


def view_in(request):
    dataset = incre_req.objects.all()
    context = {
        'data': dataset
    }
    return render(request, 'ad/view_in.html', context)


def view_menu(request):
    f = food.objects.all()
    foodFilter = FoodFilter(request.GET, queryset=f)
    f = foodFilter.qs
    context = {
        'foods': f,
        'foodFilter': foodFilter
    }
    return render(request, 'menu.html', context)


def update_food(request, id=None):
    data = food.objects.get(id=id)
    m_form = FoodForm(instance=data)
    if request.method == 'POST':
        m_form = FoodForm(request.POST, instance=data)
        if m_form.is_valid():
            m_form.save()
            # messages.info(request, ' updated Successfully')
            return redirect('view_foods')

    return render(request, 'chef/update_food.html', {'m_form': m_form})


def view_foods(request):
    dataset = food.objects.all()
    context = {
        'data': dataset
    }
    return render(request, 'chef/view_food.html', context)


def delete_food(request, id=None):
    data = food.objects.get(id=id)
    data.delete()
    return redirect('view_foods')


def view_payment(request):
    dataset = food_order.objects.all()
    context = {
        'data': dataset
    }
    return render(request, 'ad/view_payment.html', context)


def food_or(request, id):
    accessory = food.objects.get(id=id)
    t = table.objects.all()
    print(t)
    if request.method == 'POST':
        FoodName = request.POST.get('FoodName')
        food_type = request.POST.get('food_type')
        Price = request.POST.get('Price')
        table_no = request.POST.get('table_no')
        phone = request.POST.get('phone')
        cardnumber = request.POST.get('cardnumber')
        cvv = request.POST.get('cvv')
        date = request.POST.get('date')
        ob = food_order()
        ob.FoodName = FoodName
        ob.food_type = food_type
        ob.Price = Price
        ob.table_no = table_no
        ob.phone = phone
        ob.cardnumber = cardnumber
        ob.cvv = cvv
        ob.date = date
        ob.pay_status = 1
        ret = food_order.objects.filter(table_no=table_no)
        if ret.exists():
            messages.info(request, 'This table Already assigned ')
        else:
            ob.save()
            messages.info(request, 'Request')
            return redirect('view_menu')
    return render(request, 'add_order.html', {'key': accessory, 't': t})
