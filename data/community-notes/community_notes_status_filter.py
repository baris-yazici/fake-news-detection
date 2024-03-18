# Filter the helpful and not helpful notes from X's community notes data
## The data we downloaded includes contributions up until 1:32 AM · Mar 10, 2024
### first download the data from this link: https://twitter.com/i/communitynotes/download-data

import pandas as pd

# Read the notes and notes status files
notes = pd.read_csv('/path/notes-00000.tsv', delimiter='\t')
notes_status = pd.read_csv('/path/noteStatusHistory-00000.tsv', delimiter='\t')

# Check how many are helpful vs not helpful
notes_status["currentStatus"].value_counts()

# Filter the notes data based on the labels
helpful_note_ids = notes_status.loc[notes_status["currentStatus"] == "CURRENTLY_RATED_HELPFUL", "noteId"].to_list()
not_helpful_note_ids = notes_status.loc[notes_status["currentStatus"] == "CURRENTLY_RATED_NOT_HELPFUL", "noteId"].to_list()
helpful_notes = notes[notes["noteId"].isin(helpful_note_ids)]
not_helpful_notes = notes[notes["noteId"].isin(not_helpful_note_ids)]
