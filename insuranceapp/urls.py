from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
   
    path("",views.index,name="index"),
    path("loginpage",views.loginpage,name="loginpage"),
    path("login_db",views.login_db,name="login_db"),
    path("contactus",views.contactus,name="contactus"),
    path('admindashboard',views.admindashboard,name='admindashboard'),
    path('addagent',views.addagent,name='addagent'),
    path('viewagent',views.viewagent,name='viewagent'),
    path('campaign',views.campaign,name='campaign'),
    path('update_agent',views.update_agent,name='update_agent'),
    path('client_details',views.client_details,name='client_details'),
    path('clientdetail_view',views.clientdetail_view,name='clientdetail_view'),
    path('back',views.back,name='back'),
    path('createcampaign',views.createcampaign,name='createcampaign'),
    path('assignagentcampaign',views.assignagentcampaign,name='assignagentcampaign'),
    path('agentdashboard',views.agentdashboard,name='agentdashboard'),
    path('agent_profile',views.agent_profile,name='agent_profile'),
    path('edit_agent',views.edit_agent,name='edit_agent'),
    path('change_password',views.change_password,name='change_password'),
    path('customer_informations',views.customer_informations,name='customer_informations'),
    path('customer_detail',views.customer_detail,name='customer_detail'),
    path('customerdetails_view',views.customerdetails_view,name='customerdetails_view'),
     path('backagent',views.backagent,name='backagent'),
    path("logout",views.logout,name="logout"),
   
   
   
   
]