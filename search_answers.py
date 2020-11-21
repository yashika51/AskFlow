"""
Accept the error from another function.
Functions:
- Get questions based on the error_message
- Get top 5 answers from the site based on the question ids
"""

import requests
from dotenv import load_dotenv
load_dotenv()
import os
import urllib.request
import json
import gzip
from io import StringIO
from bs4 import BeautifulSoup


class ask():

    def __init__(self,error):
        self.key=os.environ.get("key")
        self.error_message=error
    
    def get_question_id(self):
        """
        returns top 5 question id's
    
        """

        url=f'https://api.stackexchange.com/2.2/search/advanced?site=stackoverflow.com&q={self.error_message}' 
        jData=requests.get(url)
        data=jData.json()
        question_ids=[]
        for i in data['items']:
            ques_id=i.get('question_id')
            question_ids.append(str(ques_id))
        #query accepts ids only delimited by semicolon
        return ';'.join(question_ids)


        
    def get_answer(self,count=5):
        """
        returns answers based on question id's given by get_function_id()
        """
        ids=self.get_question_id()

        query=f'https://api.stackexchange.com/2.2/questions/{ids}/answers?site=stackoverflow&filter=!9_bDE(fI5'

        jData=requests.get(query)
        data=jData.json()
        answers=[]
        c=0
        for i in data['items']:
            ans=i.get('body')
            soup = BeautifulSoup(ans)
            answers.append(soup.get_text().replace('\n','\n\n'))
            c+=1
            if c==count:
                break
        return answers