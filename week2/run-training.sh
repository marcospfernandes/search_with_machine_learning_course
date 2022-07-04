#!/bin/bash
# LEVEL 1
echo 'Running level 1...'
echo 'Creating Training Data and Filtering Categories...'
python week2/createContentTrainingData.py --output /workspace/datasets/fasttext/labeled_products.txt --min_products 500
echo 'Shuffling the Data...'
shuf /workspace/datasets/fasttext/labeled_products.txt > /workspace/datasets/fasttext/shuffled_labeled_products.txt
echo 'Generating Test Data...'
tail -n10000 /workspace/datasets/fasttext/shuffled_labeled_products.txt > /workspace/datasets/fasttext/training_data.txt
echo 'Generating train Data...'
head -n10000 /workspace/datasets/fasttext/shuffled_labeled_products.txt > /workspace/datasets/fasttext/test_data.txt
~/fastText-0.9.2/fasttext supervised -input /workspace/datasets/fasttext/training_data.txt -output /workspace/datasets/fasttext/product_classifier -wordNgrams 2 -lr 1 -epoch 25
~/fastText-0.9.2/fasttext test /workspace/datasets/fasttext/product_classifier.bin /workspace/datasets/fasttext/test_data.txt 1


# LEVEL 2
echo 'Running level 2...'
cut -d$'\t' -f2- /workspace/datasets/fasttext/shuffled_labeled_products.txt > /workspace/datasets/fasttext/normalized_titles.txt
~/fastText-0.9.2/fasttext skipgram -input /workspace/datasets/fasttext/normalized_titles.txt -output /workspace/datasets/fasttext/title_model -minCount 20 -epoch 25
~/fastText-0.9.2/fasttext nn /workspace/datasets/fasttext/title_model.bin