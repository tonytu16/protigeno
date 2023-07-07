import pickle
import csv

runtime_folder = 'test_seqs_runtime'

with open(runtime_folder + '/sampled_genomes.pickle', 'rb') as file:
    sampled_genomes = pickle.load(file)
with open(runtime_folder + '/num_test_seqs.pickle', 'rb') as file:
    num_seqs = pickle.load(file)
with open(runtime_folder + '/fasta_times.pickle', 'rb') as file:
    fasta_times = pickle.load(file)
with open(runtime_folder + '/bulk_compute.pickle', 'rb') as file:
    bulk_compute = pickle.load(file)
with open(runtime_folder + '/concat_tensors.pickle', 'rb') as file:
    concat_tensors = pickle.load(file)
    
rows = zip(sampled_genomes, num_seqs, fasta_times, bulk_compute, concat_tensors)

with open(runtime_folder + '/runtime.csv', 'w', newline='') as file:
    # Create a CSV writer object
    writer = csv.writer(file)
    writer.writerow(['Sampled genomes', 'Num seqs', 'Create fasta time', 'Bulk compute time', 'Concat tensors time'])
    
    # Write the data rows
    writer.writerows(rows)

