from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from app.forms import FinancierUpdateAccountForm, PVTOrderForm
from app.models import Financier, PhysicalAddress, Appliance
#from django.contrib.auth.models import User

# Create your views here.
class Dashboard(LoginRequiredMixin, View):
    template_name = 'app/index.html'

    def get(self, request, *args, **kwargs):
        """

        """

        return render(request, self.template_name)


class Home(View):
    template_name = 'home/index.html'

    def get(self, request, *args, **kwargs):
        """

        """

        return render(request, self.template_name)


class FinancierUpdateAccount(View):
    template_name = 'registration/financier_update_account.html'
    form_class = FinancierUpdateAccountForm
    address_model_class = PhysicalAddress

    def post(self, request, *args, **kwargs):
        """

        """
        form = self.form_class()
        if form.is_valid():
            address_model = self.address_model_class(request)

            user = request.user
            company_name = form.cleaned_data['company_name']
            company_reg = form.cleaned_data['company_reg']
            contact_number = form.cleaned_data['contact_number']
            web_address = form.cleaned_data['web_address']
            physical_address = address_model.objects.create(
                building_name=form.cleaned_data['contact_number'],
                street_name=form.cleaned_data['street_name'],
                suburb=form.cleaned_data['suburb'],
                province=form.cleaned_data['province'],
                city=form.cleaned_data['city'],
                zip_code=form.cleaned_data['zip_code']
            )

            Financier.objects.create(
                user=user,
                company_name=company_name,
                company_reg=company_reg,
                contact_number=contact_number,
                web_address=web_address,
                physical_address=physical_address)
            
        return render(request , self.template_name)
        
    def get(self, request, *args, **kwargs):
    
        """
        """
        
        form = self.form_class()

        context = {'form':form}
        
        return render(request, self.template_name, context)


class OurProducts(View):
    template_name = 'home/products.html'

    def get(self, request, *args, **kwargs):
        """

        """

        return render(request, self.template_name)


class PVT(View):
    template_name = 'home/pvt.html'

    def get(self, request, *args, **kwargs):
        """

        """

        return render(request, self.template_name)

class SolarGeyser(View):
    template_name = 'home/geyser.html'

    def get(self, request, *args, **kwargs):
        """

        """

        return render(request, self.template_name)


class SolarComponent(View):
    template_name = 'home/component.html'

    def get(self, request, *args, **kwargs):
        """

        """

        return render(request, self.template_name)

class Register(View):
    template_name = 'home/register.html'

    def get(self, request, *args, **kwargs):
        """

        """

        return render(request, self.template_name)

class ClientOrder(View):
    template_name = 'app/client_order.html'
    """
    address_model_class = PhysicalAddress

    def post(self, request, *args, **kwargs):
        form = self.form_class()
        if form.is_valid():
            address_model = self.address_model_class(request)

            user = request.user
            company_name = form.cleaned_data['company_name']
            company_reg = form.cleaned_data['company_reg']
            contact_number = form.cleaned_data['contact_number']
            web_address = form.cleaned_data['web_address']
            physical_address = address_model.objects.create(
                building_name=form.cleaned_data['contact_number'],
                street_name=form.cleaned_data['street_name'],
                suburb=form.cleaned_data['suburb'],
                province=form.cleaned_data['province'],
                city=form.cleaned_data['city'],
                zip_code=form.cleaned_data['zip_code']
            )

            Financier.objects.create(
                user=user,
                company_name=company_name,
                company_reg=company_reg,
                contact_number=contact_number,
                web_address=web_address,
                physical_address=physical_address)
            
        return render(request , self.template_name)
        """
    def get(self, request, *args, **kwargs):
        """
        """
        return render(request, self.template_name)


class OrderPVTSystem(View):
    template_name = 'registration/pvt_order.html'
    form_class = PVTOrderForm
    appliances_model_class = Appliance

    def post(self, request, *args, **kwargs):
        """
        """
        form = self.form_class()
        if form.is_valid():
            appliances_model = self.appliances_model_class(request)

            user = request.user
            intended_use = form.cleaned_data['intended_use']
            site_visit = form.cleaned_data['site_visit']
            property_type = form.cleaned_data['property_type']
            roof_inclination = form.cleaned_data['roof_inclination']

            possible_appliances = appliances_model.objects.create(
                form.cleaned_data['name'])
            
            PVTSystem.objects.create(
                user=user,
                roof_inclination=roof_inclination,
                property_type=property_type,
                site_visit=site_visit,
                possible_appliances=possible_appliances,
                intended_use=intended_use)
            
        return render(request , self.template_name)
        
    def get(self, request, *args, **kwargs):
    
        """
        """
        
        form = self.form_class()

        context = {'form':form}
        
        return render(request, self.template_name, context)
