from metaflow import FlowSpec, step
from ingestandstore.ingest import ingest_data
from etlprocess.extract import extract_data
from etlprocess.transform import transform_data
from etlprocess.load import load_data
import psycopg2
import time

class LinearFlow(FlowSpec):
    @step
    def start(self):
        ingest_data()
        self.next(self.extract)

    @step
    def extract(self):
        extract_data()
        self.next(self.transform)

    @step
    def transform(self):
        transform_data()
        self.next(self.load)


    @step
    def load(self):
        load_data()
        self.next(self.end)

    @step
    def end(self):
       print('ETL workflow completed!!!')

if __name__ == '__main__':
    LinearFlow()
