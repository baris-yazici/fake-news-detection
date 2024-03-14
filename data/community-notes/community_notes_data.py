# Filter the helpful and not helpful notes from X's community notes data
## The data we downloaded includes contributions up until 1:32 AM · Mar 10, 2024
### first download the data from this link: https://twitter.com/i/communitynotes/download-data

import pandas as pd

# Read the notes file
notes = pd.read_csv('/path/notes-00000.tsv', delimiter='\t')

# Initialize an empty list to store helpful note IDs
all_helpful_note_ids = []

# Loop through ratings files and aggregate helpful note IDs
for i in range(8):
    ratings = pd.read_csv(f'/Users/barisyazici/Desktop/Community Notes Data/ratings-0000{i}.tsv', delimiter='\t')
    helpful_note_ids = ratings.loc[ratings["helpfulnessLevel"]=="HELPFUL", "noteId"].unique()
    all_helpful_note_ids.extend(helpful_note_ids)

# Convert the list to a set to remove duplicates, then back to a list
all_helpful_note_ids = list(set(all_helpful_note_ids))

# Export the list of note ids
all_helpful_note_ids = pd.DataFrame(all_helpful_note_ids)
all_helpful_note_ids.columns = ["noteId"]
#all_helpful_note_ids.to_csv("/path/helpful_note_ids.csv")

# Filter and export helpful notes
helpful_notes = notes[notes["noteId"].isin(all_helpful_note_ids["noteId"])]
#helpful_notes.to_csv("/path/helpful_notes.csv")

# Initialize an empty list to store not helpful note IDs
all_not_helpful_note_ids = []

# Loop through ratings files and aggregate not helpful note IDs
for i in range(8):
    ratings = pd.read_csv(f'/Users/barisyazici/Desktop/Community Notes Data/ratings-0000{i}.tsv', delimiter='\t')
    not_helpful_note_ids = ratings.loc[ratings["helpfulnessLevel"]=="NOT_HELPFUL", "noteId"].unique()
    all_not_helpful_note_ids.extend(not_helpful_note_ids)

# Convert the list to a set to remove duplicates, then back to a list
all_not_helpful_note_ids = list(set(all_not_helpful_note_ids))

# Export the list of note ids
all_not_helpful_note_ids = pd.DataFrame(all_helpful_note_ids)
all_not_helpful_note_ids.columns = ["noteId"]
#all_not_helpful_note_ids.to_csv("/path/not_helpful_note_ids.csv")

# Filter and export not helpful notes
not_helpful_notes = notes[notes["noteId"].isin(all_not_helpful_note_ids["noteId"])]
#not_helpful_notes.to_csv("/path/not_helpful_notes.csv")
