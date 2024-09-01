This script is designed to facilitate the process of searching thingiverse (a website used to find 3D models for 3D printing purposes) by using the
websites API.

USAGE:
The user can specifiy a search term for models they want to download as well as the amount of models being downloaded. The script creates a file for 
each model containing a picture, description, and all neccesary .stl files needed for the 3D printing software. 

For example, if the user wants to download the first 10 thigns that pop up under the search 'batman', the user can do the following:

    python thingiversescraper.py -s batman -n 10

The script will download the thumbnail and description of each thing as well as the .stl files needed for the slicer, facilitating the process of searching for  things through the website itself.


## Setup Instructions

1. **Clone the Repository**

    ```bash
    git clone https://github.com/yourusername/your-repository.git
    
    cd your-repository

2. **Install Dependancies**    
    pip install -r requirements.txt

3. **Create your own 'env' file**
    Copy the example .env file to create your own .env file:
    cp .env.example .env

4. **Edit the '.env' file**
    Copy the example .env file to create your own .env file:
    nano .env

5. **Run the application**

    python thingiversescraper.py -s your-search-term -n number-of-models-wanted


## App token instructions:
 
Go to https://www.thingiverse.com/apps/create and log in to Thingiverse.com
Go through the process of getting app token

1. SELECT A PLATFORM:
    Select Desktop App

2. BASIC INFORMATION:
    Fill in each field (doesn't really matter what you put)

3. API INFORMATION:
    Once authenticated and redirected, copy the App Token field

4. Add to APP_TOKEN and script is ready to be run






