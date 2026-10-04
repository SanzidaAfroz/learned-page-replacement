Learning-Augmented Page Replacement

This project studies how a simple learned component can be used with classical page replacement algorithms.

The implemented algorithms are FIFO, LRU, Optimal, and MRU. A learned page replacement policy is also included. It uses recent access information to make an eviction decision.
Learned Component

The learned policy uses two simple features:

    Recency: how recently a page was accessed

    Frequency: how often a page was accessed recently

A small Decision Tree classifier is trained using the Optimal policy as the teacher. The model then predicts which page is a suitable candidate for eviction.
Experiment

The experiment uses:

    3 page frames

    1000 total page references

    500 locality heavy references in Phase 1

    500 random references in Phase 2

The workload changes between the two phases to test how the policies behave after a change in access pattern.
Results
Policy	Phase 1 Faults	Phase 2 Faults
FIFO	189	472
LRU	181	472
Optimal	107	402
MRU	199	473
Learned	187	469

The complete results are available in results/results.md.
How to Run

Install the required library:

pip install scikit-learn

Then run:

python3 main.py

Project Structure

learned-page-replacement/
├── main.py
├── src/
│   ├── algorithms.py
│   ├── workload.py
│   └── learned.py
├── results/
│   └── results.md
├── README.md
└── .gitignore

AI Assistance

AI tools were used during development to help with code structure, debugging, explanations, and documentation. The final implementation and experimental results were tested and reviewed as part of the project.
