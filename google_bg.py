"""Module for insert into google bigquey data"""
# Place the json keys into a different directory

from google.cloud import bigquery
import pandas as pd


def build_clinet():
    """Build client from service account"""
    path_key = "/home/lmdz_366/Documents/gcp_key.json"
    client = bigquery.Client.from_service_account_json(path_key)

    return client


def test_query(client):

    table_id = "chrome-parity-419400.temperature_valle_azul.data_2024_1"
    bg_query = "SELECT * FROM `chrome-parity-419400.lpm366.table_1` LIMIT 100"
    result = client.query(bg_query)
    df = result.to_dataframe()
    print(df.head())


if __name__ == "__main__":
    client = build_clinet()
    test_query(client)
