import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import MDS

def main():
    # Load your distance matrix from the NPY file)
    distance_matrix = np.load('distance_matrix.npy')

    # Perform Multidimensional Scaling (MDS)
    # Perform Multidimensional Scaling (MDS)
    ds = MDS(n_components=2, dissimilarity='precomputed', random_state=10)
    embedded_coords = mds.fit_transform(distance_matrix)

    # Create a scatter plot to visualize the MDS results
    plt.figure(figsize=(10, 10))
    plt.scatter(embedded_coords[:,1], embedded_coords[:,0])
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Flag")
    plt.gca().invert_xaxis()
    plt.gca().invert_yaxis()
    plt.show()

if __name__ == '__main__':
    main()
