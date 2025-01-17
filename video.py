from constants import *
import requests
from pprint import pprint

class Video:
    def __init__(self, url=BACKUP_URL):
        self.url = url

    def create_video(self, title, release_date, total_inventory):
        query_params = {"title": title,
                        "release_date": release_date,
                        "total_inventory": total_inventory}
        response = requests.post(self.url+"/videos",json=query_params)
        return response
 
    def list_videos(self):
        response = requests.get(self.url+"/videos")
        return response.json()

    def get_video(self, id):
        response = requests.get(self.url+f"/videos/{id}")
        if response.status_code == 200:
            return response.json()
        return None
 
    def update_video(self, video, title, release_date, total_inventory):
        if not title:  # title = title or video["title"]
            title = video["title"]
        if not release_date:
            release_date = video["release_date"]
        if not total_inventory:
            total_inventory = video["total_inventory"]

        query_params = {"title": title,
                        "release_date": release_date,
                        "total_inventory": total_inventory}
        response = requests.put(self.url+f"/videos/{video['id']}",
            json=query_params)
        return response

    def delete_video(self, id):
        response = requests.delete(self.url+f"/videos/{id}")
        return response.json()

        
