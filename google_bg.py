"""Module for insert into google bigquey data"""
# Place the json keys into a different directory

from google.cloud import bigquery


def build_clinet():
    """Build client from service account"""
    path_key = "/home/lmdz_366/Documents/gcp_key.json"
    cliente = bigquery.Client.from_service_account_json(path_key)


if __name__ == "__main__":
    build_clinet()
