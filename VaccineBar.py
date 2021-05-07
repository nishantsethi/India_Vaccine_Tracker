
from datetime import date
import datetime
import calendar
import pandas as pd


def VaccinesBar():
    fill = "▓"
    empty ="░"
    indiaVacData = "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/country_data/India.csv"
    df = pd.read_csv(indiaVacData)
    todaydf = df.iloc[[-1]]
    totalVaccinations = sum(todaydf['total_vaccinations']) #Total num of shots till now
    peopleSingleDosed = sum(todaydf['people_vaccinated']) #Total number of People have have recieved 1 dose
    peopleFullyVaccinated = sum(todaydf['people_fully_vaccinated']) #Total number of People have have recieved 2 dose
    vaccineShotsToday = sum(df.iloc[[-1]]['total_vaccinations']) - sum(df.iloc[[-2]]['total_vaccinations']) #Number of People have have recieved dose today
    indiaPopulation = 1366417754
    with open('last.txt', 'r') as file:
        vaccineShotsYest,prevDate = file.read().split(",")

    vaccineShotsYest = int(vaccineShotsYest)
    prevDate = int(prevDate)
    
    today = date.today()
    todayDate = today.strftime("%B %d, %Y")
    todayonlyDate = int(today.strftime("%d"))

    if vaccineShotsToday == vaccineShotsYest:
        return "Same Data"

    diff = abs(round(((float(vaccineShotsToday)-vaccineShotsYest)/vaccineShotsYest)*100,2))

    dateToPrint = todayDate

    tweet = dateToPrint + "\n\n"
    if vaccineShotsToday > vaccineShotsYest:
        emoj = "⬆"
    else:
        emoj = "⬇"

    if IfValid(prevDate,todayonlyDate):
        tweet += "Vaccine Shots Given: " + str(vaccineShotsToday) + " (" + str(diff) + "% " + emoj+ " from yesterday)\n\n"
    else:
        tweet += "Vaccine Shots Given: " + str(vaccineShotsToday) + "\n\n"

    ############

    tweet += "Percentage of Indians who have received a shot: \n"    

    percentageOfSingleDosed = round(peopleSingleDosed/indiaPopulation,4)

    to_fill = int(percentageOfSingleDosed*15)
    to_empty = 15 - to_fill

    for i in range(to_fill):
        tweet += fill
    
    for j in range(to_empty):
        tweet += empty
    
    tweet += " " + str(percentageOfSingleDosed*100) + "%\n\n"

##############
    tweet += "Percentage of Indians who have received both shots: \n"    

    percentageOfFullyVaccinated = round(peopleFullyVaccinated/indiaPopulation,4)

    to_fill = int(percentageOfFullyVaccinated*15)
    to_empty = 15 - to_fill

    for i in range(to_fill):
        tweet += fill
    
    for j in range(to_empty):
        tweet += empty
    
    tweet += " " + str(percentageOfFullyVaccinated*100) + "%"


    with open('last.txt', 'w') as file:
        file.write(str(vaccineShotsToday) + "," + str(todayonlyDate))

    return tweet

def IfValid(prevDate,todayDate):
    if prevDate+1==todayDate:
        return True
    
    return False