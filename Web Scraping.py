import requests
from bs4 import BeautifulSoup
import pandas

oyo_url = "https://www.oyorooms.com/hotels-in-bangalore/"
page_num_max=int(input("Enter page number: "))
scrapped_info_list = []

for page_num in range(1,page_num_max):
    req= requests.get(oyo_url + str(page_num))
    content = req.content

    soup= BeautifulSoup(content, "html.parser")

    all_hotels = soup.find_all("div", {"class": "hotelCardListing"})

    for hotel in all_hotels:
        hotel_dict={}
        hotel_dict["name"] = hotel.find("h3", {"class": "listingHotelDescription__hotelName"}).text
        hotel_dict["address"] = hotel.find("span", {"itemprop": "StreetAddress"}).text
        hotel_dict["price"] = hotel.find("span", {"class": "listingPrice__finalprice"}).text
        try:
            hotel_dict["rating"] = hotel.find("h3", {"span": "hotelRating_ratingSummary"}).text
        except AttributeError:
            hotel_dict["rating"]=None
    parent_amenities_element=hotel.find("div",{"class":"amenitywrapper_amenity"})
    amenities_list=[]
    for amenity in parent_amenities_element.findall("div",{"class":"amenitywrapper_amenity"}):
        amenity_list.append(amenity_find("span",{"class": "d_body_sm"}))
    hotel_dict["amenities"]=','.join(amenities_list[:-1])
    scrapped_info_list.append(hotel_dict)

dataFrame=pandas.DataFrame(scrapped_info_list)
dataFrame.to_csv("oyo.csv")
connecr.get_hotel_info(args.dbname)
