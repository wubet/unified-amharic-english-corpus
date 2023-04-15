# Unified-Amharic-English-Corpus

This corpus combine two smaller Amharic-English corpora that are publicly available. One of the corpora is available in GitHub which is collected from different sources like Bible, legal documents, and news[^1].  The other corpus is the one used by Gezmu et.al. which is a public benchmark dataset of Amharic-English parallel corpus[^2]. The corpus consists of three dataset:
1. Training data: This is the largest subset of the dataset and is used to train the machine learning algorithm. The algorithm learns patterns in the data and adjusts its parameters to minimize the error between the predicted output and the actual output.

2. Validation data: This subset is used to validate the performance of the algorithm during training. It is used to tune the hyperparameters of the algorithm to prevent overfitting. The validation set is usually taken from the training set and is not used for training the algorithm.

3. Test data: This subset is used to test the performance of the algorithm after training. The test data is completely independent of the training and validation sets, and the algorithm has never seen this data before. The test data provides an unbiased estimate of the algorithm's performance.

The main difference between the three subsets is their purpose in the training process. The training data is used to teach the algorithm how to recognize patterns in the data. The validation data is used to fine-tune the hyperparameters of the algorithm to prevent overfitting. The test data is used to test the performance of the algorithm on unseen data.

While combining the two corpora multiple redundant sentences are found out that indicate they were compiled from the same sources. Redundant sentences are removed as much as possible. There are still a few redundant sentences that need to be removed in the future. In the Amharic sentences there are spelling errors, inconsistency in translation and lack of standards while translating.

[^1]: [Amharic English Machine Translation Corpus] (https://github.com/adtsegaye/Amharic-English-Machine-Translation-Corpus)

[^2]: [Data and Knowledge Engineering Group Amharic-English Parallel Corpus (ovgu.de)] (https://www.findke.ovgu.de/findke/en/Research/Data+Sets/Amharic_English+Parallel+Corpus-p-1144.html)