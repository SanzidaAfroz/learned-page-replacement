import random


def generate_workload(
    phase1_length=500,
    phase2_length=500,
    page_count=50,
    seed=42
):
    random.seed(seed)

    # -----------------------------
    # Phase 1: Locality-heavy
    # -----------------------------
    phase1 = []

    # Frequently access a small group of pages
    hot_pages = [1, 2, 3, 4, 5]

    for _ in range(phase1_length):
        page = random.choice(hot_pages)
        phase1.append(page)

    # -----------------------------
    # Phase 2: Random
    # -----------------------------
    phase2 = []

    for _ in range(phase2_length):
        page = random.randint(1, page_count)
        phase2.append(page)

    # Combine both phases
    workload = phase1 + phase2

    return workload, phase1, phase2
