Experimental Results

The experiment uses 3 page frames and a 1000-reference synthetic workload.

Phase 1: 500 locality-heavy references
Phase 2: 500 random references
Phase 1 - Locality Heavy
Policy	Hits	Page Faults	Hit Ratio
FIFO	311	189	0.622
LRU	319	181	0.638
Optimal	393	107	0.786
MRU	301	199	0.602
Learned	313	187	0.626
Phase 2 - Random
Policy	Hits	Page Faults	Hit Ratio
FIFO	28	472	0.056
LRU	28	472	0.056
Optimal	98	402	0.196
MRU	27	473	0.054
Learned	31	469	0.062
Hit Ratio

Hit ratio is calculated as:

Hit Ratio = Hits / Total References

The results show that the learned policy performs slightly better than FIFO, LRU, and MRU in the random phase. Optimal remains the best-performing policy because it has future knowledge of the complete reference sequence.

The learned policy is based on recency and frequency features and uses a Decision Tree to predict a suitable eviction candidate. Its performance changes when the workload shifts from locality-heavy access to random access.
