import signal
signal.signal(signal.SIGINT, signal.SIG_DFL) 

def save_only_viable_PPI(query_file, output_dir, ref_dir, ref_name_file, normalize):
    # Read the PPI file
    f = open(query_file, 'r')
    header = f.readline().replace('\n','').replace('\r','').split('\t')
    res = {}
    for i in range(7,len(header)):
        res[header[i]] = []
        
    for line in f:
        s = line.replace('\n','').replace('\r','').split('\t')
        for i in range(7,len(header)):
            res[header[i]].append(float(s[i]))
    f.close()
    
    # Get the number of PPI in each file
    NT_files = os.listdir(ref_dir)
    nb_PPI = [0]*len(NT_files)
    for i
