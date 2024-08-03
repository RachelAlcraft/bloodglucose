import requests

#https://gist.github.com/bewest/dbe590ab131edfdddd4d988d58c25930

def get_blood_glucose_date_time_length(ns_url, date, time_start, length):     
    #"https://api.nightscout.com/api/v1/entries/last.json"
    api_version = "/api/v1/"
    # api requests
    recent = "/entries"        
    url = f"{ns_url}{api_version}{recent}/sgv.csv?find[dateString][$gte]=2024-07-20&find[dateString][$lte]=2024-07-21&count=50"            
    response = requests.get(url)
    data = response.content.decode("utf-8").split("\n")
    bgs = []
    for row in data:
        #tabbed = row.split("\t")
        #bg = float(tabbed[2]) / 18.01559 #converson to mmol is 18.01559M
        #date_time = tabbed[0].split("T")
        #date = date_time[0]
        #time = date_time[1]
        #arrow = tabbed[3]
        #bgs.append((round(bg,1),date,time, arrow))
        bgs.append(row)

    return bgs
        
  
  