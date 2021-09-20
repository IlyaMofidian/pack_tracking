import json
import math
import sys


class Crawler:

    origin= (0, 0)
    
    def __init__(self, order, threshold= 200):
        self.order = order
        self.threshold = threshold
        # self.origin = (0, 0)


    def test(self):
        print("This is the order {} scraping: ".format(self.order + 1))
        location, arrTime = Crawler.scrape(self)
        print("Location: ", location)
        print("arrival_time: ", arrTime)
        print("==================================================")



    # An equivalent of scraping the website        
    def scrape(self):  

        #Could move to the top
        with open('crawler_result.json', 'r') as f:
            data = json.load(f)['data'][self.order]
            # print("data is read")

        lat = data['coordinates']['latitude']
        lon = data['coordinates']['longitude']
        arrTime = data['arrival_time']
        return (lat, lon), arrTime

    
           
    # Calculates the distance between two points of a sphere  
    def haversine(self, origin, destination):
        self.origin = origin
        self.destination = destination
        lat1, lon1 = origin
        lat2, lon2 = destination
        radius = 6371  # radius of the Earth (in km)
        dlat = math.radians(lat2 - lat1)
        dlon = math.radians(lon2 - lon1)
        a = (math.sin(dlat / 2) * math.sin(dlat / 2) + 
             math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) * math.sin(dlon / 2))
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        havDis = radius * c
        return havDis
    
    
    #returns a boolean value to determine the package is moved or not
    def geoChanged(self):
        # print(Crawler.origin)
        dest, _ = Crawler.scrape(self)

        dist = Crawler.haversine(self, Crawler.origin, dest) 

        if dist > self.threshold:
            print(dist)
            print(Crawler.origin)
            print(dest)
            print("========================================")

            Crawler.origin = dest
            return True


    
    def notificationMessage(self, name= 'Watson', flight= 'Emirates 215'):
        self.name = name
        self.flight = flight
        # self.time = time
        # self.location = location
        
        if self.order == 1:
            print('Hi dear {}:\nLast status of airplane {}:\nTime of Arrival: {}\nCurrent Location: {}'
                  .format(name, flight, time, location))
        else:
            if geoChanged:
                print("Hi dear {}\nNew update of airplane {} status:\nTime of Arrival: {} (2 hours delay)\nLocation: changed from {} to {}"
                      .format(name, flight, time, location))

