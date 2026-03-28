import time
import datetime
from functions import *

print("Starting data pipeline at ", datetime.datetime.now().strftime('%y-%m-%d %H:%M:%S'))

print("--------------------------------------")

# step 1 : extract video IDs
t0 = time.time()
getVideoIDs()
t1 = time.time()
print("Step 1 : Done")
print("----> Video IDs downloaded in", str(t1-t0), "seconds", "\n")

# step 2 : extract transcripts for videos
t0 = time.time()
getVideoTranscripts()
t1 = time.time()
print("Step 2 : Done")
print("----> Transcripts downloaded in", str(t1-t0), "seconds", "\n")

# step 3 : Transform data
to = time.time()
transformData()
t1 = time.time()
print("Step 3 : Done")
print("----> Data Transformed in", str(t1-t0), "seconds", "\n")

# step 4 : Generate text embeddings
t0 = time.time()
createTextEmbeddings()
t1 = time.time()
print("Step 4 : Done")
print("----> Embeddings generated in", str(t1-t0), "seconds", "\n")

