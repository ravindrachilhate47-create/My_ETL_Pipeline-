import pandas as pd
import logging 
from pathlib import Path

logging.basicConfig(level=logging.INFO)

input_file= Path(r"C:\Users\Ravindra Chilhate\OneDrive\Desktop\Book1.csv")
output_file = Path(r"C:\Users\Ravindra Chilhate\OneDrive\Desktop\keggel projects\clean_flipkart.csv")

class flipkart_sales:
    def __init__(self,input_file,output_file):
        self.input_file=input_file
        self.output_file=output_file

    #Extract 
    def extract(self):
        logging.info("Reding a CSV file.....")
        df=pd.read_csv(self.input_file)
        print(df.info())
        return df

    # Transform 
    def transform(seld,df):
        logging.info("Transform CSV file ......")

        # change date and time 
        df['date']=pd.to_datetime(df['date'],errors="coerce",dayfirst=True)

        # match type 
        df['Match_type']=df['match_type'].str.strip()

        # event name 
        df['event_name']=df['event_name'].str.strip()

        return df 

    #  Load
    def load(self, df):
     logging.info("Saving cleaned data...")
     self.output_file.parent.mkdir(parents=True, exist_ok=True)
     df.to_csv(self.output_file, index=False)

   # run pipeline
    def run(self):
        try:
            df=self.extract()
            df=self.transform(df)
            self.load(df)

            logging.info("Pipeline completed successfully!")

        except Exception as e:
                    logging.error(f"Pipeline failed: {e}")


pipeline= flipkart_sales(
     input_file,
     output_file
)

pipeline.run()
                    
     
        