"""
Accept the error from another function.
Functions:
- Get questions based on the error_message
- Get top 5 answers from the site based on the question ids
"""

from dotenv import load_dotenv
load_dotenv()
import os
import requests
import urllib.request
import json
from bs4 import BeautifulSoup
from get_error import main


class ask():

    def __init__(self,error_list):
        self.key=os.environ.get('key')
        self.client_id=os.environ.get('client_id')
        self.answer_filter=os.environ.get('filter')
        #error_message is a list of errors
        self.error_list=error_list
        self.error_message=' '.join(error_list)
    
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

        query=f'https://api.stackexchange.com/2.2/questions/{ids}/answers?client_id={self.client_id}&site=stackoverflow&key={self.key}&filter={self.answer_filter}'

        jData=requests.get(query)
        data=jData.json()
        answers=[]
        c=0
       
        for i in data['items']:   
                ans=i.get('body')
                soup = BeautifulSoup(ans,features="html.parser")
                answers.append(soup.get_text().replace('\n',' '))
                print(soup.get_text().replace('\n',' '))
                c+=1
                if c==count:
                    break
        
        return answers

