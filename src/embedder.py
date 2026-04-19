class TextConvertor:
    def __init__(self, df):
        self.df = df

    def raw_to_text(self, row):
        return f"""
            Order_Id : {row['order_id']},
            Warehouse : {row['warehouse']},
            Product: {row['product']},
            Region: {row['region']},
            Order_quantity: {row['order_qty']},
            Order_date: {row['order_date']},
            Delivery_date: {row['delivery_date']},
            Delivery_Time_Days: {row['delivery_time_days']},
            Status: {row['status']}
        """
    
    def convert(self):
        df = self.df
        df['text'] = df.apply(self.raw_to_text, axis = 1)
        return df


        