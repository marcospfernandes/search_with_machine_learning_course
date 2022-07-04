import argparse
import os
import random
<<<<<<< HEAD
import re
import pandas
from nltk.stem.snowball import EnglishStemmer
=======
>>>>>>> parent of e213dcf (Level 1 + Level 2)
import xml.etree.ElementTree as ET
from pathlib import Path

def transform_name(product_name):
<<<<<<< HEAD
    # Converting product name to lower
    product_name = product_name.lower()
    # Removing non alpha characteres
    product_name=re.sub(r'[\W_]+', '', product_name)
    # Merging whitespaces 
    product_name = re.sub(r"(?a:\s+)"," ", product_name) 
    product_name = product_name.strip()
    return " ".join(map(stemmer.stem, product_name.split(" ")))
=======
    # IMPLEMENT
    return product_name
>>>>>>> parent of e213dcf (Level 1 + Level 2)

# Directory for product data
directory = r'/workspace/datasets/product_data/products/'

parser = argparse.ArgumentParser(description='Process some integers.')
general = parser.add_argument_group("general")
general.add_argument("--input", default=directory,  help="The directory containing product data")
general.add_argument("--output", default="/workspace/datasets/fasttext/output.fasttext", help="the file to output to")
general.add_argument("--label", default="id", help="id is default and needed for downsteam use, but name is helpful for debugging")

# Consuming all of the product data, even excluding music and movies,
# takes a few minutes. We can speed that up by taking a representative
# random sample.
general.add_argument("--sample_rate", default=1.0, type=float, help="The rate at which to sample input (default is 1.0)")

# IMPLEMENT: Setting min_products removes infrequent categories and makes the classifier's task easier.
general.add_argument("--min_products", default=0, type=int, help="The minimum number of products per category (default is 0).")

args = parser.parse_args()
output_file = args.output
path = Path(output_file)
output_dir = path.parent
if os.path.isdir(output_dir) == False:
        os.mkdir(output_dir)

if args.input:
    directory = args.input
# IMPLEMENT:  Track the number of items in each category and only output if above the min
min_products = args.min_products
sample_rate = args.sample_rate
names_as_labels = False
if args.label == 'name':
    names_as_labels = True

print("Writing results to %s" % output_file)
with open(output_file, 'w') as output:
    for filename in os.listdir(directory):
        if filename.endswith(".xml"):
            print("Processing %s" % filename)
            f = os.path.join(directory, filename)
            tree = ET.parse(f)
            root = tree.getroot()
            for child in root:
                if random.random() > sample_rate:
                    continue
                # Check to make sure category name is valid and not in music or movies
                if (child.find('name') is not None and child.find('name').text is not None and
                    child.find('categoryPath') is not None and len(child.find('categoryPath')) > 0 and
                    child.find('categoryPath')[len(child.find('categoryPath')) - 1][0].text is not None and
                    child.find('categoryPath')[0][0].text == 'cat00000' and
                    child.find('categoryPath')[1][0].text != 'abcat0600000'):
                      # Choose last element in categoryPath as the leaf categoryId or name
                      if names_as_labels:
                          cat = child.find('categoryPath')[len(child.find('categoryPath')) - 1][1].text.replace(' ', '_')
                      else:
                          cat = child.find('categoryPath')[len(child.find('categoryPath')) - 1][0].text
                      # Replace newline chars with spaces so fastText doesn't complain
                      name = child.find('name').text.replace('\n', ' ')
                      output.write("__label__%s %s\n" % (cat, transform_name(name)))
<<<<<<< HEAD

df = pandas.read_csv('/tmp/labeled_products.txt', names=["str"])
df = df.str.str.split(' ', n=1, expand=True).groupby(0).filter(lambda x: len(x) >= min_products)
df.to_csv(output_file, sep='\t', header=None, index=False) 
=======
>>>>>>> parent of e213dcf (Level 1 + Level 2)
