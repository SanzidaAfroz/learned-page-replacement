from sklearn.tree import DecisionTreeClassifier


def calculate_features(pages, position, candidate_pages, window_size=10):
    """
    Calculate recency and frequency for candidate pages.
    """

    recent_start = max(0, position - window_size)
    recent_pages = pages[recent_start:position]

    features = []

    for page in candidate_pages:

        # Recency
        last_position = None

        for i in range(position - 1, -1, -1):
            if pages[i] == page:
                last_position = i
                break

        if last_position is None:
            recency = window_size + 1
        else:
            recency = position - last_position

        # Frequency
        frequency = recent_pages.count(page)

        features.append((page, recency, frequency))

    return features


def get_optimal_eviction(pages, position, frames):
    """
    Find which page Optimal would evict.
    """

    farthest = -1
    victim = frames[0]

    for page in frames:

        try:
            next_use = pages[position + 1:].index(page)
        except ValueError:
            next_use = float("inf")

        if next_use > farthest:
            farthest = next_use
            victim = page

    return victim


def create_training_data(pages, num_frames, window_size=10):
    """
    Use Optimal as the teacher.

    1 = Optimal chooses this page for eviction
    0 = Optimal keeps this page
    """

    frames = []
    training_data = []

    for position, page in enumerate(pages):

        if page in frames:
            continue

        if len(frames) < num_frames:
            frames.append(page)
            continue

        # Ask Optimal which page should be evicted
        optimal_victim = get_optimal_eviction(
            pages,
            position,
            frames
        )

        # Calculate features
        features = calculate_features(
            pages,
            position,
            frames,
            window_size
        )

        # Create training examples
        for candidate, recency, frequency in features:

            label = 1 if candidate == optimal_victim else 0

            training_data.append(
                (recency, frequency, label)
            )

        # Simulate Optimal
        frames.remove(optimal_victim)
        frames.append(page)

    return training_data


def train_eviction_model(training_data):
    """
    Train Decision Tree.

    Features:
        recency
        frequency

    Label:
        1 = evict
        0 = keep
    """

    X = []
    y = []

    for recency, frequency, label in training_data:
        X.append([recency, frequency])
        y.append(label)

    model = DecisionTreeClassifier(
        max_depth=3,
        random_state=42
    )

    model.fit(X, y)

    return model


def learned_page_replacement(pages, num_frames, model, window_size=10):
    """
    Run the learned page replacement policy.
    """

    frames = []
    hits = 0
    faults = 0

    for position, page in enumerate(pages):

        # HIT
        if page in frames:
            hits += 1
            continue

        # PAGE FAULT
        faults += 1

        # Free frame
        if len(frames) < num_frames:
            frames.append(page)
            continue

        # Get candidate features
        features = calculate_features(
            pages,
            position,
            frames,
            window_size
        )

        # Predict which candidate should be evicted
        predictions = []

        for candidate, recency, frequency in features:

            prediction = model.predict(
                [[recency, frequency]]
            )[0]

            predictions.append(
                (candidate, prediction)
            )

        # Prefer a candidate predicted as eviction candidate
        eviction_candidates = [
            candidate
            for candidate, prediction in predictions
            if prediction == 1
        ]

        if eviction_candidates:
            victim = eviction_candidates[0]
        else:
            # Fallback: choose the page with highest recency
            victim = max(
                features,
                key=lambda x: x[1]
            )[0]

        frames.remove(victim)
        frames.append(page)

    return hits, faults

