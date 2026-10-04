

#from src.algorithms import (
#    fifo_page_replacement,
#    lru_page_replacement,
#    optimal_page_replacement,
#    mru_page_replacement
#)

#pages = [1, 2, 3, 1, 4, 2, 5, 1, 2, 3]
#frame_count = 3



# FIFO
#fifo_hits, fifo_faults = fifo_page_replacement(pages, frame_count)

# LRU
#lru_hits, lru_faults = lru_page_replacement(pages, frame_count)

#optimal
#optimal_hits, optimal_faults = optimal_page_replacement(pages,frame_count)

# MRU
#mru_hits, mru_faults = mru_page_replacement(pages,frame_count)

#print("Page reference string:", pages)
#print("Number of frames:", frame_count)

#print("\nFIFO")
#print("Hits:", fifo_hits)
#print("Page faults:", fifo_faults)

#print("\nLRU")
#print("Hits:", lru_hits)
#print("Page faults:", lru_faults)

#print("\nOptimal")
#print("Hits:", optimal_hits)
#print("Page faults:", optimal_faults)

#print("\nMRU")
#print("Hits:", mru_hits)
#print("Page faults:", mru_faults)

from src.learned import (
    create_training_data,
    train_eviction_model,
    learned_page_replacement
)




from src.algorithms import (
    fifo_page_replacement,
    lru_page_replacement,
    optimal_page_replacement,
    mru_page_replacement
)
from src.learned import train_eviction_model

from src.workload import generate_workload

training_data = [
    (1, 8, 0),
    (2, 7, 0),
    (3, 6, 0),
    (8, 2, 1),
    (10, 1, 1),
    (12, 1, 1)
]

model = train_eviction_model(training_data)

prediction = model.predict([[10, 1]])

print("\nDecision Tree test prediction:", prediction[0])



# ==========================================
# Generate workload
# ==========================================

workload, phase1, phase2 = generate_workload()


# ==========================================
# Settings
# ==========================================

frame_count = 3


# ==========================================
# Test Phase 1
# ==========================================

fifo_hits_1, fifo_faults_1 = fifo_page_replacement(
    phase1, frame_count
)

lru_hits_1, lru_faults_1 = lru_page_replacement(
    phase1, frame_count
)

optimal_hits_1, optimal_faults_1 = optimal_page_replacement(
    phase1, frame_count
)

mru_hits_1, mru_faults_1 = mru_page_replacement(
    phase1, frame_count
)


# ==========================================
# Test Phase 2
# ==========================================

fifo_hits_2, fifo_faults_2 = fifo_page_replacement(
    phase2, frame_count
)

lru_hits_2, lru_faults_2 = lru_page_replacement(
    phase2, frame_count
)

optimal_hits_2, optimal_faults_2 = optimal_page_replacement(
    phase2, frame_count
)

mru_hits_2, mru_faults_2 = mru_page_replacement(
    phase2, frame_count
)


# ==========================================
# Display results
# ==========================================

print("==========================================")
print("LEARNED PAGE REPLACEMENT EXPERIMENT")
print("==========================================")

print("\nWorkload:")
print("Total references:", len(workload))
print("Phase 1 references:", len(phase1))
print("Phase 2 references:", len(phase2))
print("Number of frames:", frame_count)


print("\n==========================================")
print("PHASE 1 - LOCALITY HEAVY")
print("==========================================")

print("\nFIFO")
print("Hits:", fifo_hits_1)
print("Page faults:", fifo_faults_1)

print("\nLRU")
print("Hits:", lru_hits_1)
print("Page faults:", lru_faults_1)

print("\nOptimal")
print("Hits:", optimal_hits_1)
print("Page faults:", optimal_faults_1)

print("\nMRU")
print("Hits:", mru_hits_1)
print("Page faults:", mru_faults_1)


print("\n==========================================")
print("PHASE 2 - RANDOM")
print("==========================================")

print("\nFIFO")
print("Hits:", fifo_hits_2)
print("Page faults:", fifo_faults_2)

print("\nLRU")
print("Hits:", lru_hits_2)
print("Page faults:", lru_faults_2)

print("\nOptimal")
print("Hits:", optimal_hits_2)
print("Page faults:", optimal_faults_2)

print("\nMRU")
print("Hits:", mru_hits_2)
print("Page faults:", mru_faults_2)



training_data = create_training_data(
    workload,
    num_frames=3
)

model = train_eviction_model(training_data)

# Phase 1
learned_hits_1, learned_faults_1 = learned_page_replacement(
    phase1,
    num_frames=3,
    model=model
)

# Phase 2
learned_hits_2, learned_faults_2 = learned_page_replacement(
    phase2,
    num_frames=3,
    model=model
)

print("\n==========================================")
print("LEARNED")
print("==========================================")

print("\nPhase 1 - Locality Heavy")
print("Hits:", learned_hits_1)
print("Page faults:", learned_faults_1)
print("Hit ratio:", learned_hits_1 / len(phase1))

print("\nPhase 2 - Random")
print("Hits:", learned_hits_2)
print("Page faults:", learned_faults_2)
print("Hit ratio:", learned_hits_2 / len(phase2))
