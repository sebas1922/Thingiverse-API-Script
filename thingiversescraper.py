import requests
import argparse
import json
import os
import shutil
import sys
from dotenv import load_dotenv

"""
TODO
#DONE trunkcate search result to desired param
#DONE find and filter stl file > put into text file for now
figure out argparse for arguments
Sort out stl files and put into folder
"""


def parse_arguments():
    parser = argparse.ArgumentParser(prog='Thiniverse Scraper', 
    description='Search functionality: Get a certain amount of stl files from a given search put in a folder with both the stl file and information (image of object, description, etc) on the object itself')

    parser.add_argument("-s", "--search", type=str, help="Search term used to return things that otherwise would pop up when searching on Thingiverse")
    parser.add_argument("-n", "--number", type=int, choices=range(1, 30), default=1, help="Used to specify the number of things being downloaded.")
    parser.add_argument("-r", "--remove", action="store_true", help="Clears the things folder after confirmation.")

    return parser.parse_args()


#defines the payload and modifies the url to search by search term
def search_request(url, token, search_term, items=10):
    request_payload = {"page":1, "per_page":items, "access_token":token}
    new_url = url + "search/" + search_term
    return requests.get(new_url, params=request_payload).json()


#gets the file links associated with thing_ID that contain an stl file
def get_files(url, thing_ID, token):
    new_url = url + "things/" + thing_ID + "/files"
    files = requests.get(new_url, params={"access_token" : token}).json()

    #get all downloadable stl files and put in list
    file_links = []
    for f in files:
        if f["name"].endswith(".stl"):
            file_links.append({"name" : f["name"], "link" : f["download_url"]})

    return file_links


#gets the information of the thing of associated ID such as name, image, license and description, and file link downloads
def get_thing_info(url, thing_ID, token):
    new_url = url + "things/" + thing_ID
    data = requests.get(new_url, params={"access_token" : token}).json()

    thing_info = {"name": data["name"], "id" : data["id"], "thumbnail_link":data["thumbnail"], "description": data["description"], "license" : data["license"], "files": get_files(url, thing_ID, token)}

    return thing_info


def main():  
    #Token authenticates this script to make requests to API
    load_dotenv()
    APP_TOKEN = os.getenv("APP_TOKEN")
    URL = "https://api.thingiverse.com/"
    main_dir = os.getcwd()

    args = parse_arguments()

    #Check to see if user wants to delete files from things folder
    if args.remove:
        answer = input("About to remove all content of things folder. Continue? [Y/N]").strip().lower()
        if answer in ("y", "yes"):
            print("Removing files...")
            shutil.rmtree(main_dir+"/things")
            os.mkdir("things")
            sys.exit("Done.")

    #Check to see if things folder is present
    if("things" not in os.listdir(main_dir)):
        os.mkdir("things")
        print("Creating directory 'things'...")

    
    #make a request to API to search for a specified amount of things based on a search term
    try:
        data = search_request(URL, APP_TOKEN, args.search, args.number)    
    except TypeError:
        sys.exit("Please specify a search term")
    things = data["hits"]

    #find all thing IDS based on the data returned in the request
    thing_ID = []
    for thing in things:
        link = thing["url"]
        thing_ID.append(link[link.rfind("/")+1:])


    #assemble what will be dumped into things folder
    thing_info = []

    for Id in thing_ID:
        thing_info.append(get_thing_info(URL, Id, APP_TOKEN))

    
    """
    Create a folder for each thing and add a file folder with the the STL files as well as an image and description
    """

    for thing in thing_info:
        os.chdir(main_dir+"/things")
        try:
            os.makedirs(thing["name"]+"/files", exist_ok=True)
        except FileExistsError:
            print("File already exists")

        os.chdir(os.getcwd()+f"/{thing["name"]}")

        with open("Thumbnail", "wb") as f:
            data = requests.get(thing["thumbnail_link"], params={"access_token" : APP_TOKEN})
            f.write(data.content)

        with open("README.md", "w") as f:
            f.write(f"{thing["name"]}\n\n ID: {thing["id"]} \n\n {thing["id"]}{thing["description"]}")
        
        os.chdir(os.getcwd()+"/files")
        
        stls = thing["files"]

        _ = 1
        print(f"Downloading files for {thing["name"]}")
        for stl in stls:
            with open(stl["name"], "wb") as f:
                print(f"Downloading file {_} of {len(stls)}...", end="\r")
                data = requests.get(stl["link"], params={"access_token" : APP_TOKEN})
                f.write(data.content)
                _ += 1
        print("")
        
    
    print(f"Downloaded {len(thing_info)} things.")
        
        
        
        
                


        
    

    



    


if __name__ == "__main__":
    main()
