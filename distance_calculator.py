import numpy as np

class DistanceCalculator:
    def calculate_distance(self, vector1, vector2):
        # Use either L2 or Cosine distance calculation logic
        return np.linalg.norm(vector1 - vector2)  # L2 distance