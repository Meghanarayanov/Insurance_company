from django.shortcuts import render

# Create your views here.
def admindashboard(request):
    return render(request,'admindashboard.html')
def addagent(request):
    return render(request,'addagent.html')
def viewagent(request):
    return render(request,'viewagent.html')
def campaign(request):
    return render(request,'campaign.html')
def update_agent(request):
    return render(request,'updateagent.html')

def client_details(request):
    return render(request,'clientdetails.html')
def clientdetail_view(request):
    return render(request,'clientdetails_view.html')
def createcampaign(request):
    return render(request,'createcampaign.html')
def assignagentcampaign(request):
    return render(request,'assignagentcampaign.html')

def agentdashboard(request):
    return render(request,'agentdashboard.html')
def agent_profile(request):
    return render(request,'agent_profile.html')
def edit_agent(request):
    return render(request,'edit_agent.html')
def change_password(request):
    return render(request,'change_password.html')
def cutomer_informations(request):
    return render(request,'customerinformation.html')





