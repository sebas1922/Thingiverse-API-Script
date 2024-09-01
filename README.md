This script is designed to facilitate the process of searching thingiverse (a website used to find 3D models for 3D printing purposes) by using the
websites API.

USAGE:
The user can specifiy a search term for models they want to download as well as the amount of models being downloaded. The script creates a file for 
each model containing a picture, description, and all neccesary .stl files needed for the 3D printing software. 


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




