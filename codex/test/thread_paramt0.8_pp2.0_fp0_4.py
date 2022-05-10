import sys, threading
threading.Thread(target=lambda: sys.stdout.flush()).start()

import clustering_viz

def main(input_folder, output_folder, num_clusters):
    """
    Executes the pipeline.
    """
    
    # Load modules
    import load_data
    import process
    import cluster
    import result_analysis
    
    # Load the data
    print("Loading the data")
    songs = load_data.load_data(input_folder)
    
    # Process the data
    print("Processing the data")
    data = process.process_data(songs)
    
    # Cluster the data
    print("Clustering data")
    clusters = cluster.cluster(data, num_clusters)
    
    # Analyze results
    print("Analyzing results")
    analyses = result_analysis.analyze(clusters, songs, num_clusters)
    
    # Visualize results
    print("Visualizing results")
