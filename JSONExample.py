import json

print("Welcome to history data analyzer.")
# inputFile = input("Enter the file to open:\n")
inputFile = "helsinki_stats.json"
print("File read successfully, ready for analysis.")
while (True):
    print("What would you like to do?")
    print("1) Calculate total amount of inhabitants by gender")
    print("2) Calculate inhabitants on a given year")
    print("3) Calculate inhabitants after given year by age cohort")
    print("0) Stop\n")
    selection = int(input("Make your choice:\n"))
    if selection == 0:
        print("Bye!")
        break
    if selection == 1:
        gender = int(input("Select your gender (0=male, 1=female):\n"))
        jsonFile = open(inputFile, 'r')
        data = json.loads(jsonFile.read())
        total = 0
        for i in range(len(data['data'])):
            if (int(data["data"][i]["key"][1]) == gender):
                total = total + int(data["data"][i]["values"][0])
        if gender == 0:
            print("There were a total of " + str(total) + " males in Helsinki between years 1900-1961")
        if gender == 1:
            print("There were a total of " + str(total) + " females in Helsinki between years 1900-1961")
        jsonFile.close()
    if selection == 2:
        year = int(input("Please enter year for search (1900-1961):\n"))
        jsonFile = open(inputFile, 'r')
        data = json.loads(jsonFile.read())
        total = 0
        for i in range(len(data['data'])):
            if (int(data["data"][i]["key"][0]) == year):
                total = total + int(data["data"][i]["values"][0])
        print("There were a total of "+str(total)+" inhabitants in Helsinki on year "+str(year))
        jsonFile.close()
    if selection == 3:
        year = int(input("Please enter year for search (1900-1961):\n"))
        cohort = int(input("Select age cohort (4=20-24, 5=25-29, 6=30-34, 7=35-39):\n"))
        jsonFile = open(inputFile, 'r')
        data = json.loads(jsonFile.read())
        total = 0
        for i in range(len(data['data'])):
            if int(data["data"][i]["key"][2]) == cohort:
                if int(data["data"][i]["key"][0]) >= year:
                    total = total + int(data["data"][i]["values"][0])
        print("There were a total of "+str(total)+" inhabitants  of ages 30-34 between the years 1950 and 1961")
        jsonFile.close()
