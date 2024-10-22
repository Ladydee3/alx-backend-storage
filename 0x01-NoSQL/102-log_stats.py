#!/usr/bin/env python3
""" MongoDB Nginx Log Stats Script """
from pymongo import MongoClient

def log_stats():
    """ Function that prints stats from the logs in the MongoDB """
    client = MongoClient('mongodb://localhost:27017/')
    db = client.logs
    collection = db.nginx

    # Count total number of logs
    log_count = collection.count_documents({})
    print(f"{log_count} logs")

    # Count logs for each HTTP method
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        method_count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {method_count}")

    # Count logs with status check (path "/status")
    status_check_count = collection.count_documents({"path": "/status"})
    print(f"{status_check_count} status check")

    # Aggregate and count top 10 most frequent IPs
    print("IPs:")
    top_ips = collection.aggregate([
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ])
    for ip in top_ips:
        print(f"\t{ip['_id']}: {ip['count']}")

if __name__ == "__main__":
    log_stats()

