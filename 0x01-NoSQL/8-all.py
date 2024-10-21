#!/usr/bin/env python3
"""
Function that lists all documents in a collection
"""
def list_all(mongo_collection):
    """
    Lists all documents in a collection
    If no document is found, returns an empty list
    """
    return list(mongo_collection.find())  # Using the find() method to fetch all documents

