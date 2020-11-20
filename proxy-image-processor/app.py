from observer import Observer
from image_transformer import ImageTransformer


obs = Observer("./images/original",
               ImageTransformer("./images/original", "./images/processed"))

obs.observe()

