import pandas as pd
class BlogPost:
    def __init__(self, entry):
        self._id = entry['id']
        self._title = entry['title']
        self._link = entry['link']
        self._content = entry['content'][0]['value']
        self._published = entry['published']
        self._medium = False
        self._instagram = False
    
    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title

    @property
    def link(self):
        return self._link

    @property
    def content(self):
        return self._content
    
    @property
    def published(self):
        return self._published

    @property
    def medium(self):
        return self._medium
    
    @property
    def instagram(self):
        return self._instagram
    
    @property
    def data(self):
        data = [self._id,self._title,self._link, self._content, self._published, self._medium, self._instagram]
        df = pd.DataFrame([data], columns=['id','title','link','content','published','medium','instagram'])
        return df

    @medium.setter
    def medium(self, n):
        self._medium = n
    
    @instagram.setter
    def instagram(self, n):
        self._instagram = n