from lib.transformer import Transformer

transformer = Transformer()
transformer.transform_content_hostname(
    "./data/Degreed_Example_Completions.csv",
    "./data/Degreed_Transformed_Completions.csv"
)
