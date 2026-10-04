def fifo_page_replacement(pages, frame_count):
    frames = []
    page_faults = 0
    hits = 0

    for page in pages:

        # Page is already in memory
        if page in frames:
            hits += 1

        # Page is not in memory
        else:
            page_faults += 1

            # There is still an empty frame
            if len(frames) < frame_count:
                frames.append(page)

            # All frames are full
            else:
                frames.pop(0)
                frames.append(page)

    return hits, page_faults

def lru_page_replacement(pages, frame_count):
    frames = []
    last_used = {}
    page_faults = 0
    hits = 0

    for time, page in enumerate(pages):

        # Page is already in memory
        if page in frames:
            hits += 1
            last_used[page] = time

        # Page is not in memory
        else:
            page_faults += 1

            # There is still an empty frame
            if len(frames) < frame_count:
                frames.append(page)

            # All frames are full
            else:
                # Find the least recently used page
                lru_page = min(frames, key=lambda p: last_used[p])

                frames.remove(lru_page)
                frames.append(page)

            last_used[page] = time

    return hits, page_faults

def optimal_page_replacement(pages, frame_count):
    frames = []
    page_faults = 0
    hits = 0

    for i, page in enumerate(pages):

        # Page is already in memory
        if page in frames:
            hits += 1
            continue

        # Page is not in memory
        page_faults += 1

        # There is still an empty frame
        if len(frames) < frame_count:
            frames.append(page)
            continue

        # Find which page will be used farthest in the future
        farthest_index = -1
        page_to_replace = None

        for frame_page in frames:

            # Look for the next occurrence of this page
            try:
                next_use = pages[i + 1:].index(frame_page)
                next_use += i + 1

            # Page is never used again
            except ValueError:
                next_use = float("inf")

            # Choose the page used farthest in the future
            if next_use > farthest_index:
                farthest_index = next_use
                page_to_replace = frame_page

        frames.remove(page_to_replace)
        frames.append(page)

    return hits, page_faults

def mru_page_replacement(pages, frame_count):
    frames = []
    last_used = {}
    page_faults = 0
    hits = 0

    for time, page in enumerate(pages):

        # Page is already in memory
        if page in frames:
            hits += 1
            last_used[page] = time

        # Page is not in memory
        else:
            page_faults += 1

            # There is still an empty frame
            if len(frames) < frame_count:
                frames.append(page)

            # All frames are full
            else:
                # Find the most recently used page
                mru_page = max(frames, key=lambda p: last_used[p])

                frames.remove(mru_page)
                frames.append(page)

            last_used[page] = time

    return hits, page_faults
