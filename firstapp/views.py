from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import View

from .models import IndividualBanks, LegalBanks

# Create your views here.
def index(request):
    return render(request, 'firstapp/index.html')


def presentation(request):
    return render(request, 'firstapp/presentation.html')


def facialChoice(request):
    return render(request, 'firstapp/facialChoice.html')


def facialResult(request):
    if(request.GET['facialChoice'] == 'individual'):
        return render(request, 'firstapp/individual.html')
    elif(request.GET['facialChoice'] == 'legal'):
        return render(request, 'firstapp/legal.html')


def individualBanks(request):
    price = int(request.GET['yearPrice'])
    pOut = float(request.GET['percentOut'])
    pIn = float(request.GET['percentIn'])
    com = float(request.GET['comission'])
    firstCheck = bool(request.GET['services1'])
    secondCheck = bool(request.GET['services2'])
    thirdCheck = bool(request.GET['services3'])
    fourthCheck = bool(request.GET['services4'])
    fifthCheck = bool(request.GET['services5'])
    sixthCheck = bool(request.GET['services6'])
    seventhCheck = bool(request.GET['services7'])
    eighthCheck = bool(request.GET['services8'])
    ninethCheck = bool(request.GET['services9'])
    tenthCheck = bool(request.GET['services10'])
    eleventhCheck = bool(request.GET['services11'])
    

    firstPrice = IndividualBanks.objects.all() 

    startForm = []

    for i in firstPrice:
        if price >= i.first:
            if pOut >= i.second:
                if pIn >= i.third:
                    if com >= i.fourth:
                        startForm.append(i.name)

    firstService = []
    firstServiceResult = []
    if firstCheck == True:
        firstService = IndividualBanks.objects.filter(fifth = True)
    else:
        firstService = IndividualBanks.objects.all()
    
    for i in firstService:
        firstServiceResult.append(i.name)

    secondService = []
    secondServiceResult = []
    if secondCheck == True:
        secondService = IndividualBanks.objects.filter(sixth = True)
    else:
        secondService = IndividualBanks.objects.all()

    for i in secondService:
        secondServiceResult.append(i.name)

    thirdService = []
    thirdServiceResult = []
    if thirdCheck == True:
        thirdService = IndividualBanks.objects.filter(seventh = True)
    else:
        thirdService = IndividualBanks.objects.all()

    for i in thirdService:
        thirdServiceResult.append(i.name)

    fourthService = []
    fourthServiceResult = []
    if fourthCheck == True:
        fourthService = IndividualBanks.objects.filter(eighth = True)
    else:
        fourthService = IndividualBanks.objects.all()

    for i in fourthService:
        fourthServiceResult.append(i.name)

    fifthService = []
    fifthServiceResult = []
    if fifthCheck == True:
        fifthService = IndividualBanks.objects.filter(nineth = True)
    else:
        fifthService = IndividualBanks.objects.all()

    for i in fifthService:
        fifthServiceResult.append(i.name)

    sixthService = []
    sixthServiceResult = []
    if sixthCheck == True:
        sixthService = IndividualBanks.objects.filter(tenth = True)
    else:
        sixthService = IndividualBanks.objects.all()

    for i in sixthService:
        sixthServiceResult.append(i.name)

    seventhService = []
    seventhServiceResult = []
    if seventhCheck == True:
        seventhService = IndividualBanks.objects.filter(eleventh = True)
    else:
        seventhService = IndividualBanks.objects.all()

    for i in seventhService:
        seventhServiceResult.append(i.name)

    eighthService = []
    eighthServiceResult = []
    if eighthCheck == True:
        eighthService = IndividualBanks.objects.filter(twelveth = True)
    else:
        eighthService = IndividualBanks.objects.all()

    for i in eighthService:
        eighthServiceResult.append(i.name)

    ninethService = []
    ninethServiceResult = []
    if ninethCheck == True:
        ninethService = IndividualBanks.objects.filter(thirteenth = True)
    else:
        ninethService = IndividualBanks.objects.all()

    for i in ninethService:
        ninethServiceResult.append(i.name)

    tenthService = []
    tenthServiceResult = []
    if tenthCheck == True:
        tenthService = IndividualBanks.objects.filter(fourteenth = True)
    else:
        tenthService = IndividualBanks.objects.all()

    for i in tenthService:
        tenthServiceResult.append(i.name)

    eleventhService = []
    eleventhServiceResult = []
    if eleventhCheck == True:
        eleventhService = IndividualBanks.objects.filter(fifteenth = True)
    else:
        eleventhService = IndividualBanks.objects.all()

    for i in eleventhService:
        eleventhServiceResult.append(i.name)

    resultList = list(set(startForm) & set(firstServiceResult) & set(secondServiceResult) & set(thirdServiceResult) & set(fourthServiceResult) & set(fifthServiceResult) & set(sixthServiceResult) & set(seventhServiceResult) & set(eighthServiceResult) & set(ninethServiceResult) & set(tenthServiceResult) & set(eleventhServiceResult))

    if len(resultList) == 0:
        data = {'List': startForm, 'Price': price, 'FirstService': firstServiceResult, 'SecondService': secondServiceResult, 'ThirdService': thirdServiceResult,'FourthService': fourthServiceResult,'FifthService': fifthServiceResult,'SixthService': sixthServiceResult,'SeventhService': seventhServiceResult,'EighthService': eighthServiceResult,'NinethService': ninethServiceResult,'TenthService': tenthServiceResult,'EleventhService': eleventhServiceResult,'Result': resultList, 'Error': "К сожалению, система не подобрала для вас ни одного банка. Пожалуйста, измените параметры"}
    else:
        data = {'List': startForm, 'Price': price, 'FirstService': firstServiceResult, 'SecondService': secondServiceResult, 'ThirdService': thirdServiceResult,'FourthService': fourthServiceResult,'FifthService': fifthServiceResult,'SixthService': sixthServiceResult,'SeventhService': seventhServiceResult,'EighthService': eighthServiceResult,'NinethService': ninethServiceResult,'TenthService': tenthServiceResult,'EleventhService': eleventhServiceResult,'Result': resultList}
                     
    return render(request, 'firstapp/individualResult.html', context=data)
    

def legalBanks(request):
    price = int(request.GET['integrationPrice'])
    pServ = float(request.GET['servicePrice'])
    com = float(request.GET['comission'])
    firstCheck = bool(request.GET['services1'])
    secondCheck = bool(request.GET['services2'])
    thirdCheck = bool(request.GET['services3'])
    fourthCheck = bool(request.GET['services4'])
    fifthCheck = bool(request.GET['services5'])
    sixthCheck = bool(request.GET['services6'])
    seventhCheck = bool(request.GET['services7'])
    eighthCheck = bool(request.GET['services8'])
    ninethCheck = bool(request.GET['services9'])
    tenthCheck = bool(request.GET['services10'])

    firstPrice = LegalBanks.objects.all() 

    startForm = []

    for i in firstPrice:
        if price >= i.first:
            startForm.append(i.name)

    firstService = []
    firstServiceResult = []
    if firstCheck == True:
        firstService = IndividualBanks.objects.filter(fourth = True)
    else:
        firstService = IndividualBanks.objects.all()
    
    for i in firstService:
        firstServiceResult.append(i.name)

    secondService = []
    secondServiceResult = []
    if secondCheck == True:
        secondService = IndividualBanks.objects.filter(fifth = True)
    else:
        secondService = IndividualBanks.objects.all()

    for i in secondService:
        secondServiceResult.append(i.name)

    thirdService = []
    thirdServiceResult = []
    if thirdCheck == True:
        thirdService = IndividualBanks.objects.filter(sixth = True)
    else:
        thirdService = IndividualBanks.objects.all()

    for i in thirdService:
        thirdServiceResult.append(i.name)

    fourthService = []
    fourthServiceResult = []
    if fourthCheck == True:
        fourthService = IndividualBanks.objects.filter(seventh = True)
    else:
        fourthService = IndividualBanks.objects.all()

    for i in fourthService:
        fourthServiceResult.append(i.name)

    fifthService = []
    fifthServiceResult = []
    if fifthCheck == True:
        fifthService = IndividualBanks.objects.filter(eighth = True)
    else:
        fifthService = IndividualBanks.objects.all()

    for i in fifthService:
        fifthServiceResult.append(i.name)

    sixthService = []
    sixthServiceResult = []
    if sixthCheck == True:
        sixthService = IndividualBanks.objects.filter(nineth = True)
    else:
        sixthService = IndividualBanks.objects.all()

    for i in sixthService:
        sixthServiceResult.append(i.name)

    seventhService = []
    seventhServiceResult = []
    if seventhCheck == True:
        seventhService = IndividualBanks.objects.filter(tenth = True)
    else:
        seventhService = IndividualBanks.objects.all()

    for i in seventhService:
        seventhServiceResult.append(i.name)

    eighthService = []
    eighthServiceResult = []
    if eighthCheck == True:
        eighthService = IndividualBanks.objects.filter(eleventh = True)
    else:
        eighthService = IndividualBanks.objects.all()

    for i in eighthService:
        eighthServiceResult.append(i.name)

    ninethService = []
    ninethServiceResult = []
    if ninethCheck == True:
        ninethService = IndividualBanks.objects.filter(twelveth = True)
    else:
        ninethService = IndividualBanks.objects.all()

    for i in ninethService:
        ninethServiceResult.append(i.name)

    tenthService = []
    tenthServiceResult = []
    if tenthCheck == True:
        tenthService = IndividualBanks.objects.filter(thirteenth = True)
    else:
        tenthService = IndividualBanks.objects.all()

    for i in tenthService:
        tenthServiceResult.append(i.name)

    resultList = list(set(startForm) & set(firstServiceResult) & set(secondServiceResult) & set(thirdServiceResult) & set(fourthServiceResult) & set(fifthServiceResult) & set(sixthServiceResult) & set(seventhServiceResult) & set(eighthServiceResult) & set(ninethServiceResult) & set(tenthServiceResult))

    if len(resultList) == 0:
        data = {'List': startForm, 'Price': price, 'FirstService': firstServiceResult, 'SecondService': secondServiceResult, 'ThirdService': thirdServiceResult,'FourthService': fourthServiceResult,'FifthService': fifthServiceResult,'SixthService': sixthServiceResult,'SeventhService': seventhServiceResult,'EighthService': eighthServiceResult,'NinethService': ninethServiceResult, 'TenthService': tenthServiceResult, 'Result': resultList, 'Error': "К сожалению, система не подобрала для вас ни одного банка. Пожалуйста, измените параметры"}
    else:
        data = {'List': startForm, 'Price': price, 'FirstService': firstServiceResult, 'SecondService': secondServiceResult, 'ThirdService': thirdServiceResult,'FourthService': fourthServiceResult,'FifthService': fifthServiceResult,'SixthService': sixthServiceResult,'SeventhService': seventhServiceResult,'EighthService': eighthServiceResult,'NinethService': ninethServiceResult, 'TenthService': tenthServiceResult, 'Result': resultList}

    return render(request, 'firstapp/legalResult.html', context=data)
    


    
    

