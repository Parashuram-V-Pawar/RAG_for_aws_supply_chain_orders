import pandas as pd

class DataProcesser:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None

    def load_data(self):
        self.df = pd.read_csv(self.file_path)
        print("Data loaded successfully.")
            

    def clean_data(self):
        df = self.df

        df['region'] = df['region'].fillna("Unknown")

        df['delivery_time_days'] = df['delivery_time_days'].fillna(df['delivery_time_days'].median())
        df['delivery_time_days'] = df['delivery_time_days'].round().astype(int)

        df['order_date'] = pd.to_datetime(df['order_date'], errors = 'coerce')
        df['delivery_date'] = pd.to_datetime(df['delivery_date'], errors = 'coerce')

        df = df.drop_duplicates(subset = 'order_id')
        
        self.df = df
        return self.df
    
# d = DataProcesser('data/aws_supply_chain_orders_raw.csv')
# d.load_data()
# cleaned_df = d.clean_data()
# print(cleaned_df.head())