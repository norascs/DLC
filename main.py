import numpy as np
import itertools as it
import pandas as pd


## Reading in stimuli from a CSV ----

# SWOW data
swow_data = pd.read_csv("../data/SWOW-EN.R100.csv.zip")

print(swow_data)

# Pull out the columns with stimuli



cues_and_responses = swow_data[["cue","R1","R2","R3"]]

swow_words = cues_and_responses.values.ravel()

## Normally you would want to filter garbage responses, and do other checks, but we'll be subsetting to the words in HistWords, which have already been filtered.

swow_words = pd.unique(swow_words)


# Castro data
castro_data = pd.read_csv("../data/castro_cat_norms.csv")

print(castro_data) # Will be similar to the above process, but there is only 1 response to each cue.

cues_and_responses = castro_data[["cue","response"]]

castro_words = cues_and_responses.values.ravel()

castro_words = pd.unique(castro_words)


# Then you'll need to combine them together

full_set = np.concatenate((swow_words, castro_words)) ## uncomment once above is changed
full_df = pd.DataFrame({"stimuli":full_set})  ## uncomment once above is changed

# Filter to only those in Histwords
histwords_set = np.concatenate((swow_words, castro_words))
histwords_df = pd.DataFrame({"stimuli":histwords_set})
histwords_vocab = pd.read_csv("../data/histwords_vocab.csv")

hw_words = histwords_vocab["word"].values

full_df = full_df[full_df.isin(hw_words)] ## uncomment once above is changed


## And save to a csv
full_df.to_csv("../data/full_set.csv")
full_df.to_csv("stimuli_to_check.csv", index = False) ## uncomment once above is changed
