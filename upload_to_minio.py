from minio import Minio
from minio.error import S3Error
import pandas as pd
import random

client = Minio(
    "127.0.0.1:9000",
    access_key="rKsHnPXWqHSvP2HLhdA3",
    secret_key="7gTR8pJndQPnufpMLI37Xx5Qr0g1HD925g4lMjtR",
    secure=False,
)

found = client.bucket_exists("dinos")
if not found:
    client.make_bucket("dinos")
else:
    print("Bucket 'dinos' already exists")

client.fput_object("dinos", "dinosaurs.csv", "dinosaurs.csv")