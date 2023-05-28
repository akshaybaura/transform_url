import polars as pl
from urllib.parse import urlparse
import tldextract
import re

class Transformer:
    @staticmethod
    def get_hostname_from_url(url):
        """This method parses the url and returns the hostname"""
        pattern = r'^https?://'
        if re.match(pattern, url):
            parsed_url = urlparse(url)
            return parsed_url.hostname
        else:
            return 'NA'

    @staticmethod
    def get_domain_from_url(url):
        """This method parses the url and returns the domain"""
        pattern = r'^https?://'
        if re.match(pattern, url):
            extracted = tldextract.extract(url)
            return f"{extracted.domain}.{extracted.suffix}"
        else:
            return 'NA'

    def transform_content_hostname(self, input_file, output_file):
        print(f"Transforming {input_file} to {output_file}")
        # reading the file
        df = pl.read_csv(input_file)
        # cleaning data for nulls and uniqueness
        print("Transforming data...")
        df = df.filter(~pl.col('ContentUrl').is_null() & ~pl.col('UserId').is_null()).unique()
        # adding transformed columns
        df = df.with_columns([pl.col('ContentUrl').apply(self.get_hostname_from_url).alias('HostName'),pl.col('ContentUrl').apply(self.get_domain_from_url).alias('Domain')])
        # saving the file
        print("Saving output file...")
        df.write_csv(output_file)
    

