#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 09:59:16 2018

@author: abhilashsk
"""

from pymongo import MongoClient

def connect_to_client():
    client=MongoClient("localhost",27017)
    connection=client.test.HousePrice2
    return connection

def create_entry(connection,data):
    connection.insert(data)
    print("Record was inserted successfully")
    
def fetch_data(connection,row_num):
    data=connection.find().skip(row_num-1).limit(1)
    print("Record was read successfully")
    return [x for x in data]

def update_entry(connection,data,entry_id):
    connection.update({'_id':entry_id},data)
    print("Record was updated successfully")
    
def delete_entry(connection,row_num):
    connection.remove({'_id':row_num})
    print("Record was deleted successfully")